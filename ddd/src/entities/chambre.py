class Etage:
    numero: int
    augmentation_map: dict = {
        0: 1,
        1: 7,
        2: 22,
        3: 33,
    }

    def get_augmentation(self):
        return self.augmentation_map[self.numero]


class Prix:
    _valeur: float

    def __init__(self, valeur) -> None:
        self._valeur = valeur

    def appliquer_augmentation(self, pourcentage: float):

        new_price = self._valeur * pourcentage / 100

        if new_price > 200:
            new_price = 200

        return Prix(new_price)


class Chambre:

    etage: Etage
    numero: int
    prix: Prix

    def __init__(self, etage: Etage, numero: int, prix: Prix) -> None:
        self.etage = etage
        self.numero = numero
        self.prix = prix

    def update_price(self, prix_rdc: float) -> None:

        self.prix = Prix(prix_rdc).appliquer_augmentation(self.etage.get_augmentation())
