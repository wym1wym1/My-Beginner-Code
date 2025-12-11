import random 

words = (
    'cat', 'dog', 'elephant', 'giraffe', 'lion', 'tiger', 'apple', 'banana', 'carrot', 
    'pizza', 'burger', 'chocolate', 'table', 'chair', 'lamp', 'phone', 'bottle', 'book', 
    'pen', 'notebook', 'bicycle', 'train', 'airplane', 'hat', 'shoe', 'watch', 'spoon', 
    'fork', 'mouse', 'keyboard'
)


word = random.choice(words)
display = ['_'] * len(word)
guessed_lets = []
wrong_lets = []


def guess():
    guess = input('Guess a letter\n- ')
    if guess.isalpha() and len(guess) == 1:
        return guess
    else:
        print('Invalid input')
        return False


def correctguess(word, guess):
    if guess in guessed_lets:
        print('Already Guessed! \n')
        print(' '.join(display))
        return 'repeat'
    
    if guess in word:
        for indx, letter in enumerate(word):
            if letter == guess:
                display[indx] = guess
        print('Correct! V V V V \n')
        print(' '.join(display))
        guessed_lets.append(guess)
        return True
    else:
        return False
    
            
                 


def wrongguess(guess):
        if guess in wrong_lets:
            print ('Already guessed that, and its wrong.\n')
            print(' '.join(display), f" \n Wrong Guesses {wrong_lets}")
            return 'repeat2'
        else:
            print('Wrong Guess!')
            wrong_lets.append(guess)

            print(' '.join(display), f" \n Wrong Guesses {wrong_lets}")



def solved(display):
    if '_' not in display:
        return True


def Play_H():
    attempts = 6
    win = False
    while not win:
        word_guess = guess()
        if word_guess == False:
            continue
        result = correctguess(word, word_guess)
        if result == False:
            w = wrongguess(word_guess)
            if w == 'repeat2':
                print (f'\n Attempts left: {attempts}')
                continue
            elif attempts == 0:
                print (f'you lost! the word was: \n {word}')
                exit()

            else:
                attempts -= 1
                print (f'\n Attempts left: {attempts}')

        elif result == True:
            print (f'\n Attempts left: {attempts}')
        
            continue
        elif result == 'repeat':
            continue

        win = solved(display)
        if win:
            print('you win yay hip hip hooray screw you')




print ('--- Hang Man Game ---')
print ('')
Play_H()

