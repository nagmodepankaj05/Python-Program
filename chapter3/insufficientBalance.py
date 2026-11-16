class InsufficientBalance(Exception):
    pass

try : 
    amount = 10000
    withdraw = int(input("Enter amount to withdraw : "))
    if withdraw > amount :
        raise InsufficientBalance("Insufficient Amount balance : ", amount)
    else:
        print(withdraw, "Rs. withdraw successfully ")
except InsufficientBalance as e:
    print(e)
finally:
    print("Operation performed")