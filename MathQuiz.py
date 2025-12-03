import random 
import operator 



operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    

}
attempts = 1
while True:
    try:
        ask = int(input('pick difficulty: (1, 2, 3)'))
        if ask in [1, 2 , 3]:
            break
    except ValueError:
        print ('invalid input. enter a number from the choices!')
        continue

levelmap = {
    1: 1,
    2: 4,
    3: 6
}
score = 0
level = levelmap.get(ask, 1)

while True:
    c = random.choice(list(operators.keys()))
    a = random.randint(1,9) * level
    b = random.randint(1,9) * level

    opfunc = operators[c]
    answer = round(opfunc(a,b))
    try:
        question = int(input(f" what is {a} {c} {b}?\n"))   
    except ValueError:
        print ('enter valid number.')
        continue 
    
    if question == answer:
        score += 1
        print (f'correct \nscore:{score}')

    else: 
        ask = input(f'incorrect! You Lose!! correct answer was: {answer}. Retry? (Yes/No)').strip().lower()
        if ask == 'yes':
            continue
        else:
            break

       # WYM1