# This function is for entering the character of the player according to the number he chose for it.
# A number from 1 - 9 and if you enter anything else it just loops on till eternity unless you give it what it wants.


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


# This, as you can see asks the player if he wants to play the game or not.
def play():
    a = input("Player 1 do you wanna play Y/n? \n")
    if a.lower() == 'y' or a.lower() == 'yes':
        b, c = "O", "X"
        user_input(arr, b, c)
    elif a.lower() == 'n' or a.lower() == 'no':
        exit(00)
    else:
        play()


# WHen the game ends, if the players wanna go again then this one comes into play, in hindsight I feel it should have
# been named "Rematch".
def replay():
    a = input("Player 1 do you wanna replay Y/n? \n")
    if a.lower() in ['y', 'yes']:
        b, c = "O", "X"
        ar = [[i + 3 * j + 1 for i in range(3)] for j in range(3)]
        user_input(ar, b, c)
    elif a.lower() == 'n' or a.lower() == 'no':
        exit(000)
    else:
        replay()


# Hehe, nice argument name innit? This one shows the current position of the board. Used by Technoblade's arch rival
def display(bozo):
    for i in bozo:
        d = ''
        for j in i:
            d += str(j) + '|'
        d = d[:len(d) - 1]
        print(d)


# This is what decides if the user won or they lost or well surprisingly drew, my bet is you'd lose with me tho ;).
def win(dust):
    d = 0
    for i in dust:
        if i[0] == i[1] and i[0] == i[2]:
            print(1)
            return 't'
    if dust[0][0] == dust[1][0] and dust[0][0] == dust[2][0]:
        print(2)
        return 't'
    elif dust[0][1] == dust[1][1] and dust[0][1] == dust[2][1]:
        print(3)
        return 't'
    elif dust[0][2] == dust[1][2] and dust[0][2] == dust[2][2]:
        print(4)
        return 't'
    elif dust[0][0] == dust[1][1] and dust[1][1] == dust[2][2]:
        print(5)
        return 't'
    elif dust[0][2] == dust[1][1] and dust[1][1] == dust[2][0]:
        print(6)
        return 't'
    else:
        return dust


# This one takes in the user input and the current board to put in the symbol.
def user_input(game_board, first_symbol, second_symbol):
    arty = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    party = []
    d = 1
    for i in range(9):
        store = []
        num = int(input('Enter the number : \n'))
        if num in party:
            print("The entered number has already been chosen. Please pick another number.")
        if num > 9 or num < 1:
            print("Please enter a number between 1 and 9 as shown in the board.")
        if num in arty:
            store.append(num)
            party.append(num)
            arty.remove(num)
            if d % 2 != 0:
                h = con(num)
                game_board[h[0]][h[1]] = first_symbol
                print('\n' * 3)
                display(game_board)
                earth = win(game_board)
                if earth == 't':
                    print('\n' * 3)
                    print('Player 1 won')
                    replay()
                    break
                print("Turn of Player 2 (X)")
            elif d == 9:
                print(' ')
            else:
                h = con(num)
                game_board[h[0]][h[1]] = second_symbol
                print('\n' * 3)
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


# This generates the board
# List comprehension it is
arr = [[i + 3 * j + 1 for i in range(3)] for j in range(3)]
for i in range(3):
    for j in range(3):
        arr[i][j] = str(arr[i][j])

# This welcomes you to the game, bet you didn't know that, ha!
print('Welcome to the Tic Tac Toe game!')

# This is for an empty line.
print('')

# This displays the board.
display(arr)

# Another empty line.
print('')

# Boom the game is afoot.
play()
