print ('Weather Converter')
print ('instructions:\n Enter the temprature in numbers')
Unit =input('what would you like to calculate? Celsius, or fahrenheit?').strip().upper() 
if Unit == 'CELSIUS' or Unit == 'C':
    F = float(input('enter the weather in Fahrenhite!'))
    C = (F - 32) / 1.8
    print (f"The temprature in celsius is {C} Celsius")
    if F>=86:
        print ('isnt it hot outside?')
    elif F<=50:
        print ('better stay warm')
elif Unit == 'FAHRENHITE' or Unit == 'F':
    Celsius = float(input('enter the weather today in Celsius!'))
    temp_F = Celsius * 1.8 + 32 
    print (f"The temprature in fahrenheit is {temp_F} Fahrenheit")
    if Celsius>=30: 
        print ('isnt it hot outside?')
    elif Celsius<=10:
        print ('better stay warm') 
else:
    print ('invalid input. follow the intrustions.')

  # WYM1