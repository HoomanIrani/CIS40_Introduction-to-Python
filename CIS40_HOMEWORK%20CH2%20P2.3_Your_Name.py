#CIS40_Chapter 2 Assignment P2.3_Houman Irani
#calculating the variable 'num' and
#displaying the square, cube, and fourth power

num = 88 #assign 88 to variable 'num'

squarNum = int(num * num) #calculate the square power of the variable 'num'
cubeNum = int(num * num * num)#calculate the cube power of the variable 'num'
forthNum = int(num**4) #calculate the fourth power of the variable 'num' 

print("The square, cube, and fourth power of the number "
      + str(num) + "\nare " + str(squarNum) + ", "
      + str(cubeNum) + ", " + str(forthNum) + ".") #print result


     
'''
Output:
The square, cube, and fourth power of the number 88
are 7744, 681472, 59969536.
'''
