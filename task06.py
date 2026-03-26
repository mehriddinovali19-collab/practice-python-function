def is_valid_phone_number(phone: str):
    result = phone.isdigit() and len(phone) == 9
    return result


def main():
    phone_number = (input("Telifon raqamingizni kiriting: "))
    if is_valid_phone_number(phone_number):
        print("True")
    else:
        print("False")


main()