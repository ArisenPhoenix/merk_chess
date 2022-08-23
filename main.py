from chess_board import Board
from chess_players import Player
from main_helpers import *
from list_obj import List
from pprint import pprint as p

pygame.init()

p1 = Player(0, True)
p2 = Player(1, False)


board = Board(800, 800, [p1, p2])
p1.list = board.player_1_pieces
p2.list = board.player_2_pieces
players = [p1.list, p2.list]


def save_move_or_piece(list_object, position, turn_move, ):
    list_object.insert(0, position)
    list_object.choose()
    turn_move.append(position)


def piece_matches_coords(pos, piece_, piece, turn_move):
    if compare_coordinates(pos, piece.coords, 50) and not piece_.chosen:
        piece_.insert(0, (piece, piece.info()))
        turn_move.insert(0, (piece, piece.info()))
        piece_.choose()
        return True
    return False


def attempt_move_piece(selected_piece, space_to_go):
    print(f"moving piece {selected_piece} to {space_to_go}")
    return True


def play():
    playing = True  # For if False, no gameplay
    counter = 0  # For controlling flow of turns
    piece_ = List()  # For saving the piece that will move
    space_ = List()  # For saving the space for the piece to move to
    all_coors = List()  # I forgot, so i need to figure out why this is important, if at all.
    turn_move = List()  # For saving each individual move per turn purposes
    game_moves = List()  # For notation and saving game purposes
    while playing:
        board.mainloop(playing)
        ev = pygame.event.get()
        player_turn = None
        counter, player_turn = which_player(p1, p2, counter, player_turn)
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = get_pos(all_coors)
                for piece in player_turn:
                    if not piece_.chosen:
                        if piece_matches_coords(pos, piece_, piece, turn_move):
                            break
                    elif piece_.chosen and not space_.chosen and turn_move.num() < 2:
                        save_move_or_piece(space_, pos, turn_move)
                    elif piece_.chosen and space_.chosen and turn_move.num() == 2:
                        successful = attempt_move_piece(piece_[0], space_[0])
                        if successful:
                            counter = update_player_turns(p1, p2)
                            piece_ = List()
                            space_ = List()
                            all_coors = List()
                            turn_move = List()
                            break
                if turn_move.num() > 0:
                    print("turn_move.num(): ", turn_move.num())
                    for tile in board.tiles:
                        info = tile.info()
                        if info["contains"] == turn_move[0][0]:
                            print(f"{info['contains']} == {turn_move[0][0]}")
                            

play()
