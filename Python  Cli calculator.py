#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True:
 print("1.Addition")
 print("2.Subtraction")
 print("3.Multiplication")
 print("4.Division")
 print("5.Modulus")
 print("6.Exit")
 choice=int(input("Enter a number "))
 if(choice >= 1 and choice <= 6):
    print("You selected:", choice )
    if(choice==6):
     print("Exiting Calculator...Thank you for using it!")
     break    
 else: 
    print("invalid, please try again")
    continue
 num1= int(input("Enter first number"))
 num2= int(input("Enter  second number"))
 if(choice==1):
    addition = num1+num2 
    print("Addition =",addition)
 elif(choice==2):
    subtraction=num1-num2
    print("Subtraction =",subtraction)
 elif(choice==3):
     multiplication=num1*num2
     print("Multiplication =",multiplication)
 elif(choice==4):
    if(num2==0):
      print("undefined (Cannot divide by zero)")
    else:
      division=num1/num2
      print("Division =",division)
 elif(choice==5):
      if(num2==0):
       print("undefined (Cannot perform modulus by zero)")
      else:
       modulus = num1%num2
       print("Modulus =",modulus)
 else:
      print("invalid")
 select = input("Do you want to continue?(y/n):")
 if select =="n":
    print("Good bye!,Thank You")
    break
 elif(select =="y"): 
    print("Welcome")
 else:
    print("invalid statement")
    break



# In[ ]:




