
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


def player_turn(user, sym, turn, count):
    user_choice = input(f'{user}: Enter the place: ').upper()
    if user_choice in value.keys():
        if value[user_choice] not in ['X', 'O']:
            value[user_choice] = sym
            canva(value)
            count += 1
            return not turn, count
        else:
            print('Already Occupied. Try Again!')
    else:
        print('Wrong Value, Try Again!')

    return turn, count


def winning_condition(value, game_on):
    winning_combo = winning_combinations = [
        ['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['C1', 'C2', 'C3'],  # rows
        ['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'], ['A3', 'B3', 'C3'],  # columns
        ['A1', 'B2', 'C3'], ['A3', 'B2', 'C1']  # diagonals
    ]
    if all(value[cell] == 'X' for cell in winning_combo):
        print('Winner is User1!!')
        return not game_on
    elif all(value[cell] == 'O' for cell in winning_combo):
        print('Winner is User2!!')
        return not game_on


value = {
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
canva(value)
game_on = True
player1_turn = True
count = 0

while game_on:
    if player1_turn:
        player1_turn, count = player_turn(user='User1', sym='X', turn=player1_turn, count=count)
    else:
        player1_turn, count = player_turn(user='User2', sym='O', turn=player1_turn, count=count)

    if count >= 6:
        game_on = winning_condition(value, game_on)
    if count == 9 and game_on:
        print("It's a Draw!")
        break

