def calculate_tax(salary: float):
    if salary >= 5_000_000:
        tax = salary * 0.20
    else:
        tax = salary * 0.13
    return tax


def calculate_net_salary(salary: float):
    tax = calculate_tax(salary)
    net_salary = salary - tax 
    return net_salary


def main():
    salary = float(input(" moashingizni kiriting: "))
    tax = calculate_tax(salary)
    net_tax = calculate_net_salary(salary)

    print(f"soliq: {tax}")
    print(f"moashni uzi: {net_tax}")


main()