from calculator import Calculation

number1 = float(input("First number = "))
number2 = float(input("Second number = "))
obj = Calculation(number1, number2)

def calculate():
    operation = input("Enter + or - or * or / = ")

    if operation == "+":
        print("Result = ", obj.add())

    elif operation == "-":
        print("Result = ", obj.sub())

    elif operation == "*":
        print("Result = ", obj.multi())

    elif operation == "/":
        print("Result = ", obj.division())


def again():
    while True:
        x = input("Do you want to calculate more? type yes or no = ")
        if x == "yes":
            obj.number1 = float(input("First number = "))
            obj.number2 = float(input("Second number = "))
            calculate()

        elif x == "no":
            print("See you later")
            break

calculate()
again()








