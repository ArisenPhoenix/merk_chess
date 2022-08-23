from pprint import pprint as p
import pygame.font


class Tile:
    def __init__(self, color1, color2, location, text, text_loc, rect_object, full, coords, piece=None):
        self.rect_object = rect_object
        self.text_coordinates = text_loc
        self.board = full
        self.color = color1
        self.color2 = color2
        self.location = location
        self.font = pygame.font.SysFont("Arial", 25)
        self.piece = piece
        self.coords = coords
        self.tile = {
            "color": self.color, "contains": self.piece,
            "location": self.location, "tile": self.rect_object, "board object": self.board
        }
        
        self.text = text
        self.tile["board object"].blit(self.font.render(self.text, True, color2), self.text_coordinates)
        if piece is not None:
            self.tile["board object"].blit(self.font.render(self.piece.board_name, True, self.piece.color),
                                           (self.text_coordinates[0] + 45, self.text_coordinates[1] + 45))
    
    def info(self, print_=False):
        """Prints and Returns all the info in a dictionary for a given tile."""
        if print_:
            p(self.tile)
        return self.tile

    def add_piece(self, piece):
        """Sets the inital state for a tile when there is one piece on it."""
        self.tile["contains"] = piece
    
    def remove_piece(self):
        """Sets the tile back to being empty."""
        self.tile["contains"] = None
    
    def take_piece(self, piece1, piece2):
        """Switches two pieces when one piece takes another."""
        print(f"{piece2} takes {piece1}")
        self.tile["contains"] = piece2
    
    def piece_info(self):
        """Provides piece info on the selected tile."""
        self.piece.info()
