#CIS40_Chapter 7 Assignment P7.2__Houman Irani
#write a program to read a file containing text.
## read each line and send it to the output file

        
count = 0 #total lines in reading file
count_error = 0 #error lines in reading file
flag1 = True
while flag1:
    try:
    ##Open and read a file that user enter
    ##and creat a write file which report some result below
        file = input("Enter the file name to get input:")
        file = file.strip()
        in_file = open(file,'r')
        flag1 = False
    except IOError:
        print("Can not find the file!")
flag2 = True   
while flag2:
    try:
        file = input("Enter the file name to save output:")
        file = file.strip()
        if ".txt" not in file:
            raise error
        else:
            out_file = open(file,'w')
            flag2 = False
    except:
        print("Can not find the file!")

for line in in_file:
    count += 1
    copeLine = ("/*" + str(count) + "*/ " + line)
    out_file.write(copeLine)

in_file.close()
out_file.close()
print("Copy done!")



'''
Output1(in idle):
Enter the file name to get input:hfa
Can not find the file!
Enter the file name to get input:mary.txt
Enter the file name to save output:kldaf
Can not find the file!
Enter the file name to save output:output1.txt
Copy done!

Output1(in the file):
/*1*/ Mary had a little lamb
/*2*/ Whose fleece was white as snow.
/*3*/ And everywhere that Mary went,
/*4*/ The lamb was sure to go!

'''
