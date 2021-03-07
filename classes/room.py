class Room():
    def __init__(self, number, capacity, song_list, till):
        self.number = number
        self.capacity = capacity
        self.song_list = song_list
        self.till = till

        self.guest_list = []
        self.entry_fee = 50

    def add_guest_to_room(self, guest):
        if (self.room_capacity() == "Welcome") and (self.guest_can_afford_entry(guest) == True):
            self.guest_list.append(guest.name)

    def remove_guest_from_room(self, guest):
        self.guest_list.remove(guest)

    def add_song_to_list(self, song):
        self.song_list.append(song)

    def remove_song_from_room(self, song_title):
        for song in self.song_list:
            if song["Title"] == song_title:
                self.song_list.remove(song)

    def room_capacity(self):
        if len(self.guest_list) < self.capacity:
            return "Welcome"
        else:
            return "Sorry, room is full"

    def guest_can_afford_entry(self, guest):
        return self.entry_fee < guest.wallet