#function
def menu():
    print ("1) sum")
    print ("2) subtract")
    print ("3) multiply")
    print ("4) divide")

#call the function
menu ()

#read the input  of the keyboard
opt = input("select an option")

#try to continue with the calculator application
num1 = float(input("please enter a number"))
num2 = float(input("please enter another number"))

if opt == "1":
    total = num1 + num2
    print ("the total is " + str(total))
elif opt == "2":
    total = num1 - num2
    print ("the total is " + str(total))
elif opt == "3":
    total = num1 * num2
    print ("the total is " + str(total))
elif opt == "4":
    if num2 == 0:
        print("you cannot divide by zero")
    else:
        total = num1 / num2
        print ("the total is " + str(total))
else:
    print("that is not a valid option")