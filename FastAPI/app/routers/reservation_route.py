"""This module implements the FastAPI router for the reservation endpoints."""
from fastapi import APIRouter, Body, HTTPException
from ..models.reservation_model import Reservation
from ..services.reservation_service import (
    create_reservation_service,
    get_reservation_service,
    get_all_reservations_service,
    update_reservation_service,
    delete_reservation_service
)
from peewee import DoesNotExist

reservation_route = APIRouter()

@reservation_route.post("/")
def create_reservation(reservation: Reservation = Body(...)):
    """
    Endpoint to create a new reservation.

    Args:
        reservation (Reservation): The reservation data to create a new reservation.
    
    Returns:
        Reservation: The created reservation object.
    """
    return create_reservation_service(reservation)


@reservation_route.get("/{reservation_id}")
def read_reservation(reservation_id: int):
    """
    Endpoint to get a reservation by ID.

    Args:
        reservation_id (int): The ID of the reservation to retrieve.
    
    Returns:
        dict: The reservation details.
    
    Raises:
        HTTPException: If the reservation with the provided ID does not exist.
    """
    try:
        return get_reservation_service(reservation_id)
    except DoesNotExist as e:
        raise HTTPException(status_code=404, detail="Reservation not found") from e


@reservation_route.get("/")
def read_reservations():
    """
    Endpoint to retrieve all reservations.

    Returns:
        list: A list of all reservations.
    """
    return get_all_reservations_service()


@reservation_route.put("/{reservation_id}")
def update_reservation(reservation_id: int, reservation_data: Reservation = Body(...)):
    """
    Endpoint to update a reservation by ID.

    Args:
        reservation_id (int): The ID of the reservation to update.
        reservation_data (Reservation): The updated reservation data.
    
    Returns:
        Reservation: The updated reservation object.
    
    Raises:
        HTTPException: If the reservation with the provided ID does not exist.
    """
    try:
        return update_reservation_service(reservation_id, reservation_data)
    except DoesNotExist as e:
        raise HTTPException(status_code=404, detail="Reservation not found") from e


@reservation_route.delete("/{reservation_id}")
def delete_reservation(reservation_id: int):
    """
    Endpoint to delete a reservation by ID.

    Args:
        reservation_id (int): The ID of the reservation to delete.
    
    Returns:
        dict: A confirmation message that the reservation was deleted.
    
    Raises:
        HTTPException: If the reservation with the provided ID does not exist.
    """
    try:
        return delete_reservation_service(reservation_id)
    except DoesNotExist as e:
        raise HTTPException(status_code=404, detail="Reservation not found") from e
