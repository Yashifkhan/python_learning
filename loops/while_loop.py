# revers a number 
# n=int(input("Enter yor number : "))

# rev=0
# while n >0:
#    rev=rev*10 +n%10
#    n=n//10
# print(rev) 


# accept the number and check it is the palindorm or not 

# n=int(input("Enter yor number : "))

# temp=n
# rev=0
# while n>0:
#     rev =rev*10 +n%10
#     n=n//10
# print('rev: ', rev)
# if rev == temp:
#     print("number is palindrom")
# else:
    # print("number is not palindrom ") 
    
    
# create a game of gussing number and user number are same then win dthe game  
import random

num=random.randint(1,11)
print(num)

while True:
    guess = int(input("Enter your guess: "))
    print("guess:", guess)

    if guess == num:
        print("You win the game, numbers are same")
        break
    elif guess > num:
        print("You guessed a bigger number")
    else:
        print("You guessed a smaller number")
    
    