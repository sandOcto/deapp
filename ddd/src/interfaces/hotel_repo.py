from typing import Protocol

from src.entities.hotel import Hotel


class HotelRepoInterface(Protocol):

    def get_hotel(self, hotel_id: str) -> Hotel:
        raise NotImplementedError("get_hotel method not implemented")
