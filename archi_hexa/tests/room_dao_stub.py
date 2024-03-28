from src.room import Room
from src.room_dao_port import RoomDAOInterface


class RoomDAOStub(RoomDAOInterface):

    def __init__(self, rooms: list[Room]):
        self.rooms = rooms

    def get_all_rooms(self) -> list[Room]:
        return self.rooms
