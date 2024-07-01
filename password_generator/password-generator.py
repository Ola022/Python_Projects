import string
import random
from csv import writer

""" TO GENNERATE CSV File
head = ["Platform", "Password"]
with open("pass.csv", "w") as f:
    writer_data = writer(f)
    writer_data.writerow(head)
"""


def pass_gen():
    # Get all letters, digit, and symbols
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    # Enter the platform name
    platform = input("Enter the platform: \n")

    # Accept the expected length
    pass_length = int(input("Enter the length of the password: \n"))

    # Extend and combine the list to S
    characters = []
    characters.extend(list(s1))
    characters.extend(list(s2))
    characters.extend(list(s3))
    characters.extend(list(s4))

    # Shuffle the character
    random.shuffle(characters)
    password = (''.join(characters[0:pass_length]))
    print(password)

    pass_data = [platform, password]
    with open("pass.csv", "a") as f:
        writer_data = writer(f)
        writer_data.writerow(pass_data)


pass_gen()
