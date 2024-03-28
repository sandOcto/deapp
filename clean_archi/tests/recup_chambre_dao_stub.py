from src.administration.business.entities.chambre import Chambre
from src.administration.business.interfaces.chambre_dao import ChambreDAOInterface


class RecupererChambresDAOStub(ChambreDAOInterface):

    def __init__(self, rooms: list[Chambre]):
        self.rooms = rooms

    def get_all_rooms(self) -> list[Chambre]:
        return self.rooms

    def get_a_room(self) -> Chambre:
        return self.rooms[0]
