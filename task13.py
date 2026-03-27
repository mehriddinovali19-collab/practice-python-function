def is_palindrome(text: str):
    return text == text[::-1]


def main():
    word = str(input("matn kiriting: "))

    if is_palindrome(word):
        print("Bu palindrome ")
    else:
        print("Bu palindrome emas ")

main()