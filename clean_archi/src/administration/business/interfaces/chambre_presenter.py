from typing import Protocol

from src.administration.business.entities.chambre import Chambre


class ChambrePresenterInterface(Protocol):

    def execute(self, list_ch: list[Chambre]) -> None:
        raise NotImplementedError()
