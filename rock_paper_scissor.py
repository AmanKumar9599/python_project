def rock():
    import random
    print('Welcome to the Rock, Paper and Scissor game.')
    print(f'''HOPE YOU KNOW THE BASICS OF THE GAME 
FOR YOUR CONVENINCE I WOULD LIKE TO REMIND YOU OF THE RULES FOLLOWED IN IT
1.ROCKS BEATS SCISSOR
2.SCISSOR BEATS PAPER
3.PAPER BEATS ROCK''')

    a=input('With whom you wants to play\nEnter \"Player\" or \"Computer\"\n')
    pvc=a.upper()
    ls=['ROCK','PAPER','SCISSOR']
    if(pvc=='COMPUTER'):
        player=input("Enter your choice 'Rock' / 'paper' / 'Scissor'\n").upper()
        print("Your choice is",player)
        comp=random.choice(ls)
        print("Computer choice is",comp)
        if(player=='ROCK' and comp=='SCISSOR' or player=='SCISSOR' and comp=='PAPER' or player=='PAPER' and comp=='ROCK' ):
            print('You win!')
        elif(comp=='ROCK' and player=='SCISSOR' or comp=='SCISSOR' and player=='PAPER' or comp=='PAPER' and player=='ROCK' ):
            print('Computer Win!')
        else:
            print("Draw!")
    elif(pvc=='PLAYER'):
        p1=input('Enter your name:\n')
        p2=input('Enter your name:\n')
        c1=input("Enter 'Rock' / 'paper' / 'Scissor'\n").upper()
        c2=input("Enter 'Rock' / 'paper' / 'Scissor'\n").upper()
        if(c1=='ROCK' and c2=='SCISSOR' or c1=='SCISSOR' and c2=='PAPER' or c1=='PAPER' and c2=='ROCK' ):
            print(p1,'win!')
        elif(c2=='ROCK' and c1=='SCISSOR' or c2=='SCISSOR' and c1=='PAPER' or c2=='PAPER' and c1=='ROCK' ):
            print(p2,'Win!')
        else:
            print("Draw!")
rock()
rematch=input('Do you want to play again\nEnter "Yes" or "No"\n').upper()
while rematch=='YES':
    rock()