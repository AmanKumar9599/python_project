print('Welcome to the GAME!!!')
print('"Guess the number"')
name=input('Hi BUDDY what\'s your name\n')
print(name,'Let\'s play the game')
print("NOTE-- Your numbers have difference of atleast 20")
a=int(input('Enter the first number\n'))
b=int(input('Enter the second number\n'))
if (a-b>19 or b-a>19):
    import random
    num=random.randint(a,b)
    level=input('Which level do you wants to play\n"Easy"/"Hard"\n').upper()
    if level=='EASY':
        print("You have 10 chances to guess the number.")
        for i in range(1,11):
            inc=int(input('let\'s guess the number:'))
            if(num==inc):
                print('You correctly guess the number.')
                print('Your score is',10-i)
                break
            else:
                if(inc<num):
                    print('Your number is lower than the guessed number.')
                else:
                    print('Your number is higher than the guessed number.')

    elif level=="HARD":
        print("You have 5 chances to guess the number.")
        for i in range(1,6):
            inc=int(input('let\'s guess the number:'))
            if(num==inc):
                print('You correctly guess the number.')
                print('Your score is',5-i)
                break
            else:
                if(inc<num):
                    print('Your number is lower than the guessed number.')
                else:
                    print('Your number is higher than the guessed number.')
else:
    print("You haven\'t input desired data.")