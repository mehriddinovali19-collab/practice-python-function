def calculate_age(birth_year, current_year):
    return current_year - birth_year


def main():
    current_year = 2026
    birth_year = int(input("Qachon to'g;ilgansiz? "))

    age = calculate_age(birth_year, current_year)
    if age >= 18:
        print("Siz voyaga yetkansiz")
    else:
        print("Siz voyaga yetmagansiz! ")

main()