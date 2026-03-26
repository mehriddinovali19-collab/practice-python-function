def is_strong_password(password: str):
    if len(password) >= 8:
        
        return True
    else:
        return False 
    

def main():
    password = input("Pasrol kiriting: ")

    if is_strong_password(password):
        print("Kuchli parol")
    else:
        print("afsuski kuchsiz parol!")


main()