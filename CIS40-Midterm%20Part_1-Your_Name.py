#CIS40_Midterm_Part 1__Houman Irani
#Write a menu-driven program for De Anza College Food Court with functions
##1.show the menu 2.get order constains from user and test if it's valid input
###3.comput the total price before and after tax
####4.print receipt for customers (student custmers is tax-free)

#list all the contents in this program
MEAL1 = 'De Anza Burger'
MEAL2 = 'Bacon Cheese'
MEAL3 = 'Mushroom Swiss'
MEAL4 = 'Western Burger'
MEAL5 = 'Don Call Burger'
PRICE1 = 5.25
PRICE2 = 5.75
PRICE3 = 5.95
PRICE4 = 5.95
PRICE5 = 5.95
TAX_RATE = 0.09

#the main function orders the whole program
##and arrange the sequence of all functions in it 
def main():
    display_menu_de_anza()
    quant1,quant2,quant3,quant4,quant5,student_test = get_input()
    total_no_tax,total_add_tax = comput_total(quant1,quant2,quant3,quant4,quant5)
    print_output(quant1,quant2,quant3,quant4,quant5,total_no_tax,total_add_tax,student_test)


#display function uses to show the menu
def display_menu_de_anza():
    print("1.%-20s $%4.2f"%(MEAL1,PRICE1))
    print("2.%-20s $%4.2f"%(MEAL2,PRICE2))
    print("3.%-20s $%4.2f"%(MEAL3,PRICE3))
    print("4.%-20s $%4.2f"%(MEAL4,PRICE4))
    print("5.%-20s $%4.2f"%(MEAL5,PRICE5))
    print("6.Exit")

   
#get input function obtains which meals are ordered and the quantities of each meal
##and to prompt user input the valid information if they typed the invalid one
##return the quantities of each meal which the user ordered
def get_input():
    burg1 = burg2 = burg3 = burg4 = burg5 =0 #initialized the quantity of each burger

    #use try-except nested in the while loop
    ##to ask which meal the user wants or finish the order processes
    flag0 = False 
    while not flag0:
        #to check if the input of meal number is integer 
        flag1 = False
        while not flag1:
            
            try:
                mealNum = input("Meal Number(type meal number 1-5 or 6 to exit):")
                mealNum = int(mealNum.strip())
                #to check if the input of the meal number is in the range 1 to 6
                ##and stop all the meal order part to continue next steps when user enter number "6"
                if mealNum > 0 and mealNum < 6:
                    #to check if the input valid or not for the quantity of the meal that the user has chosen
                    flag2 = False
                    while not flag2:
                        try:
                            burgerQuant = input("How much?")
                            burgerQuant = int(burgerQuant.strip())

                            if burgerQuant >= 0:
                                
                                flag2 = True
                            #to record the quantity of all the meals the user has chosen
                                if mealNum == 1:
                                    burg1 = burgerQuant
                                elif mealNum == 2:
                                    burg2 = burgerQuant
                                elif mealNum == 3:
                                    burg3 = burgerQuant
                                elif mealNum == 4:
                                    burg4 = burgerQuant
                                elif mealNum == 5:
                                    burg5 = burgerQuant
                            else:
                                print("Error!Enter a valid number,please!")
                            
                        except:
                            print("Error!Enter a number,please!")
                elif mealNum ==6:
                    print("Exit.")
                    flag0 = True
                    flag1 = True
                else :
                    print("Error!type in the meal number 1-5 or 6 to exit.")
            except:
                print("Error!type in the meal number 1-5 or 6 to exit.")            

    #to obtain if the costumer is students or not
    #and  prompt user if the input is not valid
    flag3 = False
    while not flag3:
        
        student_test =input("Student or not?(\"1\" for \"Yes\", \"0\" for \"No\")")
        student_test = student_test.strip()
        if student_test == "1":
            student_test = int(student_test)
            flag3 = True
        elif student_test == "0":
            student_test = int(student_test)
            flag3 = True
        else:
            print("Error!Enter \"1\"or\"0\"")
    return burg1,burg2,burg3,burg4,burg5,student_test
  

