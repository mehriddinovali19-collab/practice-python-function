def deposit(balance, amount):
    if amount > 0:
        balance += amount
        
        return balance


def withdraw(balance, amount):
    if amount > 0  and amount <= balance:
        balance -= amount 

        return balance


def check_balance(balance):
    print(f'sizning hisobingizda: {balance}')


def main():
    balance = 500
    
    amount = float(input("enter an amount: "))
    op = input("amal: ")

    if op == "deposit":
       hisob =  deposit(balance, amount)
    elif op == "withdraw":
       hisob = withdraw (balance, amount)
    else:
        print("amal noto'gri!")


    check_balance(hisob)

main()
