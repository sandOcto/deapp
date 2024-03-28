from src.entities.hotel import Hotel
from src.interfaces.hotel_repo import HotelRepoInterface


class RecupererHotelRepoStub(HotelRepoInterface):

    def __init__(self, hotels: list[Hotel]):
        self.hotels = hotels

    def get_hotel(self, hotel_id: str) -> Hotel:
        for hotel in self.hotels:
            if hotel.hotel_id == hotel_id:
                return hotel
        return None
