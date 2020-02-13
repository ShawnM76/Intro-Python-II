# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def player_move(self, name, current_room):
        return f"{self.name} now moves to {self.current_room}"
