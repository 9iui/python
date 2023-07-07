import os

dir = input("could you like to input a directrory you want to check")

file_list = os.listdir(dir)

for file_name in file_list:
    print(file_name)
