import pdb


#Ex 1
'''
user_funds = 10.31
item_price = 5.30

if item_price < user_funds:
    print("You have enough money!")
if item_price == user_funds:
    print("You have the precise amount of money")
if item_price > user_funds:
    print("Sorry you don't have enough money")
'''

#Ex 2
'''
def product(n):
    total = 1
    for n in n:
        total *= n
    return total

print(product([4,4,5]))
'''

#Ex 3
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
            return True



