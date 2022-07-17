import unittest
from classes.room import Room
from classes.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("Doro")
        self.room = Room("room1", 4)

    def test_room_has_name(self):
        self.assertEqual("room1", self.room.name)

    def test_add_guest_to_room(self, guest1):
        self.add_guest_to_room(guest1)
        self.assertEqual(1, len(self.guests_in_room))