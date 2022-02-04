#CIS40_Chapter 3 Assignment P3.1_Houman Irani
#read a integer from user
##figure out whether it is negative/zero/positive

#constant in the program
ZERO = 0


#Obtain a test number from user as an integer
number = int(input("Enter the test integer:"))

#figure out which the input number belongs to 
if number == ZERO:
    print("Zero")
elif number > ZERO:
    print("Positive")
else :
    print("Negative")



'''
Output1:
Enter the test integer:5
Positive


Output2:
Enter the test integer:-4
Negative

Output3:
Enter the test integer:0
Zero
'''
