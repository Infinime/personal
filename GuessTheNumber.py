#Infinime!Created on 271118 10:33a
import random
from random import randint as ri
print("You are to guess the number generated randomly by the program. The number is between 0 and 100. Good Luck!")
again="Y"
while again=="Y":
    tried=[]
    secNum=ri(0,100)
    finished=False
    while finished==False:
        print("Guess the number")
        ans=int(input())
        if not ans in tried:
            tried.append(ans)
        if ans==secNum:
            print("Correct!!! Excellent Guessing...")
            print('You got it after ',len(tried),' different tries.')
            finished=True
        elif ans>secNum:
            print("Too Big!!!")
            finished=False
        elif ans<secNum:
            print("Too small!")
            finished=False
    print("Again?(Y/N)")
    again=input().upper()
