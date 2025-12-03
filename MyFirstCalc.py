print ('calculator \n Choose an operator, and enter two numbers. ')
while True:
    operator = input('pick an operator ( +, -, *, /) or "quit" to exit').strip() 
    
    
    if operator == 'quit':
         print ('ending calculator session.')
         break
    
    if operator not in ["+", "-", "*", "/" ]:
            print(f"{operator} is not a valid operator. Please try again")
            continue
    
    try:
        value1 = float(input('pick a number')) 
        value2 = float(input('pick another number'))
    except ValueError:
        print ('Error. Pick a number.')
        continue


    if operator == '+':
            print (f"{value1} + {value2} = {value1 + value2}")
    elif operator == '-':
            print (f"{value1} - {value2} = {value1 - value2}")
    elif operator == '*':
            print (f"{value1} * {value2} = {value1 * value2}")
    elif operator == '/':
            if value2 == 0:
                print ('error, cant divide by zero. please retry')
                continue
            else:
                result = value1 / value2
            if result % 1 == 0:
                ask = input('would you like that as a whole number? (yes/no)').lower()
                if ask == 'yes':
                    print (f"{value1} //  {value2} = {value1 // value2}")
                elif ask == 'no':
                    print (f"{value1} / {value2} = {value1 / value2}")
            else: 
                    print(f"{value1} / {value2} = {result}")
        


        


# WYM1