import random


upperlimit = 100
lowerlimit = 1


number = random.randint(lowerlimit,upperlimit)
flag = False


while(flag == False):
    guess = int(input("Enter number: "))

    if guess > upperlimit:
        print("Number must be equal or lower than", upperlimit)
    elif guess < lowerlimit:
        print("Number must be equal or higher than", lowerlimit)

    if guess > number:
        print("Mystery number is lower than input")
    elif guess < number:
        print("Mystery number is higher than input")

    if guess == number:
        flag = True 
        print("Congrats you are correct")
