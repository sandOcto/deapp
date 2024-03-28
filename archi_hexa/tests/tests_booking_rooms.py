import random

from src.room_service import RoomService

from .room_dao_spy import RoomDAOSpy

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
    ch_dao = RoomDAOSpy([])
    chambre_instance = RoomService(ch_dao)

    # when
    results = chambre_instance.get_all_rooms()

    # then
    assert len(results) == 0


def test_get_one_room():

    # given
    ch_dao = RoomDAOSpy(ALL_FAKE_ROOMS[0:1])
    chambre_instance = RoomService(ch_dao)

    # when
    results = chambre_instance.get_all_rooms()

    # then
    assert len(results) == 1
    assert results[0] == {"etage": 2, "numero": 1_000, "prix": 58.43}


def test_get_rooms():

    # given
    ch_dao = RoomDAOSpy(ALL_FAKE_ROOMS)
    chambre_instance = RoomService(ch_dao)

    # when
    results = chambre_instance.get_all_rooms()

    # then
    assert len(results) == 4


def test_update_room_prices():
    # given
    prix_rdc = 100
    dao_stub = RoomDAOSpy(ALL_FAKE_ROOMS)
    room_service = RoomService(dao_stub)
    # price_calculator = PriceCalculator(stub_room_service)

    # when
    room_service.update_room_prices(prix_rdc)

    # then
    updated_rooms_list = dao_stub.get_updated_rooms_list()

    assert updated_rooms_list == NEW_FAKE_ROOMS


def test_update_rooms_prices_max_200():
    # given
    prix_rdc = 199
    dao_stub = RoomDAOSpy(ALL_FAKE_ROOMS)
    room_service = RoomService(dao_stub)
    # price_calculator = PriceCalculator(stub_room_service)

    # when
    room_service.update_room_prices(prix_rdc)

    # then
    updated_rooms_list = dao_stub.get_updated_rooms_list()

    assert updated_rooms_list == NEW_FAKE_ROOMS_MAX_200
