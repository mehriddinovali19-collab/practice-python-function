def get_grade(score):
    if score>=90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "F"
    else:
        return "D"
    

def main():
    score = int(input("ballingizni kiriting: "))
    print(get_grade(score))

main()