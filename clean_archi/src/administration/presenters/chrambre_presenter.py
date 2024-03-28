from src.administration.business.entities.chambre import Chambre
from src.administration.business.interfaces.chambre_presenter import (
    ChambrePresenterInterface,
)


class ChambrePresenter(ChambrePresenterInterface):

    def __init__(self) -> None:
        self.liste_chambres = None

    def execute(self, list_ch: list[Chambre]) -> None:
        self.liste_chambres = "hello"

    def get_stringified_liste_chambres(self) -> list[Chambre]:
        return self.liste_chambres
