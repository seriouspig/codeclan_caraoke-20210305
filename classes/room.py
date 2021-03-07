class Room():
    def __init__(self, number, capacity, song_list, till):
        self.number = number
        self.capacity = capacity
        self.song_list = song_list
        self.till = till

        self.guest_list = []
        self.entry_fee = 50

        self.bar = [
            {"Drink": "Beer", "Price":5},
            {"Drink": "Wine", "Price":10},
            {"Drink": "Vodka", "Price":15}
        ]

    # adding guest to the room if he can afford it and the room is not full
    def add_guest_to_room(self, guest):
        if (self.room_capacity() == "Welcome") and (self.guest_can_afford_entry(guest) == True):
            self.guest_list.append(guest.name)

    # removing guest from the room
    def remove_guest_from_room(self, guest):
        self.guest_list.remove(guest)

    # adding a song to the room's song list
    def add_song_to_list(self, song):
        self.song_list.append(song)

    # removing song from the room's song list by song title
    def remove_song_from_room(self, song_title):
        for song in self.song_list:
            if song["Title"] == song_title:
                self.song_list.remove(song)

    # checkign if room can accept more guests and returning adequate message
    def room_capacity(self):
        if len(self.guest_list) < self.capacity:
            return "Welcome"
        else:
            return "Sorry, room is full"

    # checking if guest can afford the entry fee
    def guest_can_afford_entry(self, guest):
        return self.entry_fee < guest.wallet