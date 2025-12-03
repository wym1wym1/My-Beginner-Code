import random 


while True:
    answer = random.randint(1, 10)
    for i in range(0, 3):
        quit = False
        guess = int(input('guess a number bettwen 1, 10. '))
        if guess == answer:
            print ('u guessed right Attempts taken:', i)
            retry = input('would you like to play again? Yes/No').strip().lower()
            if retry == 'yes':
                print('alright. playing again.')
                break
            elif retry == 'no':
                print ('okay bye bye')
                quit = True
        else:
            print ('try again. Attempt number:', i + 1)
    else:
        print ('out of attempts.')
        retry = input('would you like to play again? Yes/No').strip().lower()
        if retry == 'yes':
            print ('alright. win this time!')
        elif retry == 'no':
            print ('okay bye bye')
            quit = True

    if quit:
        break

 # WYM1
