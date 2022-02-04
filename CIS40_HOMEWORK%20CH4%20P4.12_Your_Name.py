#CIS40_Chapter 4 Assignment P4.12_Houman Irani
##read a word and prints all substrings 

#obtain the word from user
word = input("Enter the word:")

#calculate the length of the word
n = len(word)

#print the substrings of the word
for i in range(1, n + 1):
    for j in range(0, n - i + 1):
        print(word[j:j + i])


'''
Output1:
Enter the word:rum
r
u
m
ru
um
rum

output2:
Enter the word:apple
a
p
p
l
e
ap
pp
pl
le
app
ppl
ple
appl
pple
apple
'''
