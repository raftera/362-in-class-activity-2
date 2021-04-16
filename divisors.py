num = input("Enter a number to find its divisors. This will include 1 and the number itself. ")
numi = int(num)

for x in range(1, numi+1):
    if numi % x == 0:
        print(str(x) + " ")