def add(a, b):
    return a+b


def subtract(a, b):
    return a -b 


def multiply(a, b):
    return a*b


def divide(a, b):
    if b !=0 :
        return a/b
    else:
        return None
    

def main():
    a = float(input("a ga son bering: "))
    b = float(input("b ga son bering: "))
    op = input("amal: ")

    if op == "+":
        print(add(a, b))
    elif op == "-":
        print(subtract(a, b))
    elif op == "*":
        print(multiply(a, b))
    elif op == "/":
        result = divide(a, b)
        if result == None:
            print("0 ga bo'lish mukin emas!")
        else:
            print(result)
    else: 
        print("bo'nday amla mavjud emas!")

main()
