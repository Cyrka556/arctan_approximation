# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 08:45:42 2021

@author: rhydi
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 8 09:18 2019
"""
#imports
import time
import math

# function for x values who's modulus is less than 1

def dec_iteration(x,n):
    
    sign=(-1)**n
    base=(2*n)+1
    power=x**base
    function=(power*sign)/base
    return function

# function for x values who's modulus is greater than 1

def mod_iteration(x,n):
    sign=(-1)**n
    base=(2*n)+1
    power=(1/x)**base
    function=(power*sign)/base
    return function

# function for iteration loop
def dec_loop(x,N):
    ans=dec_iteration(x,0)
    for n in range(1,N):
        ans += dec_iteration(x,n)
    return ans

def pos_mod_iteration(x,N):
    ans=mod_iteration(x,0)
    for n in range(1,N):
        ans += mod_iteration(x,n)
    result=((math.pi)/2)-ans
    return result

def neg_mod_iteration(x,N):
    ans=mod_iteration(x,0)
    for n in range(1,N):
        ans += mod_iteration(x,n)
    result=-((math.pi)/2)-ans
    return result


# Selection    
MyInput = '0'
while MyInput != 'q':
    MyInput = input('Enter a choice:\na: Approximation of arctan(x)\nb: Comparison of iteration and arctan(x) from -2 to 2\nq: Exit\n\n')
    print()
    
    #Iteration of arctan
    if MyInput == 'a':
        print('You have chosen part a')
        print()
        y=2
        while y<3:
            print('This will estimate a value for arctan(x), input an x value\r\nand how many iterations (N value) you would like')
            print()
            x=float(input("Input your x value: "))
            N=int(input("Input the quantity of iterations: "))
            print()
            if N<0:
                print("No value can be determined")
                pass
            elif x>1:
                print("arctan of",x,"for",N,"interations is:",pos_mod_iteration(x,N))
            elif x<-1:
                print("arctan of",x,"for",N,"interations is:",neg_mod_iteration(x,N))
            else:
                print("arctan of",x,"for",N,"interations is:",dec_loop(x,N))
            print()
            response=input("Press\ne to approximate a new value\ns to go to main menu\n")
            if response=='e':
                print()
                pass
            else:
                print()
                break
    
    #comparison of arctan and iternatrion

    elif MyInput == 'b':
        #  creating loop to redo option b
        v=2
        while v<3:
            print('You have chosen part b')
            print()
            print('This will calculate approximations and compare them to the actual\nvalue for x between -2 and 2')
            print()
            #
            # put your code for part (d) here
            #
            N=int(input('Input how many iterations: '))
            print()
            if N<0:
                print('No values can be determined')
                print()
                pass
            
            else:
                comp=[[-2, math.atan(-2), neg_mod_iteration(-2,N), abs(math.atan(-2)-neg_mod_iteration(-2,N))],
                      [-1.75, math.atan(-1.75), neg_mod_iteration(-1.75,N), abs(math.atan(-1.75)-neg_mod_iteration(-1.75,N))],
                      [-1.5, math.atan(-1.5), neg_mod_iteration(-1.5,N), abs(math.atan(-1.5)-neg_mod_iteration(-1.5,N))],
                      [-1.25, math.atan(-1.25), neg_mod_iteration(-1.25,N), abs(math.atan(-1.25)-neg_mod_iteration(-1.25,N))],
                      [-1, math.atan(-1), dec_loop(-1,N), abs(math.atan(-1)-dec_loop(-1,N))],
                      [-0.75, math.atan(-0.75), dec_loop(-0.75,N), abs(math.atan(-0.75)-dec_loop(-0.75,N))],
                      [-0.5, math.atan(-0.5), dec_loop(-0.5,N), abs(math.atan(-0.5)-dec_loop(-0.5,N))],
                      [-0.25, math.atan(-0.25), dec_loop(-0.25,N), abs(math.atan(-0.25)-dec_loop(-0.25,N))],
                      [0, math.atan(0), dec_loop(0,N), abs(math.atan(0)-dec_loop(0,N))],
                      [0.25, math.atan(0.25), dec_loop(0.25,N), abs(math.atan(0.25)-dec_loop(0.25,N))],
                      [0.5, math.atan(0.5), dec_loop(0.5,N), abs(math.atan(0.5)-dec_loop(0.5,N))],
                      [0.75, math.atan(0.75), dec_loop(0.75,N), abs(math.atan(0.75)-dec_loop(0.75,N))],
                      [1, math.atan(1), dec_loop(1,N), abs(math.atan(1)-dec_loop(1,N))],
                      [1.25, math.atan(1.25), pos_mod_iteration(1.25,N), abs(math.atan(1.25)-pos_mod_iteration(1.25,N))],
                      [1.5, math.atan(1.5), pos_mod_iteration(1.5,N), abs(math.atan(1.5)-pos_mod_iteration(1.5,N))],
                      [1.75, math.atan(1.75), pos_mod_iteration(1.75,N), abs(math.atan(1.75)-pos_mod_iteration(1.75,N))],
                      [2, math.atan(2), pos_mod_iteration(2,N), abs(math.atan(2)-pos_mod_iteration(2,N))],]



                print()
                print('╔═════════╦═════════════════════════╦══════════════════════════╦══════════════════════════╗')
                print('║    x    ║        arctan(x)        ║       Approximated       ║        Difference        ║')
                print('╠═════════╬═════════════════════════╬══════════════════════════╬══════════════════════════╣')

                #  ,item[2]," "*(3-len(str(item[2]))),'║',item[3],"  "*(6-len(str(item[3]))),'║'

                for item in comp:
                    print('║',item[0]," "*(6-len(str(item[0]))),'║',item[1]," "*(22-len(str(item[1]))),"║",item[2]," "*(23-len(str(item[2]))),"║",item[3]," "*(23-len(str(item[3]))),"║")
                    print('╠─────────╬─────────────────────────╬──────────────────────────╬──────────────────────────╣')
                print('╚═════════╩═════════════════════════╩══════════════════════════╩══════════════════════════╝')


            response=input("Press\ne to compare a different number of iterations\ns to return to main menu\n")
            if response=='e':
                print()
                pass
            else:
                print()
                break
        

    elif MyInput != 'q':
        print('This is not a valid choice')

print('This program will self-destruct in 5 seconds')
for i in range(5):
    print(5-i)
    time.sleep(1)
print('BANG!')
