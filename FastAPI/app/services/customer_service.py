"""This module contains the service functions for the customer model."""
from app.models.customer_model import Customer


def create_customer_service(customer):
    """
    Creates a new customer in the database.

    Args:
        customer (Customer): An object containing the customer details.
        
    Returns:
        CustomerModel: The created customer record.
    """
    customer_record = Customer.create(
        name=customer.name,
        phone=customer.phone,
        email=customer.email
    )
    return customer_record


def get_customer_service(customer_id: int):
    """
    Retrieves a customer by their ID.

    Args:
        customer_id (int): The ID of the customer to retrieve.
        
    Returns:
        dict: A dictionary containing the customer's data.
        
    Raises:
        DoesNotExist: If the customer with the given ID does not exist.
    """
    customer = Customer.get_by_id(customer_id)
    return {
        "id": customer.id,
        "name": customer.name,
        "phone": customer.phone,
        "email": customer.email,
    }


def get_all_customers_service():
    """
    Retrieves all customers from the database.

    Returns:
        list: A list of dictionaries containing the data of all customers.
    """
    customers = list(Customer.select())
    return [
        {
            "id": customer.id,
            "name": customer.name,
            "phone": customer.phone,
            "email": customer.email
        }
        for customer in customers
    ]


def update_customer_service(customer_id: int, customer_data):
    """
    Updates an existing customer’s details by their ID.

    Args:
        customer_id (int): The ID of the customer to update.
        customer_data (Customer): An object containing the updated customer details.
        
    Returns:
        CustomerModel: The updated customer record.
        
    Raises:
        DoesNotExist: If the customer with the given ID does not exist.
    """
    customer = Customer.get_by_id(customer_id)
    customer.name = customer_data.name
    customer.phone = customer_data.phone
    customer.email = customer_data.email
    customer.save()
    return customer


def delete_customer_service(customer_id: int):
    """
    Deletes a customer from the database by their ID.

    Args:
        customer_id (int): The ID of the customer to delete.
        
    Returns:
        dict: A message confirming the deletion.
        
    Raises:
        DoesNotExist: If the customer with the given ID does not exist.
    """
    customer = Customer.get_by_id(customer_id)
    customer.delete_instance()
    return {"message": "Customer deleted"}
