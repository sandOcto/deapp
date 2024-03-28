from typing import Protocol

from src.room import Room


class RoomDAOInterface(Protocol):

    def get_all_rooms(self) -> list[Room]:
        raise NotImplementedError("get_all_rooms method not implemented")

    def update_room_prices(self, rooms: list[Room]):
        raise NotImplementedError("update_room_prices method not implemented")
