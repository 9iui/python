cal = 24 
unit = "hours"

def days(xx):
    if xx > 0:
         print("this is the "+str(xx)+" unit "+str(cal )+ "the unit is " + str(unit)+ " .")
    elif xx == 0:
        print("ther number which was enterd is 0 and can not be calculated")
 

def val():
    x = input("i would like you to input a number \n")
    if x == "exit":
         return "exit"
    elif x.isdigit():
         x= int(x)
         days(x)
    else:
        print("this input wasnt a number pls change it")


