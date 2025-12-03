print ('bill splitter calculator. -- \n')
print ('')

while True:
    print ('Insert bill amount here:')
    try:
        bill = float(input(''))
        if bill > 0:
            print ('Eating for free?')
            continue
        break
    except ValueError:
        print ('enter the bill as a number.')
        continue
while True:
    print('')
    print ('Enter amount of people')
    
    people = (input())
    if '.' in people:
        print ('enter a whole number of people.')
        continue
    else:
        
        try:
            checker2 = int(people)
            if checker2 <= 0:
                print ('0 people? try again.')
                continue
            else:
                break
            
        except ValueError:
            print ('Enter a valid number of people.')
            continue
print ('')

split = bill / checker2

print (f'each person has to pay:{split}')

# WYM1