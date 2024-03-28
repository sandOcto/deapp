from typing import Protocol

from src.entities.hotel import Hotel


class HotelRepoImpl(Protocol):

    def get_hotel(self, hotel_id: str) -> Hotel:
        pass
