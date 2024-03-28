from src.administration.business.entities.chambre import Chambre
from src.administration.business.interfaces import RoomDAOInterface


class RecupererChambresDAOStub(RoomDAOInterface):

    def __init__(self, rooms: list[Chambre]):
        self.rooms = rooms
        self.updated_rooms = []

    def get_all_rooms(self) -> list[Chambre]:
        return self.rooms

    # def update_room_prices(self, rooms: list[Chambre]):
    #     self.updated_rooms = rooms

    # def get_updated_rooms_list(self) -> list[Chambre]:
    #     return self.updated_rooms
