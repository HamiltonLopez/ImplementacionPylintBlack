"""This module contains the service functions for the reservation model."""
from models.reservation_model import Reservation

def create_reservation_service(reservation):
    """
    Creates a new reservation in the database.

    Args:
        reservation (Reservation): The reservation data to be saved.
    
    Returns:
        Reservation: The created reservation record.
    """
    reservation_record = Reservation.create(
        customer_id=reservation.customer_id,
        dateReservation=reservation.dateReservation,
        timeReservation=reservation.timeReservation
    )
    return reservation_record


def get_reservation_service(reservation_id: int):
    """
    Retrieves a reservation by its ID.

    Args:
        reservation_id (int): The ID of the reservation to retrieve.
    
    Returns:
        dict: The reservation details.
    
    Raises:
        DoesNotExist: If the reservation with the given ID does not exist.
    """
    reservation = Reservation.get_by_id(reservation_id)
    return {
        "id": reservation.id,
        "customer_id": reservation.customer_id,
        "dateReservation": reservation.dateReservation,
        "timeReservation": reservation.timeReservation,
    }


def get_all_reservations_service():
    """
    Retrieves all reservations from the database.

    Returns:
        list: A list of all reservation records.
    """
    reservations = list(Reservation.select())
    return [
        {
            "id": reservation.id,
            "customer_id": reservation.customer_id,
            "dateReservation": reservation.dateReservation,
            "timeReservation": reservation.timeReservation
        }
        for reservation in reservations
    ]


def update_reservation_service(reservation_id: int, reservation_data):
    """
    Updates an existing reservation by its ID.

    Args:
        reservation_id (int): The ID of the reservation to update.
        reservation_data (Reservation): The new data for the reservation.
    
    Returns:
        Reservation: The updated reservation record.
    
    Raises:
        DoesNotExist: If the reservation with the given ID does not exist.
    """
    reservation = Reservation.get_by_id(reservation_id)
    reservation.customer_id = reservation_data.customer_id
    reservation.dateReservation = reservation_data.dateReservation
    reservation.timeReservation = reservation_data.timeReservation
    reservation.save()
    return reservation


def delete_reservation_service(reservation_id: int):
    """
    Deletes a reservation from the database by its ID.

    Args:
        reservation_id (int): The ID of the reservation to delete.
    
    Returns:
        dict: A confirmation message.
    
    Raises:
        DoesNotExist: If the reservation with the given ID does not exist.
    """
    reservation = Reservation.get_by_id(reservation_id)
    reservation.delete_instance()
    return {"message": "Reservation deleted"}
