from chess_board import Board
from chess_players import Player
from main_helpers import *
from list_obj import List

pygame.init()

p1 = Player(0, True)
p2 = Player(1, False)

board = Board(800, 800, [p1, p2])
p1.list = board.player_1_pieces
p2.list = board.player_2_pieces
players = [p1.list, p2.list]


def attempt_move_piece(selected_piece, space_to_go):
    print(f"moving piece {selected_piece} to {space_to_go}")
    return True



    
    



def slight_startup(boolean):
    boolean = True
    return boolean


def slight_reset(boolean):
    boolean = False
    return boolean


def reset_values():
    # global counter,   piece_, space_, all_coors, turn_move, can_move
    counter = 0
    piece_ = List()
    space_ = List()
    all_coors = List()
    turn_move = List()
    can_move = False


def piece_matches_coords(pos, piece_list, piece, turn_move):
    if compare_coordinates(pos, piece_list.coords, 50) and not piece_list.chosen:
        print("Match")
        if not piece_list.chosen:
            piece_list.insert(0, piece.info)
            turn_move.append(piece.info)
            piece_list.chosen = True
            return True
    return False


def play():
    playing = True
    counter = 0
    moves = List()
    piece_ = List()
    space_ = List()
    all_coors = List()
    turn_move = List()
    can_move = False
    can_select_piece = True
    # global counter,   piece_, space_, all_coors, turn_move, can_move, playing
    while playing:
        board.mainloop(playing)
        ev = pygame.event.get()
        player_turn = None
        counter, player_turn = which_player(p1, p2, counter, player_turn)
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("piece is chosen? ", piece_.chosen)
                pos = get_pos(all_coors)
                for piece in player_turn:
                    if piece_matches_coords(pos, piece, piece_, turn_move):
                        break
                    elif not space_.chosen and turn_move.num() < 2:
                        space_.insert(0, pos)
                        space_.choose()
                        turn_move.append(pos)
                        print("Can Now Pick Tile")
                        break
                    elif piece_.chosen and space_.chosen and turn_move.num() == 2:
                        print("tile chosen")
                        print(space_)
                        successful = attempt_move_piece(piece_[0], space_[0])
                        if successful:
                            print(turn_move)
                            # Switches Player Turns and returns a 0 for the counter.
                            counter = update_player_turns(p1, p2)
                            reset_values()
                    else:
                        return play()
                        
                        
# playing, counter,   piece_, space_, all_coors, turn_move
play()









