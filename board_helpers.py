def board_setup():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    board = {}
    mult = 0
    for let in letters:
        for num in numbers:
            value = mult * len(numbers) + num
            key = f"{let}{num}"
            board[key] = value
        mult += 1
    return board



