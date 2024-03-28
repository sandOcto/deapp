from src.administration.business.interfaces.chambre_dao import ChambreDAOInterface
from src.administration.business.interfaces.chambre_presenter import (
    ChambrePresenterInterface,
)


class GetOneRoomUseCase:

    def __init__(
        self, room_dao: ChambreDAOInterface, presenter: ChambrePresenterInterface
    ):
        self.room_dao = room_dao
        self.presenter = presenter

    def execute(self):
        room = self.room_dao.get_a_room()
        self.presenter.execute([room])