#comput function to calculate the total before and after tax
##return total_no_tax and total_add_tax
def comput_total(quant1,quant2,quant3,quant4,quant5):
    total_no_tax = PRICE1 * quant1 + PRICE2 * quant2 \
                   + PRICE3 * quant3 + PRICE4 * quant4 + PRICE5 * quant5
    tax = total_no_tax * TAX_RATE
    total_add_tax = total_no_tax + tax
    return total_no_tax,total_add_tax
    

#print the receipt inlude the item, price and quantities and total price  
def print_output(quant1,quant2,quant3,quant4,quant5,total_no_tax,total_add_tax,student_test):

    print("%25s"%"Receipt")
    print("%10s"%"Meal Name","%12s"%"Price","%15s"%"Quantity")
    print("-" * 40)
    if quant1 != 0:
        print("%-16s"%(MEAL1),"$%4.2f"%PRICE1,"%10d"%(quant1))
    if quant2 != 0:
        print("%-16s"%(MEAL2),"$%4.2f"%PRICE2,"%10d"%(quant2))
    if quant3 != 0:
        print("%-16s"%(MEAL3),"$%4.2f"%PRICE3,"%10d"%(quant3))
    if quant4 != 0:
        print("%-16s"%(MEAL4),"$%4.2f"%PRICE4,"%10d"%(quant4))
    if quant5 != 0:
        print("%-16s"%(MEAL5),"$%4.2f"%PRICE5,"%10d"%(quant5))

    print("-" * 40)
    print("Total before tax:$%5.2f"%(total_no_tax))
    
    if student_test == 1:
        total_after_tax = total_no_tax
        tax = 'None for students'
        
    else :
        total_after_tax = total_add_tax
        tax = "9.000%"
        

    print("Tax:",tax)
        
    print("Total price after tax:$%5.2f"%(total_after_tax))

    
main()



'''
Output1:
1.De Anza Burger       $5.25
2.Bacon Cheese         $5.75
3.Mushroom Swiss       $5.95
4.Western Burger       $5.95
5.Don Call Burger      $5.95
6.Exit
Meal Number(type meal number 1-5 or 6 to exit):0
Error!type in the meal number 1-5 or 6 to exit.
Meal Number(type meal number 1-5 or 6 to exit):0
Error!type in the meal number 1-5 or 6 to exit.
Meal Number(type meal number 1-5 or 6 to exit):0
Error!type in the meal number 1-5 or 6 to exit.
Meal Number(type meal number 1-5 or 6 to exit):-1
Error!type in the meal number 1-5 or 6 to exit.
Meal Number(type meal number 1-5 or 6 to exit):-1
Error!type in the meal number 1-5 or 6 to exit.
Meal Number(type meal number 1-5 or 6 to exit):-1
Error!type in the meal number 1-5 or 6 to exit.
Meal Number(type meal number 1-5 or 6 to exit):-1
Error!type in the meal number 1-5 or 6 to exit.
Meal Number(type meal number 1-5 or 6 to exit):1
How much?-1
Error!Enter a valid number,please!
How much?-1
Error!Enter a valid number,please!
How much?-1
Error!Enter a valid number,please!
How much?0
Meal Number(type meal number 1-5 or 6 to exit):6
Exit.
Student or not?("1" for "Yes", "0" for "No")-1
Error!Enter "1"or"0"
Student or not?("1" for "Yes", "0" for "No")-1
Error!Enter "1"or"0"
Student or not?("1" for "Yes", "0" for "No")-0
Error!Enter "1"or"0"
Student or not?("1" for "Yes", "0" for "No")0
                  Receipt
 Meal Name        Price        Quantity
----------------------------------------
----------------------------------------
Total before tax:$ 0.00
Tax: 9.000%
Total price after tax:$ 0.00


Output2:
1.De Anza Burger       $5.25
2.Bacon Cheese         $5.75
3.Mushroom Swiss       $5.95
4.Western Burger       $5.95
5.Don Call Burger      $5.95
6.Exit
Meal Number(type meal number 1-5 or 6 to exit):5
How much?1
Meal Number(type meal number 1-5 or 6 to exit):1
How much?2
Meal Number(type meal number 1-5 or 6 to exit):6
Exit.
Student or not?("1" for "Yes", "0" for "No")0
                  Receipt
 Meal Name        Price        Quantity
----------------------------------------
De Anza Burger   $5.25          2
Don Call Burger  $5.95          1
----------------------------------------
Total before tax:$16.45
Tax: 9.000%
Total price after tax:$17.93
'''
