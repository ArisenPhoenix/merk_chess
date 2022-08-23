import pygame


def update_player_turns(p1, p2):
    """Switches Player Turns and return a 0 counter"""
    print("Switching Turns")
    p1.player_turn()
    p2.player_turn()
    return 0


def which_player(p1, p2, check, player):
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


def get_pos(coors_list):
    pos = pygame.mouse.get_pos()
    coors_list.append(pos)
    return pos


def compare_coordinates(_pos, _piece, num):
    _piece = (_piece[0] + 50, _piece[1] + 50)
    if _pos[0] - num < _piece[0] < _pos[0] + num and _pos[1] - num < _piece[1] < _pos[1] + num:
        print(f"THESE LOCATIONS MATCH: ", (_pos, _piece))
        return True
    else:
        return False








