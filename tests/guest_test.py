import unittest

from classes.guest import Guest
from classes.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("John Wick", 300, "Enya", "Only Time")
        self.guest2 = Guest("Frank Booth", 1000, "Bobby Vinton" , "Blue Velvet")
        self.guest3 = Guest("Hannibal Lecter", 30, "Angie Gold" , "Eat You Up")
        self.guest4 = Guest("Michael Myers", 60, "Peter Murphy" , "Cuts You Up")
        self.guest5 = Guest("Norman Bates", 150, "Pink Floyd" , "Mother")
        self.guest6 = Guest("Rich Hannibal Lecter", 100, "Angie Gold" , "Eat You Up")

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

    # test the customer paying the entry fee and passing money to room till
    def test_guest_pays_entry_fee(self):        
        self.guest1.pay_entry_fee(self.room1)
        self.assertEqual(250, self.guest1.wallet)
        self.assertEqual(50, self.room1.till)
        
    # test weather the customer's favourite song is on the playlist    
    def test_guest_favourite_song_in_room(self):
        self.assertEqual("Hurray", self.guest1.favourite_song_in_room(self.room1))
        self.assertEqual("I don't like those songs", self.guest3.favourite_song_in_room(self.room1))

    # test customer buying drinks and passing the money to the room till
    def test_guest_buys_drink(self):
        self.guest1.buy_drink(self.room1, "Beer")
        self.guest2.buy_drink(self.room1, "Wine")
        self.guest3.buy_drink(self.room1, "Vodka")
        self.assertEqual(295, self.guest1.wallet)
        self.assertEqual(990, self.guest2.wallet)
        self.assertEqual(15, self.guest3. wallet)
        self.assertEqual(30, self.room1.till)