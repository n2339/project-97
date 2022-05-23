import random
number = random.randint(1,9)

chances= 0
while chances < 5:
 question = int (input('enter a number between one and nine'))
 if question == number : 
    print('you won, congrats')
 elif question < number :
     print ('guess a higher number')
 elif question> number :
     print ('guess a lower number')
 chances = chances  + 1

if not chances < 5 :
    print('you lose. the number is',number)