# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 12:10:09 2021

@author: kiprop
"""
Options=()
while Options != "Q":

    Options=input("Enter Options [P,C,F,M,KM,In,CM,Q]?")
    print("Option:",Options)
    print()
    if Options=="P":
        
        print("Options:")
        print("[P] Print Options")
        print("[C] Convert from Celcious")
        print("[F] Convert from Fahrenheit")
        print("[M] Convert from Miles")
        print("[KM] Convert from Kilometers")
        print("[In] Convert from Inches")
        print("[CM] Convert from Centimeters")
        print("[Q] Quite")
        
    elif Options == "C":
        # Convert from celsius to fahrenheit
        celsius = float(input("Celsius temperature: "))
        temp =round((celsius * 1.8) + 32,2)
        print('Fahrenheit: ' + str(temp))
        print()
    elif Options == "F":
        #convert from miles to kilometres and Kilometres to miles.
        Fahrenheit = float(input("Fahrenheit temperature:"))
        ftemp =round((Fahrenheit - 32) * 5.0/9.0,2)
        print("Celcius:"+str(ftemp))
        print()

    elif Options == "M":
        #convert miles to kilometers
        Miles = float(input("Enter Values in Miles:"))
        conv_fac = 0.621371
        miles =round((Miles * conv_fac),2)
        print('Kilometers:'+str(miles))
        print()

    elif Options == 'KM':
        kilometres = float(input('Enter the values in Kilometres:'))
        conv_fac = 1.60934
        kl =round((kilometres * conv_fac),2)
        print('Miles:' + str(kl))
        print()

    elif Options == "In":
        inches = float(input('Enter the values of inches:'))
        inch =round((inches * 2.54),2)
        print('Centimetres:'+ str(inch))
        print()

    elif Options == "CM":
        centimetres =float(input('Enter the values of Centimetres'))
        cm =round((centimetres/2.54),2)
        print('Inches:'+ str(cm))
        print()

