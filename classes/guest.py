class Guest:
    def __init__(self, name, wallet, fav_artist, fav_title):
        self.name = name
        self.wallet = wallet
        self.fav_artist = fav_artist
        self.fav_title = fav_title

    def pay_entry_fee(self, room):
        self.wallet -= room.entry_fee
        room.till += room.entry_fee

    def favourite_song_in_room(self, room):
        for song in room.song_list:
            if song["Title"] == self.fav_title:
                return "Hurray"
            else:
                return "I don't like those songs"

    def buy_drink(self, room, drink_name):
        for drink in room.bar:
            if drink["Drink"] == drink_name:
                self.wallet -= drink["Price"]
                room.till += drink["Price"]