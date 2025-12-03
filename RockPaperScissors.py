import random
wins = 0
losses = 0 
ties = 0
RPS = ['rock' , 'paper' , 'scissors']
while True:
    CHOICE = input('Choose! Rock, Paper, Scissors.. or (QUIT)').strip().lower()
    if CHOICE == 'quit':
        break
    if CHOICE not in RPS:
        print (f'I said, rock paper scissors. NOT {CHOICE}.')
        continue
    print ('Shoot!')
    AICHOICE = random.choice(RPS)

    print (f"Computer chose: {AICHOICE}!")

    print ('')

    if CHOICE == AICHOICE:
        print (f"You chose {CHOICE}! it's a tie!")
        ties += 1

    elif (CHOICE == 'rock' and AICHOICE == 'scissors') or \
        (CHOICE == 'scissors' and AICHOICE == 'paper') or \
        (CHOICE == 'paper' and AICHOICE == 'rock'):
        print ('You Win!')
        wins += 1
    else:
        print ('You Lose!')
        losses += 1 

    print ('')


    print (f"Your current score! \n ties : {ties} \n wins: {wins} \n losses: {losses}")
    if wins > 3:
        print ('your a winner!')
    elif losses > 3:
        print ("it's just a game of luck.")


    ask = input('would you like to play again? (Yes/No)').strip().lower()
    if ask == 'yes':
        continue
    else:
        break

# Elyas Muhammad Abbas
       # 3 / 3 