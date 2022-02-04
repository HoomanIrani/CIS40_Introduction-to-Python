#CIS40_Final_Part 1__Houman Irani
#Write a menu-driven program for De Anza College Food Court with functions
##1.show the menu 2.get order constains from user and test if it's valid input
###3.comput the total price before and after tax
####4.print receipt for customers (student custmers is tax-free)

import time
import datetime


class DeAnzaBurger:
    '''
    This is a class for De Anza college to order five kinds of burgers,then, print and save it to a current time file
    '''
    _TAXRATE = 0.09
    _STUDENTTAXRATE = 0
    
    def __init__(self):
        '''
        initialization all instance variable
        '''
        self.priceDict = {'De Anza Burger':5.25,'Bacon Cheese':5.75,'Mushroom Swiss':5.95,'Western Burger':5.95,'Don Call Burger':5.95}
        self.orderDict={'De Anza Burger':0,'Bacon Cheese':0,'Mushroom Swiss':0,'Western Burger':0,'Don Call Burger':0}
        self._priceBeforeTax = 0
        self._priceAfterTax = 0
        self.student_test = ''
                
    def main(self):
        self.displayMenu()
        self.getInput()
        self.computTotal()
        self.printOutputAndSaveToAFile()
    
    def displayMenu(self):
        '''
        show all five burgers and the price of them
        '''
        print("1.%-20s $%4.2f"%('De Anza Burger',self.priceDict['De Anza Burger']))
        print("2.%-20s $%4.2f"%('Bacon Cheese',self.priceDict['Bacon Cheese']))
        print("3.%-20s $%4.2f"%('Mushroom Swiss',self.priceDict['Mushroom Swiss']))
        print("4.%-20s $%4.2f"%('Western Burger',self.priceDict['Western Burger']))
        print("5.%-20s $%4.2f"%('Don Call Burger',self.priceDict['Don Call Burger']))
        print("6.Exit")
        
    def getInput(self):
        '''
        use try-except nested in the while loop
        to ask which meal the user wants or finish the order processes
        '''
        flag0 = False 
        while not flag0:            
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
                                burgerQuant = input("How many?")
                                burgerQuant = int(burgerQuant.strip())
                                if burgerQuant >= 0:
                                    flag2 = True
                                    #to record the quantity of all the meals the user has chosen
                                    if mealNum == 1: self.orderDict['De Anza Burger'] = burgerQuant
                                    elif mealNum == 2: self.orderDict['Bacon Cheese'] = burgerQuant
                                    elif mealNum == 3: self.orderDict['Mushroom Swiss'] = burgerQuant
                                    elif mealNum == 4: self.orderDict['Western Burger'] = burgerQuant
                                    elif mealNum == 5: self.orderDict['Don Call Burger'] = burgerQuant
                                else: print("Error!Enter a valid number,please!")                            
                            except: print("Error!Enter a number,please!")
                    elif mealNum ==6:
                        print("Exit.")
                        flag0 = True
                        flag1 = True
                    else : print("Error!type in the meal number 1-5 or 6 to exit.")
                except: print("Error!type in the meal number 1-5 or 6 to exit.")            

        #to obtain if the costumer is students or not
        #and  prompt user if the input is not valid
        flag3 = False
        while not flag3:
            self.student_test = input("Student or not?(\"1\" for \"Yes\", \"0\" for \"No\")")
            self.student_test = self.student_test.strip()
            if self.student_test == "1": flag3 = True
            elif self.student_test == "0": flag3 = True
            else: print("Error!Enter \"1\"or\"0\"")
    
    def computTotal(self):
        '''
        comput function to calculate the total before and after tax
        update self._priceBeforeTax,self._priceAfterTax
        '''
        for key in self.orderDict:
            self._priceBeforeTax += self.priceDict[key] * self.orderDict[key]
        self._priceAfterTax = self._priceBeforeTax + self._priceBeforeTax * self._TAXRATE
    

    def printOutputAndSaveToAFile(self):
        '''
        print the receipt inlude the item, price and quantities and total price
        and save the receipt into a current time file
        '''
        timeStamp = time.time()
        orderTimeStamp = datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H-%M-%S') 
        orderTimeStamp = orderTimeStamp + '.txt'
        fileOfTheBill = open(orderTimeStamp,'w')

        title = ("%25s"%"Receipt\n")
        print(title)
        fileOfTheBill.write(title)

        headLine = str("%10s"%"Meal Name"+"%12s"%"Price"+"%15s"%"Quantity\n")
        print(headLine)
        fileOfTheBill.write(headLine)

        divideLine = ("-" * 40 + "\n")
        print(divideLine)
        fileOfTheBill.write(divideLine)

        for key in self.orderDict:
            if self.orderDict[key] != 0:
                burgerOutput = str("%-16s"%(key) + "$%4.2f"%(self.priceDict[key]) + "%10d"%(self.orderDict[key]) + "\n")
                print(burgerOutput)
                fileOfTheBill.write(burgerOutput)
      
        divideLine = ("-" * 40 + "\n")
        print(divideLine)
        fileOfTheBill.write(divideLine)

        beforeTaxOutput = str("Total before tax:$%5.2f"%(self._priceBeforeTax) + "\n")
        print(beforeTaxOutput)
        fileOfTheBill.write(beforeTaxOutput)
    
        if self.student_test == '1':
            taxLine = str("Tax:%5.2f"%(self._STUDENTTAXRATE) + "%\n")
            totalLine = str("Total price after tax:$%5.2f"%(self._priceBeforeTax) + "\n")
        
        else :
            taxLine = str("Tax:%5.2f"%(self._TAXRATE) + "%\n")            
            totalLine = str("Total price after tax:$%5.2f"%(self._priceAfterTax) + "\n")
            
        print(taxLine)
        fileOfTheBill.write(taxLine)
        print(totalLine)
        fileOfTheBill.write(totalLine)
        fileOfTheBill.close()

