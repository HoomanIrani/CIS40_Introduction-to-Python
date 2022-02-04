#CIS40_Chapter 4 Assignment P4.9_Houman Irani
##read a word and prints the word in reverse

#obtain the word from user
word = input("Enter the word:")

#calculate the length of the word
n = len(word)

#reverse the word and print it out
for i in range(n-1,-1,-1):
    print(word[i],end="")



'''
Output1:
Enter the word:Harry
yrraH

output2:
Enter the word:apple
elppa
'''
