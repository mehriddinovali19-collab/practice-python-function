def ask_question(question: str, correct_answer: str):
    return question


def check_answer(user_answer, correct_answer):
    if correct_answer == user_answer:
        print("javob qabul qilindi")
    else:
        print("javob xatolik bor!")


def main():
    correct_answer = "Russia"
    question =input(ask_question("Eng katta mamlakat qaysi? ", correct_answer))
    
    check_answer(question, correct_answer)


main()