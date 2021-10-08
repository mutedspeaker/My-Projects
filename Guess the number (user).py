lower = int(input("Enter lower range for the number from which I am going to guess. :D \n"))
higher = int(input("Now enter the higher range.\n"))


def checker():
    n = input().lower()
    if n in ['g', 'l', 'r']:
        return n
    else:
        print("Please enter g,l or r only !!")
        checker()


def comp_guess(a, b):
    c = (b + a)//2
    while True:
        print(f'If {c} is greater than your guess, input "g",\n'
              f'if it is lesser than your guess input "l"\n'
              f'and if it is your guess input "r". :D\n')
        i = checker()
        if i == 'g':
            b = c
            c = c = (b + a)//2
        elif i == 'l':
            a = c
            c = (b + a) // 2
        else:
            print("Yay, guess was right!!!!!")
            print('The mission was successful boys, WE DID IT!')
            break


comp_guess(lower, higher)
