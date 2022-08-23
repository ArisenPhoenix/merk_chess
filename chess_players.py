class Player:
    """Player Object For Chess."""
    def __init__(self, number, turn=bool):
        self.number = number
        self.turn = turn
        self.list = []
        self.move_list = []
        if self.number == 0:
            self.turn = True
            # print(f"player {self.number + 1} turn: ", self.turn)
        else:
            self.turn = False
            # print(f"player {self.number + 1} turn: ", self.turn)

    def player_turn(self):
        """Toggles player turn from False to True and from True to False"""
        self.turn = not self.turn
        if self.turn:
            print(f"player {self.number + 1} turn: ", self.turn)
    
    def add_move(self, move: tuple):
        """move should be a tuple of coordinates and squares"""
        self.move_list.append(move)
    