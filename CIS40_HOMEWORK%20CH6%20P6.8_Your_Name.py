#CIS40_Chapter 6 Assignment P6.8__Houman Irani
#write a program to compute the alternating sum of all elements in a list.

#define a main function to order the whole processes
def main():
    the_list = get_input()
    print('The list just enter:',the_list)
    result = alter_sum(the_list)
    print("The alternating sum of the list is",result)

#define a function that get input from user, check esch enter content
    #and stop at "s",return the list that user entered
def get_input():
    result = []
    flag=True
    while flag:
        get_input = input("Enter a number or enter \"s\" for finish:")
        try:
            get_input = int(get_input)
            result.append(get_input)
        
        except:
            if get_input == "s":
                flag =False
            else:
                print("error")
    return result

#define a comput function
##get sum of all the even position elements and the sum of all the odd position elements
###get the result that the difference when even sum minus the odd sum
###return the result


def alter_sum(in_list):
    pos_even = []
    pos_odd = []
    n = len(in_list)
    for pos in range(n):
        if pos == 0:
            pos_even.append(in_list[pos])
        elif pos % 2 == 0:
           pos_even.append(in_list[pos])
        else:
            pos_odd.append(in_list[pos])
    result = sum(pos_even)- sum(pos_odd)

    return result
main()

'''
Output1:
Enter a number or enter "s" for finish:1
Enter a number or enter "s" for finish:4
Enter a number or enter "s" for finish:9
Enter a number or enter "s" for finish:16
Enter a number or enter "s" for finish:
error
Enter a number or enter "s" for finish:9
Enter a number or enter "s" for finish:7
Enter a number or enter "s" for finish:4
Enter a number or enter "s" for finish:9
Enter a number or enter "s" for finish:11
Enter a number or enter "s" for finish:s
The list just enter: [1, 4, 9, 16, 9, 7, 4, 9, 11]
The alternating sum of the list is -2


Output2:
Enter a number or enter "s" for finish:1
Enter a number or enter "s" for finish:2
Enter a number or enter "s" for finish:3
Enter a number or enter "s" for finish:s
The list just enter: [1, 2, 3]
The alternating sum of the list is 2
'''
