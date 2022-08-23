import pygame
from chess_tiles import Tile
from chess_piece_options import get_piece
from pprint import pprint as p

white_num = 150
white = (white_num, white_num, white_num)
black_num = 35
black = (black_num, black_num, black_num)
white_piece_color = (255, 51, 153)
black_piece_color = (51, 255, 51)


def mainloop(playing):
    """Main Loop For Chess Game"""
    for an_event in pygame.event.get():
        if an_event.type == pygame.QUIT:
            playing = False
        if not playing:
            quit()
            exit()


class Board:
    """Chess Board Class"""
    def __init__(self, width, height, players_list=None):
        self.board = pygame
        self.player_1_pieces = []
        self.player_2_pieces = []
        self.width = width
        self.height = height
        display = self.board.display
        display.init()
        display.set_caption("Merk Chess")
        self.window = display.set_mode((self.width, self.height))
        self.populate_tiles()
        self.mainloop = mainloop
        
    def populate_tiles(self):
        """Main Function For Setting Up the Chess Board With Tiles and Pieces"""
        tile = self.board.draw.rect
        rect_width = self.width / 8
        rect_height = self.height / 8
        surf = self.board.display.set_mode((self.width, self.height))
        x = y = 0
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        
        def create_horizontal_rects(x_coor, y_coor, color1, color2, p_color1, p_color2, num):
            """Creates the Horizontal Squares Before Moving Down"""
            location = (x_coor, y_coor)
            for a_tile in range(8):
                text_coords = (a_tile * rect_width, y_coor)
                tile_num = num + 1
                tile_letter = letters[a_tile]
                tile_name = f"{tile_letter}{tile_num}"
                piece = get_piece((tile_letter, tile_num))
                board_coords = text_coords
                piece_color = p_color2
                piece_initiated = None
                
                if piece[1] == "color1":
                    piece_color = p_color1
                    
                if piece[0] is not None:
                    piece_initiated = piece[0](piece_color, tile_name, board_coords)
                tile_info = {
                    "coords": (x_coor, y_coor), "dims": (rect_width, rect_height),
                    "location": location, "tile": tile_name, "board_coords": board_coords
                }
                piece_ = piece_initiated
                
                if piece[1] == "color1":
                    self.player_1_pieces.append(piece_initiated)
                    piece_initiated.add_tile_info(tile_info)
                elif piece[1] == "color2":
                    self.player_2_pieces.append(piece_initiated)
                    piece_initiated.add_tile_info(tile_info)
                tile_data = self.board.Rect(x_coor, y_coor, rect_width, rect_height)
                
                if a_tile % 2 == 0:
                    Tile(color1, color2, location, tile_name, text_coords,
                         tile(surf, color1, tile_data), self.window, board_coords,
                         piece_initiated)
                    
                if a_tile % 2 == 1:
                    
                    Tile(color2, color1, location, tile_name, text_coords,
                         tile(surf, color2, tile_data), self.window, board_coords,
                         piece_initiated)
                x_coor += rect_width
        
        for column in range(8):
            if column % 2 == 0:
                create_horizontal_rects(x, y, white, black, white_piece_color, black_piece_color, column)
            if column % 2 == 1:
                create_horizontal_rects(x, y, black, white, white_piece_color, black_piece_color, column)
            y += rect_width
            self.board.display.flip()
        return surf
    
    def update_board(self):
        self.board.display.update(self.window)
        
    def get_all_piece_info(self):
        """Returns a dictionary with both players and all their pieces."""
        def list_info(player_list):
            info_list = []
            for item in player_list:
                info_list.append(item.info())
            return info_list
        
        p1 = list_info(self.player_1_pieces)
        p2 = list_info(self.player_2_pieces)

        lists = {"player1": p1, "player2": p2}
        p(lists)
        return lists
        