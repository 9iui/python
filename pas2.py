import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "{}[]!@#$%&"

all_chars = lower + upper + symbols
length = input("What is the length you want for the password? ")
try:
    length = int(length)
    if length <= 0 or length > len(all_chars):
        raise ValueError
    password = "".join(random.sample(all_chars, length))
    print(password)
except ValueError:
    print("Invalid password length. Please enter a positive integer less than or equal to {}".format(len(all_chars)))
