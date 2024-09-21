"""
This module contains the routes for managing customer data.
"""
from fastapi import APIRouter, Body, HTTPException
from models.customer_model import Customer
from services.customer_service import (
    create_customer_service,
    get_customer_service,
    get_all_customers_service,
    update_customer_service,
    delete_customer_service,
)
from peewee import DoesNotExist

customer_route = APIRouter()

@customer_route.post("/")
def create_customer(customer: Customer = Body(...)):
    """
    Creates a new customer.
    Parameters:
    - customer (Customer): The customer object to be created.
    Returns:
    - The created customer object.
    """

    return create_customer_service(customer)


@customer_route.get("/{customer_id}")
def read_customer(customer_id: int):
    """
    Retrieves a customer by their ID.
    Args:
        customer_id (int): The ID of the customer to retrieve.
    Returns:
        Customer: The customer object.
    Raises:
        HTTPException: If the customer is not found.
    """

    try:
        return get_customer_service(customer_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Customer not found") from exc


@customer_route.get("/")
def read_customers():
    """
    Reads and returns all customers.
    Returns:
        List[Customer]: A list of all customers.
    """

    return get_all_customers_service()


@customer_route.put("/{customer_id}")
def update_customer(customer_id: int, customer_data: Customer = Body(...)):
    """
    Update a customer with the given customer_id and customer_data.
    Parameters:
    - customer_id (int): The ID of the customer to update.
    - customer_data (Customer): The updated customer data.
    Returns:
    - The updated customer.
    Raises:
    - HTTPException: If the customer with the given ID does not exist.
    """
    try:
        return update_customer_service(customer_id, customer_data)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Customer not found") from exc


@customer_route.delete("/{customer_id}")
def delete_customer(customer_id: int):
    """
    Deletes a customer with the given customer_id.
    Args:
        customer_id (int): The ID of the customer to be deleted.
    Returns:
        None
    Raises:
        HTTPException: If the customer does not exist.
    """

    try:
        return delete_customer_service(customer_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Customer not found") from exc
