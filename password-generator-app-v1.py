import random
# Random password generator
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?' # List of characters

# Password length from user
password_length = int(input('Password length: '))
# Password count from user
password_count = int(input('Password count: '))
# Loop to generate password
for x in range(0, password_count):
    password = ''
    for x in range(0, password_length):
        password_char = random.choice(characters)
        password += password_char
    print('Password: ' + password)

