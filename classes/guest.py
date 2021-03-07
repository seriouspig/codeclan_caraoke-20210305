class Guest:
    def __init__(self, name, wallet, fav_artist, fav_title):
        self.name = name
        self.wallet = wallet
        self.fav_artist = fav_artist
        self.fav_title = fav_title

    def pay_entry_fee(self, room_fee):
        self.wallet -= room_fee