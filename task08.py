def c_to_f(celsius):
    return(celsius * 9/5)+ 35


def f_to_c(fahrenheit):
    return(fahrenheit-32)*5/9


def main():
    print("1 - celsius -> fahrenheit")
    print("2 - fahrenheit -> celsius")

    choice = input("tanlang (1 yoki 2): ")

    if choice == "1":
        c = float(input("celsius ni kiriting: "))
        print("Fahrenheit:", c_to_f(c))
    elif choice == "2":
        c = float (input("fahrenheit ni kiriting: "))
        print("Celsius:", f_to_c(c))

    else:
        print("Noto'g'ri tanlov!")



main()
