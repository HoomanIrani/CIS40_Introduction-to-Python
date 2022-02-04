#CIS40_Chapter 5 Assignment P5.7_Houman Irani
#write a function that count the number of words that content in the string
#and return it

def countWords(string):
    words = string.split()
    wordNum = len(words)
    return wordNum

get_input = input("Enter the string:")
print(countWords(get_input))


 
'''
Output1:
Enter the string:Mary had a little lamb
5

Output2:
Enter the string:This is a string
4
'''

