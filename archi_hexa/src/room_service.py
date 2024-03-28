from .room import Room
from .room_dao_port import RoomDAOInterface


class RoomService:

    def __init__(self, dao: RoomDAOInterface):
        self.dao = dao

    def get_all_rooms(self) -> list[Room]:
        return self.dao.get_all_rooms()

    def update_room_prices(self, prix_rdc: float) -> None:
        rooms = self.get_all_rooms()
        for room in rooms:

            if room["etage"] == 0:
                room["prix"] = prix_rdc
            elif room["etage"] == 1:
                room["prix"] = prix_rdc * 1.07
            elif room["etage"] == 2:
                room["prix"] = prix_rdc * 1.22
            elif room["etage"] == 3:
                room["prix"] = prix_rdc * 1.33
            else:
                raise ValueError("Invalid floor number")

            if room["prix"] > 200:
                room["prix"] = 200

        self.dao.update_room_prices(rooms)
