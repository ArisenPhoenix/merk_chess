from chess_board import Board
import pygame
from chess_players import Player
from pprint import pprint as p

pygame.init()

p1 = Player(0, True)
p2 = Player(1, False)

board = Board(800, 800, [p1, p2])
p1.list = board.player_1_pieces
p2.list = board.player_2_pieces
players = [p1.list, p2.list]


def compare_coordinates(_pos, _piece, num):
    _piece = (_piece[0] + 50, _piece[1] + 50)
    if _pos[0] - num < _piece[0] < _pos[0] + num and _pos[1] - num < _piece[1] < _pos[1] + num:
        print(f"THESE LOCATIONS MATCH: ", (_pos, _piece))
        return True
    else:
        return False


def attempt_move_piece(piece_to_move, space_to_go):
    print(f"moving piece {piece_to_move} to {space_to_go}")
    return True


def which_player(check, player):
    if p1.turn:
        player = p1.list
        if check == 0:
            print("player 1")
            check += 1
    elif p2.turn:
        player = p2.list
        if check == 0:
            print("player 2")
            check += 1
    return check, player


playing = True
counter = 0
click_coors = []
can_move = False
piece_ = []
space_ = []
can_select_piece = True
while playing:
    ev = pygame.event.get()
    player_turn = None
    counter, player_turn = which_player(counter, player_turn)
    for event in ev:
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            click_coors.append(pos)
        for piece in player_turn:
            if compare_coordinates(event.pos, piece.coords, 50):
                piece_.insert(0, piece.info)
        if len(click_coors) == 2:
            can_move = True
        if len(piece_) >= 1:
            space_.insert(0, pos)
            print(f"Want to go to {pos}")
            if len(piece_) >= 1 and len(space_) >= 1:
                if can_move:
                    print("CAN MOVE PIECE NOW!")
                    if attempt_move_piece(piece_[0], space_[0]):
                        print("attempt move is True")
                        p1.player_turn()
                        p2.player_turn()
                        counter = 0
                

    board.mainloop(playing)





