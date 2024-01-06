#Tạo bảng
board = {'1': ' ', '2': ' ', '3': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' '}

#Combo chiến thắng
winning_combos = [('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9'),
                   ('1', '4', '7'), ('2', '5', '8'), ('3', '6', '9'),
                   ('1', '5', '9'), ('3', '5', '7')]

#Đánh dấu người chơi
player1 = 'X'
player2 = 'O'

#Tạo bảng
def print_board():
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

# Hàm chứng minh kết quả trận đấu
def is_game_over():
    # Check if there is a winner
    for combo in winning_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            print(f"{board[combo[0]]} is the winner!")
            return True
    # Kiểm tra xem bảng đã đấy chưa
    if ' ' not in board.values():
        print("It's a tie!")
        return True
    return False

#Tạo hàm tạo bước đi của người chơi
def get_move(player):
    while True:
        position = input(f"{player}, enter a position (1-9): ")
        if position in board and board[position] == ' ':
            break
        else:
            print("Invalid position. Try again.")
    board[position] = player

# tạo vòng lặp cho game
def play_game():
    # In bảng
    print_board()
    while not is_game_over():
        get_move(player1)
        print_board()
        if is_game_over():
            break
        get_move(player2)
        print_board()

# Bắt đầu game
play_game()