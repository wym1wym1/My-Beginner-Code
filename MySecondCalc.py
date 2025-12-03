print ('two Digit Calculator. \n Rules: \n 1- use this formula "num1 (operator) num2"')
print ('')



def add(x, y):
    answer_add = x + y
    return answer_add

def substract(x,y):
    answer_substract = x - y
    return answer_substract

def mult(x,y):
    answer_mult = x * y 
    return answer_mult

def div(x,y):
    answer_div = x / y
    return answer_div

available_op = {
    '+': add,
    '-': substract,
    '*': mult,
    '/': div
}

while True:
    calculation = input('enter the calculation. type QUIT to exit. \n').split()


    if calculation[0].upper() == 'QUIT':
        break


    if len(calculation) != 3:
        print ('Please enter two digits.')
        continue
    
        
    operator = calculation[1]
    num1 = calculation[0]
    num2 = calculation[2]
    try:  
        if '.' in num1 or '.' in num2:
            num1 = float(num1)
            num2 = float(num2)
        else:
            num1 = int(num1)
            num2 = int(num2)
    except ValueError:
        print ('Please type in valid numbers. ')
        continue

    if operator not in available_op:
        print (f'please choose one of the available operators: {list(available_op)}')
        continue
    elif operator == '/':
        if num2 == 0:
            print ('Cant divide by zero.')
            continue
    
    chosenf = available_op[operator]
    result = chosenf(num1, num2)

    print (f'answer: {result}')

    # WYM1