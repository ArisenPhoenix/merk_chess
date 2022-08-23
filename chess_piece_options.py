from chess_pieces import *


def king(king_obj):
    k = king_obj
    print(k)
    
    
def queen(king_obj):
    k = king_obj
    print(k)
    
    
def rook(king_obj):
    k = king_obj
    print(k)
    
    
def bishop(king_obj):
    k = king_obj
    print(k)
    
    
def knight(king_obj):
    k = king_obj
    print(k)
    
    
def pawn(king_obj):
    k = king_obj
    print(k)
    
    
def get_piece(loc):
    let = loc[0]
    num = loc[1]
    piece = None
    color = ""
    piece_type = ""
    
    if num == 1 or num == 2:
        color = "color1"
    elif num == 8 or num == 7:
        color = "color2"
    else:
        # print("That can't be a number at setup.")
        color = None
    
    if num != 8 and num != 7 and num != 2 and num != 1:
        piece = None
    else:
        if let == "A" or let == "H":
            if num == 7 or num == 2:
                piece = Pawn
                piece_type = "Pawn"
            else:
                piece = Rook
                piece_type = "Rook"
        elif let == "B" or let == "G":
            if num == 7 or num == 2:
                piece = Pawn
                piece_type = "Pawn"
            else:
                piece = Knight
                piece_type = "Knight"
        elif let == "C" or let == "F":
            if num == 7 or num == 2:
                piece = Pawn
                piece_type = "Pawn"
            else:
                piece = Bishop
                piece_type = "Bishop"
        elif let == "D":
            if num == 7 or num == 2:
                piece = Pawn
                piece_type = "Pawn"
            else:
                piece = Queen
                piece_type = "Queen"
        elif let == "E":
            if num == 7 or num == 2:
                piece = Pawn
                piece_type = "Pawn"
            else:
                piece = King
                piece_type = "King"
        
    return piece, color, piece_type


