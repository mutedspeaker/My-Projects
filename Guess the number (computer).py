import random
a = random.randint(0, 1001)
print("I have chosen a random number between 1 and 1000")
print("I'll tell if you're near of further away from the number")
while True:
    b = int(input("Enter your guess number. \n"))
    if b == 1001:
        print(a)
    if b == a:
        print("You guessed the actual number !!!!")
        break
    c = abs(a - b)
    if c < 2:
        print('(+-2)')
    elif c < 3:
        print('(+-3)')
    elif c < 5:
        print('(+-5)')
    elif c < 10:
        print('(+-10)')
    elif c//10 < 3:
        print("(+-30)")
    elif c//10 < 5:
        print("(+-50)")
    elif c//10 < 10:
        print("(+-100)")
    elif c//10 < 50:
        print("(+-500)")
    else:
        print('(+-1000)')
