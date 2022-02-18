from calculatorLogic import *

def main():
    print("Choose which operation to run: ")
    print("'1' for addition")
    print("'2' for subtraction")
    print("'3' for multiplication")
    print("'4' for division")
    print("Any other input will cause an error and repeat the input.")
    while True:
        switch = input("Please type your operation: ")
        if switch == '1':
            addition()
            break
        elif switch == '2':
            subtraction()
            break
        elif switch == '3':
            multiplication()
            break
        elif switch == '4':
            division()
            break
        else:
            print('Error! Please type the correct operation.')
            continue
main()