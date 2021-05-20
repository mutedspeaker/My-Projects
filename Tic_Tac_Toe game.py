def con(num):
    if num == 1:
        return 0, 0
    elif num == 2:
        return 0, 1
    elif num == 3:
        return 0, 2
    elif num == 4:
        return 1, 0
    elif num == 5:
        return 1, 1
    elif num == 6:
        return 1, 2
    elif num == 7:
        return 2, 0
    elif num == 8:
        return 2, 1
    elif num == 9:
        return 2, 2
    else:
        nu = int(input("Please enter number from 1 to 9"))
        con(nu)


def play():
    a = input("Player 1 do you wanna play Y/n? \n")
    if a.lower() == 'y' or a.lower() == 'yes':
        b, c = "O", "X"
        user_input(arr, b, c)


def replay():
    a = input("Player 1 do you wanna replay Y/n? \n")
    if a.lower() in ['y', 'yes']:
        b, c = "O", "X"
        arr = [[i + 3 * j + 1 for i in range(3)] for j in range(3)]
        user_input(arr, b, c)


def display(bozo):
    for i in bozo:
        d = ''
        for j in i:
            d += str(j)+'|'
        d = d[:len(d) - 1]
        print(d)


def win(dust):
    for i in dust:
        if i[0] == i[1] and i[0] == i[2]:
            print(i)
            return 't'
    if dust[0][0] == dust[1][0] and dust[0][0] == dust[2][0]:
        return 't'
    elif dust[0][1] == dust[1][1] and dust[0][1] == dust[2][1]:
        return 't'
    elif dust[0][2] == dust[1][2] and dust[0][2] == dust[2][2]:
        return 't'
    elif dust[0][0] == dust[1][1] and dust[1][1] == dust[2][2]:
        return 't'
    elif dust[0][2] == dust[1][1] and dust[1][1] == dust[2][0]:
        return 't'
    else:
        return dust


def user_input(game_board, first_symbol, second_symbol):
    d = 1
    for i in range(9):
        store = []
        num = int(input('Enter the number : \n'))
        if 10 > num > 0:
            store.append(num)
            if d % 2 != 0:
                h = con(num)
                game_board[h[0]][h[1]] = first_symbol
                print('\n'*3)
                display(game_board)
                earth = win(game_board)
                if earth == 't':
                    print('\n'*3)
                    print('Player 1 won')
                    replay()
                    break
                print("Turn of Player 2 (X)")
            else:
                h = con(num)
                game_board[h[0]][h[1]] = second_symbol
                print('\n'*3)
                display(game_board)
                earth = win(game_board)
                if earth == 't':
                    print('\n' * 3)
                    print('Player 2 won')
                    replay()
                    break
                print("Turn of Player 1 (O)")
            d += 1
    else:
        print("It's a draw guys!")
        replay()


arr = [[i+3*j+1 for i in range(3)] for j in range(3)]
for i in range(3):
    for j in range(3):
        arr[i][j] = str(arr[i][j])
print('Welcome to the Tic Tac Toe game!')
print('')
display(arr)
print('')
play()