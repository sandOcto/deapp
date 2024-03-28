from src.administration.business.interfaces.chambre_dao import ChambreDAOInterface


class GetAllRoomsUseCase:

    def __init__(self, room_dao: ChambreDAOInterface):
        self.room_dao = room_dao

    def execute(self):
        return self.room_dao.get_all_rooms()
