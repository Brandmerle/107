print ("hello world!")

#variables
name = "brandon"
last_name= "merle"
age = 1
found = False
print (name)

#if / statement
if age < 100:
    print ("no worries, you're not that old")
    print("I am using the indentation")
elif age == 100: #else if statement
    print("wow you are a century")
else:
    print("It seems that you are really old")

#functions
def sayHello():
    print("hello world!")

def sayGoodbye(name):
    print("bye " + str(name)) #str converts to string

# call functions
sayHello()
sayGoodbye("brandon")

#arrays are called lists in python - logic remains the same with pos 0,1,2,3
color = ["red", "green", "blue", "yellow"]
print (color)

#add an element to the "list" created above
color.append ("pink")
print (color)
print (color [0]) #prints color in the "0" position in the list
color.remove("yellow")
print (color)

#for loop 
for col in color:
    print (col)
    #if in javascript it this would be: for(let i=0; limit>0;i++)
    #let temp = color [i]
    #print temp

#dictionaries - easier to handle because you dont need to remember the positon, just the key (ex: "last_name")
me ={
    "name": "brandon",
    "last_name": "merle",
    "age": 41
}
print(me)
print(me["last_name"])
me["last_name"] = "Doe" #change a key attribute on the list
print(me)
me["color"]= "blue" #add a new key to the list
print (me)

ages = [32, 74, 20, 69, 52, 26, 31, 77, 43, 73, 51, 57, 19, 79, 40, 34, 27, 23, 21, 44, 53, 55, 24, 36, 41, 47, 78, 46, 68, 75, 49, 83, 61, 60, 29, 56, 67, 17, 70, 81, 87, 38]
#print the sum of all of the numbers
def example1():
    total = 0
    for age in ages:
        total=total + age
    print (total)
#call the functions
example1()

#count how many users are equal or older than 21
def example2():
    counter = 0
    for age in ages:
        if age >= 21:
            counter +=1
    print (counter)
example2()

#how many users are between 30 and 40 yrs old
def example3():
    counter = 0
    for age in ages:
        if age >=30 and age <=40:
            counter +=1
    print ("There are " + str(counter) + " users between 30 and 40")
example3()