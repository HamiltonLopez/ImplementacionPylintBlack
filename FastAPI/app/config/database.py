"""This module contains the database configuration and models for the FastAPI application."""
import os
from dotenv import load_dotenv
from app.config.settings import DATABASE
from peewee import AutoField, CharField, DateField, ForeignKeyField, Model, MySQLDatabase, TimeField



database = MySQLDatabase(
    DATABASE["name"],
    user=DATABASE["user"],
    passwd=DATABASE["password"],
    host=DATABASE["host"],
    port=DATABASE["port"],
)
class Customer(Model):
    """
    Represents a customer in the database.

    Attributes:
        id (int): The unique identifier for the customer.
        name (str): The name of the customer.
        phone (str): The phone number of the customer.
        email (str): The email address of the customer.
    """
    id = AutoField(primary_key=True)
    name = CharField(max_length=100)
    phone = CharField(max_length=15)
    email = CharField(max_length=100)

    class Meta:
        """Defines the metadata for the Customer model."""
        database = database
        table_name = "customers"

class Reservation(Model):
    """
    Represents a reservation in the database.

    Attributes:
        id (int): The unique identifier for the reservation.
        customer (Customer): The customer associated with the reservation.
        date (datetime.date): The date of the reservation.
        time (datetime.time): The time of the reservation.
    """
    id = AutoField(primary_key=True)
    customer = ForeignKeyField(Customer, backref='reservations')
    date = DateField()
    time = TimeField()

    class Meta:
        """Defines the metadata for the Reservation model."""
        database = database
        table_name = "reservations"
