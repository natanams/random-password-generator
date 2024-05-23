import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = random.choice(string.ascii_uppercase) 
    password = password +''.join(random.choice(characters) for _ in range(length - 1))
    return password
password_length = int(input("Enter the password Length: "))
random_password = generate_password(password_length)
print("Random Password:", random_password)