import unittest

from classes.room import Room 
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        song_list1 = [
            {"Artist": "Enya", "Title": "Only Time"},
            {"Artist": "Bobby Vinton", "Title": "Blue Velvet"}
        ]

        self.guest1 = Guest("John Wick", 300, "Enya", "Only Time")
        self.guest2 = Guest("Frank Booth", 1000, "Bobby Vinton" , "Blue Velvet")
        self.guest3 = Guest("Hannibal Lecter", 30, "Angie Gold" , "Eat You Up")
        self.guest4 = Guest("Michael Myers", 60, "Peter Murphy" , "Cuts You Up")
        self.guest5 = Guest("Norman Bates", 150, "Pink Floyd" , "Mother")
        self.guest6 = Guest("Rich Hannibal Lecter", 100, "Angie Gold" , "Eat You Up")

        self.room1 = Room(1, 10, song_list1, 0)
        self.room2 = Room(2, 5, song_list1, 0)

    # test that room has a number
    def test_room_has_a_number(self):
        self.assertEqual(1, self.room1.number)

    # test that room has a maximum capacity
    def test_room_has_a_capacity(self):
        self.assertEqual(10, self.room1.capacity)

    # test that room has a song list - find by artist name
    def test_room_has_a_song_list_artist(self):
        self.assertEqual("Enya",self.room1.song_list[0]["Artist"])

    # test that room has a song list - find by title name
    def test_room_has_a_song_list_title(self):
        self.assertEqual("Blue Velvet", self.room1.song_list[1]["Title"])

    # test that guest can check to the room
    def test_check_guest_to_room(self):
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_guest_to_room(self.guest2)
        self.assertEqual("John Wick",self.room1.guest_list[0])
        self.assertEqual("Frank Booth",self.room1.guest_list[1])

    # test that guest can check out from the room
    def test_checkout_guest_from_room(self):
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_guest_to_room(self.guest2)
        self.room1.remove_guest_from_room(self.guest1.name)
        self.assertEqual(["Frank Booth"], self.room1.guest_list)

    # test adding new song to the rooms song list
    def test_add_song_to_room(self):
        new_song = {"Artist": "Rick Astley", "Title": "Never Gonna Give You Up"}
        self.room1.add_song_to_list(new_song)
        self.assertEqual("Never Gonna Give You Up", self.room1.song_list[2]["Title"])

    # test removing song from the rooms song list
    def test_remove_song_from_room(self):
        self.room1.remove_song_from_room("Only Time")
        self.assertEqual(1, len(self.room1.song_list))
        self.assertEqual("Blue Velvet", self.room1.song_list[0]["Title"])

    # test that room is not full
    def test_room_capacity_not_full(self):
        self.room1.room_capacity()
        self.assertEqual("Welcome", self.room1.room_capacity())

    # test that room is full
    def test_room_capacity_full(self):
        self.room2.add_guest_to_room(self.guest1)
        self.room2.add_guest_to_room(self.guest2)
        self.room2.add_guest_to_room(self.guest6)
        self.room2.add_guest_to_room(self.guest4)
        self.room2.add_guest_to_room(self.guest5)
        self.room2.room_capacity()
        self.assertEqual("Sorry, room is full", self.room2.room_capacity())

    # test if new guest can afford the entry fee
    def test_guest_can_afford_entry_fee(self):
        self.assertEqual(True, self.room1.guest_can_afford_entry(self.guest1))
        self.assertEqual(False, self.room1.guest_can_afford_entry(self.guest3))

   
