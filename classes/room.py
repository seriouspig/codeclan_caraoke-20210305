class Room():
    def __init__(self, number, capacity, song_list, till):
        self.number = number
        self.capacity = capacity
        self.song_list = song_list
        self.till = till

        self.guest_list = []

    def add_guest_to_room(self, guest):
        self.guest_list.append(guest)

    def remove_guest_from_room(self, guest):
        self.guest_list.remove(guest)

    def add_song_to_list(self, song):
        self.song_list.append(song)

    def remove_song_from_room(self, song_title):
        for song in self.song_list:
            if song["Title"] == song_title:
                self.song_list.remove(song)