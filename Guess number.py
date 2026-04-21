import random
num=random.randint(1,10)
guess=0

while(guess!=num):
    
    guess=int(input("Enter you guess number(!-10):"))
    
    if(guess<num):
        print("too low")
        
    elif(guess>num):
        print("too high")
        
    else:
        print("correct machan")
