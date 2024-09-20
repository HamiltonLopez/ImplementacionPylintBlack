"""
This module contains the Pydantic model for customer data.
"""
from pydantic import BaseModel


class Customer(BaseModel):
    """
    Customer model class.
    Attributes:
        id (int): The unique identifier of the customer.
        name (str): The name of the customer.
        phone (str): The phone number of the customer.
        email (str): The email address of the customer.
    """

    id: int
    name: str
    phone: str
    email: str
