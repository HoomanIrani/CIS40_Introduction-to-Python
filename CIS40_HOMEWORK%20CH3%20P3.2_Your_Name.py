#CIS40_Chapter 3 Assignment P3.2_Houman Irani
#Obain a floating-point number from user
##figure out whether it's positive/negative/zero
###if the absolute value is less than 1,print"small"
####if the absolute value is greater than 1000000,print"large"

#constants in the program
ZERO = 0
SMALL_POINT = 1
LARGE_POINT = 1E6



#Obtain a test number from user as a floating-point number
number = float(input("Enter a number(floating-point number):"))

#figure out which the input number belongs to 
if number == ZERO:
    print("Zero")
elif number > ZERO:
    print("Positive")
else :
    print("Negative")


#testing the absolute number large or small
numberAbs = abs(number)

if numberAbs < SMALL_POINT and numberAbs > ZERO:
    print("Small")
elif numberAbs > LARGE_POINT:
    print("Large")

'''
Output1:
Enter a number(floating-point number):0
Zero


Output2:
Enter a number(floating-point number):3241113414
Positive
Large


Output3:
Enter a number(floating-point number):-0.4343
Negative
Small
'''
