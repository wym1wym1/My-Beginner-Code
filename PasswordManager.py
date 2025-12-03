
def change_vaultk(ckey):
    newkey = input('Enter your new password. \n - ')
    print (f'Changed password from {ckey} to {newkey}')
    return newkey

def change_password(c_pass):
    print (list(c_pass.keys()))
    
    while True:
        
        account = input('For which account? \n- ').strip().lower()
        if account in c_pass:
            break
        else:
            print ('That account doesnt exist!')
            continue
    newpass = input('Enter your new Password. \n - ')
    c_pass[account] = newpass
    print (f'Password for {account} changed!')
    return c_pass

def view_pass(c_pass):
    print (list(c_pass.keys()))
    while True:
        account = input('For which account? \n- ')
        if account in c_pass.keys():
            break
        else:
            print ('That account doesnt exist!')
    passw = c_pass[account]
    print (f'Password for {account} is: {passw}')
    return c_pass

def add_pass(cpass):
        while True:
            account = input('For what account? \n- ')
            if account in cpass:
                print(f'{account} already exists')
            else:
                passw = input('whats the password? \n- ')
                cpass[account] = passw
            print (f'{account} added with the password {passw} ')
            print ('Add another account. or "EXIT" to quit.')
            if account.upper() == 'EXIT' or passw.upper() == 'EXIT':
                break
            return cpass



print ('Password Vault.')

password = 'ElyasM'
attempts = 0 
for i in range(1, 4):

    q1 = input('Enter Vault Key \n - ')

    if q1 != password:

        attempts += 1

        
        if attempts == 3:
            print ('Out of attempts. Exiting, Bye!')
            exit()

        else:
            print (f'Invalid Key. Try again. attempt number: {attempts}')


    elif q1 == password:
        print ('Welcome In!')
        break


PASSWORDS = {
    'twitter': 'ABC1212',
    'facebook': 'SiuOn',
    'teams': 'Wwbb23'
}

OPTIONS = ['1 - Change Vault Key',
           '2- Change Passwords',
           '3- View an accounts Password',
           '4- Add a new account'
           ]
print (f' Your accounts: {list(PASSWORDS.keys())} \n what would you like to do? (select via the number. or "EXIT" to exit.) \n {OPTIONS}')

AVCHOICES = [1, 2, 3, 4]   # <--- i am fully aware that this is an unreliable method. how ever, i just dont feel like changing a lot of things right now. 

while True:

    CHOICE = input('')

    if CHOICE.upper() == 'EXIT':
        exit()
    else:
        try:
            CHOICE = int(CHOICE)
            if CHOICE not in AVCHOICES:
                print ('That choice is unavailable')
                continue
        except ValueError:
            print ('Please choose either "EXIT" or an available choice via the number.')

    

    if CHOICE == 1:
        password = change_vaultk(password)
        print ('Password Changed!')

    elif CHOICE == 2:
        PASSWORDS = change_password(PASSWORDS)

    elif CHOICE == 3:
        view_pass(PASSWORDS)

    elif CHOICE == 4:
        PASSWORDS = add_pass(PASSWORDS)

    else:
        print ('Unavailable option.')


#3 WORK IN PROGRESS!
# WYM1