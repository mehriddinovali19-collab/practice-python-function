def calculate_bmi(weight: float, height: float):
    bmi = weight /(height **2)
    return bmi


def bmi_status(bmi: float):
    if bmi < 18.5:
        return "underwieght"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overwieght"
    else:
        return "obese"
    

def main():
     weight = float (input("weight(kg): "))
     height = float (input("height(metr): "))

     bmi = calculate_bmi(weight, height)
     status = bmi_status(bmi)


     print(f'bmi: {bmi:.2f}')
     print( f'holat: {status}')

main()


    