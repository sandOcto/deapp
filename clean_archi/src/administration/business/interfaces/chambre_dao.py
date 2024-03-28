from typing import Protocol

from src.administration.business.entities.chambre import Chambre


class ChambreDAOInterface(Protocol):

    def get_all_rooms(self) -> list[Chambre]:
        raise NotImplementedError("get_all_rooms method not implemented")

    def get_a_room(self) -> Chambre:
        raise NotImplementedError("get_a_room method not implemented")
