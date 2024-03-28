from src.interfaces.hotel_repo import HotelRepoInterface


class GetHotelUseCase:

    def __init__(self, hotel_repository: HotelRepoInterface):
        self.hotel_repository = hotel_repository

    def execute(self, hotel_id: str):
        return self.hotel_repository.get_hotel(hotel_id)
