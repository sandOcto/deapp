import random

from src.administration.business.entities.chambre import Chambre
from src.administration.business.rules.use_cases.recuperer_chambres import (
    GetAllRoomsUseCase,
)
from src.administration.business.rules.use_cases.recuperer_une_chambre import (
    GetOneRoomUseCase,
)
from src.administration.presenters.chrambre_presenter import ChambrePresenter

from .recup_chambre_dao_stub import RecupererChambresDAOStub

ALL_FAKE_ROOMS = [
    {"etage": 0, "numero": 2, "prix": 50},
    {"etage": 2, "numero": 1_000, "prix": 58.43},
    {"etage": 1, "numero": 101, "prix": 53.5},
    {"etage": 3, "numero": 102, "prix": 53.5},
]


NEW_FAKE_ROOMS = [
    {"etage": 0, "numero": 2, "prix": 100},
    {"etage": 2, "numero": 1_000, "prix": 122},
    {"etage": 1, "numero": 101, "prix": 107},
    {"etage": 3, "numero": 102, "prix": 133},
]

NEW_FAKE_ROOMS_MAX_200 = [
    {"etage": 0, "numero": 2, "prix": 199},
    {"etage": 2, "numero": 1_000, "prix": 200},
    {"etage": 1, "numero": 101, "prix": 200},
    {"etage": 3, "numero": 102, "prix": 200},
]


def test_get_no_rooms():

    # given
    ch_dao = RecupererChambresDAOStub([])
    use_case_get_all_chambres = GetAllRoomsUseCase(ch_dao)

    # when
    liste_chambres = use_case_get_all_chambres.execute()

    # then
    assert len(liste_chambres) == 0


def test_get_one_room():

    # given
    chambre = Chambre(
        etage=2,
        numero=1_000,
        prix=58.43,
    )
    ch_dao = RecupererChambresDAOStub([chambre])
    presenter = ChambrePresenter()

    use_case_one_chambre = GetOneRoomUseCase(ch_dao, presenter)

    # when
    use_case_one_chambre.execute()
    result = presenter.get_stringified_liste_chambres()

    print(result)

    # then
    assert result.etage == 2
    assert result.numero == 1_000
    assert result.prix == 58.43
    assert isinstance(result, Chambre)


# def test_get_rooms():

#     # given
#     ch_dao = RoomDAOSpy(ALL_FAKE_ROOMS)
#     chambre_instance = RoomService(ch_dao)

#     # when
#     results = chambre_instance.get_all_rooms()

#     # then
#     assert len(results) == 4


# def test_update_room_prices():
#     # given
#     prix_rdc = 100
#     dao_stub = RoomDAOSpy(ALL_FAKE_ROOMS)
#     room_service = RoomService(dao_stub)
#     # price_calculator = PriceCalculator(stub_room_service)

#     # when
#     room_service.update_room_prices(prix_rdc)

#     # then
#     updated_rooms_list = dao_stub.get_updated_rooms_list()

#     assert updated_rooms_list == NEW_FAKE_ROOMS


# def test_update_rooms_prices_max_200():
#     # given
#     prix_rdc = 199
#     dao_stub = RoomDAOSpy(ALL_FAKE_ROOMS)
#     room_service = RoomService(dao_stub)
#     # price_calculator = PriceCalculator(stub_room_service)

#     # when
#     room_service.update_room_prices(prix_rdc)

#     # then
#     updated_rooms_list = dao_stub.get_updated_rooms_list()

#     assert updated_rooms_list == NEW_FAKE_ROOMS_MAX_200
