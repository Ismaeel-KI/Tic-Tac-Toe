
def canva(value):
    def colored(val):
        if val == 'X':
            return f"\033[91mX\033[0m"  # Red
        elif val == 'O':
            return f"\033[94mO\033[0m"  # Blue
        return ' '

    print(f'''
      1   2   3
    _____________
  A | {colored(value['A1'])} | {colored(value['A2'])} | {colored(value['A3'])} |
    |___|___|___|
  B | {colored(value['B1'])} | {colored(value['B2'])} | {colored(value['B3'])} |
    |___|___|___|
  C | {colored(value['C1'])} | {colored(value['C2'])} | {colored(value['C3'])} |
    |___|___|___|
    ''')

def winning_condition(value):
    winning_combo = [
        ['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['C1', 'C2', 'C3'],
        ['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'], ['A3', 'B3', 'C3'],
        ['A1', 'B2', 'C3'], ['A3', 'B2', 'C1']
    ]
    for combo in winning_combo:
        if all(value[cell] == 'X' for cell in combo):
            return 'X'
        elif all(value[cell] == 'O' for cell in combo):
            return 'O'
    return None

def is_full(board):
    return " " not in board.values()

def empty_cells(board):
    empty = [cell for cell, val in board.items() if val == " "]
    return empty

def minimax(board, depth, alpha, beta, maximizing, ai, human):
    winner = winning_condition(board)
    if winner == ai:
        return 10 - (9 - depth), None
    elif winner == human:
        return -10 + (9 - depth), None
    elif is_full(board):
        return 0, None

    if maximizing:
        best_val = float('-inf')
        best_move = None
        for cell in empty_cells(board):
            board[cell] = ai
            val, _ = minimax(board, depth-1, alpha, beta, False, ai, human)
            board[cell] = ' '
            if val > best_val:
                best_val, best_move = val, cell
            alpha = max(alpha, val)
            if beta <= alpha:
                break
        return best_val, best_move
    else:
        best_val = float('inf')
        best_move = None
        for cell in empty_cells(board):
            board[cell] = human
            val, _ = minimax(board, depth-1, alpha, beta, True, ai, human)
            board[cell] = ' '
            if val < best_val:
                best_val, best_move = val, cell
            beta = min(beta, val)
            if beta <= alpha:
                break
        return best_val, best_move


def play():
    values = {
        "A1": ' ',
        "A2": ' ',
        "A3": ' ',
        "B1": ' ',
        "B2": ' ',
        "B3": ' ',
        "C1": ' ',
        "C2": ' ',
        "C3": ' ',
    }

    canva(values)
    game_on = True
    human = input("Choose Your symbol 'X' or 'O': ").upper()
    ai = 'O' if human == 'X' else 'X'
    turn = 'X'

    while game_on:
        if turn == human:
            user_choice = input('Enter the place: ').upper()
            if user_choice in values:
                if values[user_choice] not in ['X', 'O']:
                    values[user_choice] = human
                    turn = ai
                else:
                    print('Already Occupied. Try Again!')
            else:
                print('Wrong Value, Try Again!')
        else:
            print("AI is thinking...")
            _, move = minimax(board=values, depth= 9, alpha= float('-inf'), beta= float('inf'), maximizing= True, ai=ai, human=human)
            values[move] = ai
            turn = human

        canva(values)

        winner = winning_condition(values)
        if winner:
            print(f'{winner} Won !!')
            break
        if is_full(values):
            print("Draw !!\n\n\n")
            print('Try Again')
            play()

play()