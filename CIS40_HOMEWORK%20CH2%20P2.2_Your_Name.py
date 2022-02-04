#CIS40_Chapter 2 Assignment P2.2_Houman Irani
#calculating the perimeter of the letter-size(8.5 * 11 inch) sheet of
#paper and the length of its diagonal

from math import sqrt

width = 8.5 # the width of the paper in inch
length = 11 # the length of the paper in inch
perimeter = (width + length)*2 #calculate the perimeter of the paper
diagonal = sqrt(width ** 2 + length ** 2) #calculate the diagonal of the paper
print("The perimeter of the letter-size (8.5*11 inch)"
      + " sheet of paper is %5.2f"%(perimeter) + "inch\n"
      + "and the length of its diagonal is %5.2f"%(diagonal)
      + "inch")#print result
     
'''
Output:
The perimeter of the letter-size (8.5*11 inch) sheet of paper is 39.00inch
and the length of its diagonal is 13.90inch
'''
