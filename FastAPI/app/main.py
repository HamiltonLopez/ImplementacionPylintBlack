"""This module is the main module of the FastAPI application."""

from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from starlette.responses import RedirectResponse
from app.helpers.api_key_auth import get_api_key
from app.database import database as connection
from app.routes.customer_route import customer_route
from app.routes.reservation_route import reservation_route

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Asynchronous context manager for managing the lifespan of the FastAPI application.

    Parameters:
    - application (FastAPI): The FastAPI application instance.

    Yields:
    None

    Raises:
    None

    Notes:
    - This context manager ensures that the database connection is 
    opened before yielding and closed after yielding.
    - If the connection is already closed before entering the context, it will be reconnected.
    """
    if connection.is_closed():
        connection.connect()
    try:
        yield
    finally:
        if not connection.is_closed():
            connection.close()

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    """
    Redirects the root path to the documentation.

    Returns:
    RedirectResponse: A response that redirects to the documentation.
    """
    return RedirectResponse(url="/docs")

# ----------------CUSTOMERS----------------
app.include_router(customer_route, tags=["Customers"], prefix="/api/customers", dependencies=[Depends(get_api_key)])

# ----------------RESERVATIONS----------------
app.include_router(reservation_route, tags=["Reservations"], prefix="/api/reservations", dependencies=[Depends(get_api_key)])
