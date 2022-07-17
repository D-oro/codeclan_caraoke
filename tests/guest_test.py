import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Doro")

    def test_guest_has_name(self):
        self.assertEqual("Doro", self.guest.name)