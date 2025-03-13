#08 create a random module 01
import random
random  = random.randint(1,1000)
print(random)
#08 create a random module 02
import random
list = ["raimbow","blue","green","red","black"]
randomlist = random.choice(list)
print(randomlist)
#08 create a random module 03
import random
list = ["H","T"]
coin = random.choice(list)
guess = input("enter H/T")
if guess == list:
    print("you win")
elif guess != list:
    print("you lose")
#08 random module 04
import random
num = random.ranint(1,5)
guess = int(input("enter a number from one to 5")
if guess == num:
    print("well done")
else:
    if num < guess:
        print("your guess is to high")
    else:
        print("your guess is to low")
