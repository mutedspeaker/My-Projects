from random import randint as rp
a = ['rock', 'paper', 'scissor']


def win(m, n):
    if m and n in a:
        if m == n:
            return 'd'
        elif m == "rock":
            if n == 'paper':
                return 2
            else:
                return 1
        elif m == 'paper':
            if n == 'scissor':
                return 2
            else:
                return 1
        else:
            if n == 'paper':
                return 1
            else:
                return 2


def checker():
    i = input('Enter rock, paper or scissor: \n').lower()
    if i in a:
        return i
    else:
        print('Please enter only rock,paper or scissor!!!')
        checker()


def play():
    j = checker()
    b = rp(0, 2)
    k = a[b]
    s = win(j, k)
    print(f'You chose : {j.capitalize()}.\nAnd the computer chose : {k.capitalize()}.'
          f'\nSo,')
    if s == 'd':
        print('It is a draw!\n')
        re()
    else:
        if s == 1:
            print('You win!!\n')
            re()

        else:
            print('The computer wins!!\n')
            re()


def re():
    r = input('You wanna replay??\n')
    print('\n\n')
    if r.lower() in ['y', 'yes']:
        play()
    else:
        exit()


play()
