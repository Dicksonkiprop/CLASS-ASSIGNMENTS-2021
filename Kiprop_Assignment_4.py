# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 18:26:06 2021

@author: kiprop
"""

price=float(input("Enter the house price"))
downPayment =()
CreditStatus=()
CreditScore=int(input("CreditScore"))
first_name = input("Enter the first name")
last_name = input("Enter the last name")
fullnames = first_name + " " + last_name
email = input("Enter the email address")
phone = input("Enter the phone number")
mailing = input("Enter the Physical address")
city = input("Enter the City")
state=input("Enter the State")
zipcode = input("Enter the zip code")
if 780 <= CreditScore <=850:
        downPayment = (0.0 * price)
        CreditStatus= ("Exellent Credit")
        #print ("Zero Down Payment")        
elif 740 <= CreditScore <=779:
        downPayment = (0.2 * price)
        CreditStatus=("Very Good Credit")       
elif 720 <= CreditScore <=739:
        downPayment = (0.3 * price)
        CreditStatus= ("Above Average Credit")       
elif 680 <= CreditScore <=719:
        downPayment = (0.6 * price)
        CreditStatus= ("Average Credit")       
elif 620 <= CreditScore <=679:
        downPayment = (0.18 * price)
        CreditStatus= ("Below Average Credit")       
elif 580 <= CreditScore <=619:
        downPayment = (0.2 * price)
        CreditStatus= ("Poor Credit Score")       
elif  CreditScore <580:
        downPayment = (0.25 * price)
        CreditStatus= ("Poor Credit Score")        
else:
    print("Out of Range")
print()
print("Name:",fullnames)
print("Physical Address:",mailing)
print("City:",city +"","State:",state,"zipcode:",zipcode)
print()
print("New House Price:",price)
print ("Down Payment:",round(downPayment,2))
print("Credit Score:",CreditScore)
print("Credit Status:", CreditStatus) 
print()
print("CONGRATULATIONS - YOU NOW OWN YOUR DREAM HOME -",fullnames)


