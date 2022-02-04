#CIS40_Chapter 5 Assignment P5.7__Houman Irani
#write a function that flipping randomly two characters except the first and the last
##when the length of the word is bigger than 3
###and return it

#import randient
from random import randint

def scramble(word):
    word_length = len(word)#obtain word length to figure out if it needs flip

    #randomly choosing a character expect the first one and the last two
    ##and flipping the character and the followed one with lists fucntion
    ###if the length is bigger than 3
    ####then rewrite the whole word and return it
    if word_length > 3:
        the_list = list(word)
        index_num = randint(1,word_length - 3)
        the_list[index_num],the_list[index_num + 1] = the_list[index_num + 1],the_list[index_num]
        new_word = word[0]
        for i in the_list[1:len(word)+1]:
            new_word += i

        return new_word
    elif word_length <= 3:
        return word
c = input("WORD:")
print(scramble(c))




 
'''
Output1:
WORD:function
fucntion

Output2:
WORD:way
way

Output3:
WORD:that
taht
'''

