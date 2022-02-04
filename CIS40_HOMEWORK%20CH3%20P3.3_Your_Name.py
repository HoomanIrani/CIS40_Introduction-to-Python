#CIS40_Chapter 3 Assignment P3.3_Houman Irani
##read an integer and print the namber of it's digits.

#obtain the number from users
number = int(input("Enter an integer:"))


#multiply -1 when the number is negatibe 
if number < 0:
    number = number * -1

#calculate and figure out the digits of the number
if number >=0 and number < 10:
    numberDigit = 1
elif number >= 10 and number < 100:
    numberDigit = 2
elif number >= 100 and number < 1e3:
    numberDigit = 3
elif number >= 1e3 and number < 1e4:
    numberDigit = 4
elif number >= 1e4 and number < 1e5:
    numberDigit = 5
elif number >= 1e5 and number < 1e6:
    numberDigit = 6
elif number >= 1e6 and number < 1e7:
    numberDigit = 7
elif number >= 1e7 and number < 1e8:
    numberDigit = 8
elif number >= 1e8 and number < 1e9:
    numberDigit = 9
elif number >= 1e9 and number < 1e10:
    numberDigit = 10
else :
    numberDigit = 11

#print result
print("The digits of the number is",numberDigit)


'''
Output1:
Enter an integer:-47529057140
The digits of the number is 11

Output2:
Enter an integer:-76587
The digits of the number is 5

Output3:
Enter an integer:878
The digits of the number is 3
'''
