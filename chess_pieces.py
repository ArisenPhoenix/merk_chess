import pygame


class Piece:
    """Generic Piece For Setting Basic Settings across all Pieces in Chess"""
    def __init__(self, name, color, square, coords):
        self.name = name
        self.square = square
        self.color = color
        self.coords = coords
        self.tile_data = {}
        self.piece = {"name": self.name, "color": self.color, "square": self.square, "coords": self.coords, "rules": {}}
    
    def info(self):
        """Prints and returns the info on the selected chess piece"""
        print(self.piece)
        return self.piece
        
    def listen(self):
        """Listen For Event Affecting A Chess Piece Object"""
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
                
    def add_tile_info(self, tile_data):
        self.tile_data = tile_data
                
                
class King(Piece):
    """King Piece"""
    def __init__(self, color, square, coords, name="King", board_name="K"):
        super().__init__(name, color, square, coords)
        self.name = name
        self.board_name = board_name
        self.color = color
        self.square = square
        self.coords = coords


class Queen(Piece):
    """Queen Piece"""
    def __init__(self, color, square, coords, name="Queen", board_name="Q"):
        super().__init__(name, color, square, coords)
        self.name = name
        self.board_name = board_name
        self.color = color
        self.square = square
        self.coords = coords
    
    
class Rook(Piece):
    """Rook Piece"""
    def __init__(self, color, square, coords, name="Rook", board_name="R"):
        super().__init__(name, color, square, coords)
        self.name = name
        self.board_name = board_name
        self.color = color
        self.square = square
        self.coords = coords
        
        
class Bishop(Piece):
    """Bishop Piece"""
    def __init__(self, color, square, coords, name="Bishop", board_name="B"):
        super().__init__(name, color, square, coords)
        self.name = name
        self.board_name = board_name
        self.color = color
        self.square = square
        self.coords = coords
        

class Knight(Piece):
    """Knight Piece"""
    def __init__(self, color, square, coords, name="Knight", board_name="N"):
        super().__init__(name, color, square, coords)
        self.name = name
        self.board_name = board_name
        self.color = color
        self.square = square
        self.coords = coords
        
        
class Pawn(Piece):
    """Pawn Piece"""
    def __init__(self, color, square, coords, name="Pawn", board_name="P"):
        super().__init__(name, color, square, coords)
        self.name = name
        self.board_name = board_name
        self.color = color
        self.square = square
        self.coords = coords
        

class Empty(Piece):
    """Empty Piece"""
    def __init__(self, color, square, coords, name="", board_name=""):
        super().__init__(name, color, square, coords)
        self.name = name
        self.board_name = board_name
        self.color = color
        self.square = square
        self.coords = coords
    
