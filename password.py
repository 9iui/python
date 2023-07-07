import random

lower ="abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols ="{}[]!@#$%&"

all = lower + upper + symbols
len = input("what is the lenth you want ")
password = "".join(random.sample(all,int(len)))

print(password)