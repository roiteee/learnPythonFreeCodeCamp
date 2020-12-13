#Single line comment
#Use # to comment out everything after it
'''Multiline comment
no need to # everytime
'''

#try except

#number = int(input("Enter an integer"))
#print(number)       #everything works if user enters integer otherwise breaks the program

try:
    number2 = int(input("Enter an integer"))
    print(number2)
except ZeroDivisionError:
    print("Divided by 0")
except ValueError as err:
    #print("Invalid input")
    print(err)
