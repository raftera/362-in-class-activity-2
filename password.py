import random
num = input("Enter a number for a length of a randomly generated password. ")
num1 = int(num)
password = str("Your password is: ")
for x in range (1, num1+1):
    rando = random.randint(0,9)
    password += str(rando)
print(password)