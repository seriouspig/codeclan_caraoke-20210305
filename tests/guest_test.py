import unittest

from classes.guest import Guest
from classes.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("John Wick", 300, "Enya", "Only Time")
        self.guest2 = Guest("Frank Booth", 1000, "Bobby Vinton" , "Blue Velvet")

        song_list1 = [
            {"Artist": "Enya", "Title": "Only Time"},
            {"Artist": "Bobby Vinton", "Title": "Blue Velvet"}
        ]

        self.room1 = Room(1, 10, song_list1, 0)
        self.room2 = Room(2, 5, song_list1, 0)

    # test guest has a name
    def test_guest_has_a_name(self):
        self.assertEqual("John Wick", self.guest1.name)

    # test guest has a wallet
    def test_guest_has_a_wallet(self):
        self.assertEqual(1000, self.guest2.wallet)

    # test guest has a favourite artist
    def test_guest_has_a_favourite_artist(self):
        self.assertEqual("Enya", self.guest1.fav_artist)

    # test guest has a favourite song
    def test_guest_has_a_favourite_song(self):
        self.assertEqual("Blue Velvet", self.guest2.fav_title)

    def test_guest_pays_entry_fee(self):        
        self.guest1.pay_entry_fee(self.room1.entry_fee)
        self.assertEqual(250, self.guest1.wallet)
        