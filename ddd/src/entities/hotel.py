from .chambre import Chambre


class Hotel:

    hotel_id: str
    liste_chambres: list[Chambre]

    def __init__(self, liste_chambres: list[Chambre]) -> None:
        self.liste_chambres = liste_chambres

    def appliquer_augmentation(self, prix_rdc: float) -> None:
        for chambre in self.liste_chambres:
            chambre.update_price(prix_rdc)

    def get_chambres(self) -> list[Chambre]:
        return self.liste_chambres
