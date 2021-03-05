import unittest

from classes.song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Enya", "Only Time")

    # test if song has an artist
    def test_has_an_artist(self):
        self.assertEqual("Enya",self.song.artist)

    # test if song has a title
    def test_has_a_song(self):
        self.assertEqual("Only Time", self.song.title)
        