theOrder = DeAnzaBurger()
theOrder.main()




'''
Output1 (in the IDLE):
1.De Anza Burger       $5.25
2.Bacon Cheese         $5.75
3.Mushroom Swiss       $5.95
4.Western Burger       $5.95
5.Don Call Burger      $5.95
6.Exit
Meal Number(type meal number 1-5 or 6 to exit):2
How many?1
Meal Number(type meal number 1-5 or 6 to exit):fds
Error!type in the meal number 1-5 or 6 to exit.
Meal Number(type meal number 1-5 or 6 to exit):4
How many?dsf
Error!Enter a number,please!
How many?2
Meal Number(type meal number 1-5 or 6 to exit):-0
Error!type in the meal number 1-5 or 6 to exit.
Meal Number(type meal number 1-5 or 6 to exit):0
Error!type in the meal number 1-5 or 6 to exit.
Meal Number(type meal number 1-5 or 6 to exit):6
Exit.
Student or not?("1" for "Yes", "0" for "No")1
                 Receipt

 Meal Name       Price      Quantity

----------------------------------------

Bacon Cheese    $5.75         1

Western Burger  $5.95         2

----------------------------------------

Total before tax:$17.65

Tax: 0.00%

Total price after tax:$17.65






Output1 (in the file):
                 Receipt
 Meal Name       Price      Quantity
----------------------------------------
Bacon Cheese    $5.75         1
Western Burger  $5.95         2
----------------------------------------
Total before tax:$17.65
Tax: 0.00%
Total price after tax:$17.65




Output2 (in the Idle):
1.De Anza Burger       $5.25
2.Bacon Cheese         $5.75
3.Mushroom Swiss       $5.95
4.Western Burger       $5.95
5.Don Call Burger      $5.95
6.Exit
Meal Number(type meal number 1-5 or 6 to exit):1
How many?2
Meal Number(type meal number 1-5 or 6 to exit):3
How many?1
Meal Number(type meal number 1-5 or 6 to exit):6
Exit.
Student or not?("1" for "Yes", "0" for "No")0
                 Receipt

 Meal Name       Price      Quantity

----------------------------------------

De Anza Burger  $5.25         2

Mushroom Swiss  $5.95         1

----------------------------------------

Total before tax:$16.45

Tax: 0.09%

Total price after tax:$17.93





Output2(in the file):
                 Receipt
 Meal Name       Price      Quantity
----------------------------------------
De Anza Burger  $5.25         2
Mushroom Swiss  $5.95         1
----------------------------------------
Total before tax:$16.45
Tax: 0.09%
Total price after tax:$17.93
'''
