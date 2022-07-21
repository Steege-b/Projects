import string, random

upper = list(string.ascii_uppercase)
lower = list(string.ascii_lowercase)
numbers = list(string.digits)
special = list("<>?/\;!@#$%^&*")
length = int(input('Enter length (min 12):'))
def PWGenerator(length):
    password = []
    for x in range(2):
        password.append(random.choice(upper))
        password.append(random.choice(lower))
    for x in range(4):
        password.append(random.choice(numbers))
        password.append(random.choice(special))
    remainder = length - 12
    if remainder < 0:
        print('Password too short, defaulting to 12 characters.')
    for x in range(remainder):
        password.append(random.choice(upper + lower +special + numbers))
    random.shuffle(password)
    print("".join(password))

PWGenerator(length)