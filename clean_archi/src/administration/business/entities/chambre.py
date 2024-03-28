class Chambre:

    etage: int
    numero: int
    prix: float

    def __init__(self, etage: int, numero: int, prix: float) -> None:
        self.etage = etage
        self.numero = numero
        self.prix = prix

    def update_price(self, prix_rdc: float) -> None:

        if self.etage == 0:
            self.prix = prix_rdc
        elif self.etage == 1:
            self.prix = prix_rdc * 1.07
        elif self.etage == 2:
            self.prix = prix_rdc * 1.22
        elif self.etage == 3:
            self.prix = prix_rdc * 1.33
        else:
            raise ValueError("Invalid floor number")

        if self.prix > 200:
            self.prix = 200
