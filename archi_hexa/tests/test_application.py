# from src.room_service import RoomService

# from .room_dao_stub import RoomDAOStub
# from .tests_booking_rooms import ALL_FAKE_ROOMS


# def test_prix_etage_1():
#     # given
#     prix_rdc = 100
#     dao_stub = RoomDAOStub(ALL_FAKE_ROOMS)
#     stub_room_service = RoomService(dao_stub)
#     # price_calculator = PriceCalculator(stub_room_service)

#     # when
#     list_rooms = stub_room_service.update_room_prices(prix_rdc)

#     # then
#     assert all(room.prix == 100 for room in list_rooms if room.etage == 0)
#     assert all(room.prix == 107 for room in list_rooms if room.etage == 1)
#     assert all(room.prix == 122 for room in list_rooms if room.etage == 2)
#     assert all(room.prix == 133 for room in list_rooms if room.etage == 3)
