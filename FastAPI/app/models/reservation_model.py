"""
This module contains the Pydantic model for reservation data.
"""
from datetime import date, time
from pydantic import BaseModel


class Reservation(BaseModel):
    """
    Reservation model class.
    Attributes:
        id (int): The ID of the reservation.
        customer_id (int): The ID of the customer associated with the reservation.
        dateReservation (date): The date of the reservation.
        timeReservation (time): The time of the reservation.
    """

    id: int
    customer_id: int
    dateReservation: date
    timeReservation: time
