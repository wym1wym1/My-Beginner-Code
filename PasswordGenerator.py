import random


print ('Password generator')

letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

numbers = ['0','1','2','3','4','5','6','7','8','9']

weights = [1]*len(letters) + [2.5]*len(numbers)

def password_generator(x):  
    password = ''
    for i in range(x):
        choices = letters + numbers
        rchar = random.choices(choices, weights=(weights), k=1 )[0]
        if rchar.isalpha() and random.choice([True, False]):
            rchar = rchar.upper()
        password += rchar
    return password

while True:
    ask = (input('choose the length of ur password (maximum is 10) or "quit" to.. well quit. \n - ')).lower()

    if ask == 'quit':
        print ('\n okay, exiting.')
        break
    try:
        ask = int(ask)
    except ValueError:
        print ('either type quit or a number between 1 to 10. my god')
        continue
    if ask > 10:
        print('Error. Max is 10. i will make it 10 anyway.')
        ask = 10

    print (password_generator(ask))
    
 

 # WYM1