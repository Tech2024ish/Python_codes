import math

def check_perfect_cubic_root(num):
    cubic_root=math.cbrt(num)
    if cubic_root**3==num:
        print(f"The cubic root of {num} is: {cubic_root}\n")
    else:
        print(f"Error, {num} has no perfect cubic root.\n")

while True:
    try:
        number=int(input("\nEnter the integer num: "))
        check_perfect_cubic_root(number)
    except ValueError:
        print("Wrong input. Enter the valid integer.")
    __continue__=input("Do you want to continue? ").lower()
    if __continue__=="no":
        print("Thank you for cheching. Have a nice day.\n")
        break