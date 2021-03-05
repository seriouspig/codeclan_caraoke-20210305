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

        self.room1 = Room(1, 10, song_list1, 0)

    def test_room_has_a_number(self):
        self.assertEqual(1, self.room1.number)

    def test_room_has_a_capacity(self):
        self.assertEqual(10, self.room1.capacity)

    def test_room_has_a_song_list_artist(self):
        self.assertEqual("Enya",self.room1.song_list[0]["Artist"])

    def test_room_has_a_song_list_title(self):
        self.assertEqual("Blue Velvet", self.room1.song_list[1]["Title"])

    def test_check_guest_to_room(self):
        self.room1.add_guest_to_room(self.guest1.name)
        self.room1.add_guest_to_room(self.guest2.name)
        self.assertEqual("John Wick",self.room1.guest_list[0])
        self.assertEqual("Frank Booth",self.room1.guest_list[1])
        # print(self.room1.guest_list)

    def test_checkout_guest_from_room(self):
        self.room1.add_guest_to_room(self.guest1.name)
        self.room1.add_guest_to_room(self.guest2.name)
        self.room1.remove_guest_from_room(self.guest1.name)
        self.assertEqual(["Frank Booth"], self.room1.guest_list)
        # print(self.room1.guest_list)