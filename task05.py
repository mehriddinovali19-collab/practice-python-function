def check_guess(secret, guess):
    return secret == guess


def print_result(is_correct):
    if is_correct:
        print("to'gri topdingiz ")
    else:
        print("xato topdingiz")


def main():
    secret = 123
    while True:
        guess = float(input("parol kiriting: "))
        result = (check_guess(secret, guess))
        print_result(result)

        if result:
            break

main()