import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Thank God It's Friday")

    def test_song_has_name(self):
        self.assertEqual("Thank God It's Friday", self.song.name)