from src.room import Room
from src.room_dao_port import RoomDAOInterface


class RoomDAOSpy(RoomDAOInterface):

    def __init__(self, rooms: list[Room]):
        self.rooms = rooms
        self.updated_rooms = []

    def get_all_rooms(self) -> list[Room]:
        return self.rooms

    def update_room_prices(self, rooms: list[Room]):
        self.updated_rooms = rooms

    def get_updated_rooms_list(self) -> list[Room]:
        return self.updated_rooms
