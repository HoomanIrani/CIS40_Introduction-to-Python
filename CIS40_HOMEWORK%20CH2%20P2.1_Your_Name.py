#CIS40_Chapter 2 Assignment P2.1_Houman Irani
#convertting the dimensions of the letter-size(8.5 * 11 inch) to millimeters

PER_INCH_TO_MM = 25.4 #Per inch equal to 24.5 mm
widthInch = 8.5 # the width in inch
lengthInch = 11 # the length in inch
widthMm = round(widthInch * PER_INCH_TO_MM,2) #conversion from inch to mm
lengthMm = round(lengthInch * PER_INCH_TO_MM,2) #conversion from inch to mm
print("The dimensions of the letter-size (8.5*11 inch) sheet" #print result
      + " of paper in millimeters \nis " + str(widthMm) + "*" + str(lengthMm)
      + "mm")

'''
Output:
The dimensions of the letter-size (8.5*11 inch) sheet of paper in millimeters 
is 215.9*279.4mm
'''
