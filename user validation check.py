import random
import string
def user_details():
    first_name=input('Enter your first name here:')
    last_name=input('Enter your last name here:')
    email=input('Enter your email:')
    user_list= [first_name,last_name,email]
    return user_list
container=[]

def password_generator(user_list):
    length=5
    chars=string.ascii_lowercase
    password_generated=''.join(random.choice(chars)for i in range(length))
    password=str(user_list[0][0:2]+user_list[1][-2:] + password_generated)
    return password

check=True
while check:
    user_list=user_details()
    password=password_generator(user_list)
    print('Your password is'+ str(password))
    password_is_okay=input('Enter Yes if you like the password,if no enter no:')
    password_main=True
    while password_main:
        if password_is_okay=='Yes':
            user_list.append(password)
            password_main=False
            
        else:
            your_password=input('Enter a password  longer than or equal to 7 characters')
            password_length=True
            while password_length:
                if (len(your_password)) >6:
                    user_list.append(your_password)
                    password_length=False
                    password_main=False  
                else:
                    print('Your password is not up to 7 characters or more')
                    your_password=input('Enter a password  longer than or equal to 7 characters')
                    password_main=False
    container.append(user_list)
    user_list=[]
                    
    hng_employee=input('Enter another detail? If Yes, type Yes, if no then type No:')
    if hng_employee=='No':
        check=False
        
    else:
        check=True
    for user in container:
        print(user)
    