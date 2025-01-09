"""
Write a program that repeatedly prompts user for integer numbers
until the user enters 'done'. Once 'done' entered, print out the 
largest and smallest numbers. If the user entered other thing than
valid number catch it with try/ecept and print out the appropriate
massage and ignore that number.

"""
def number_from_user():
    largest_num=None
    smallest_num=None
    print("\n")

    while True:
        user_input=input("Enter a number(or 'done' to finish): ")
        if user_input=="done":
            break
        try:
            number=int(user_input)
            if largest_num is None or number>largest_num:
                largest_num=number

            if smallest_num is None or number<smallest_num:
                smallest_num=number
        except ValueError:
            print("Invalid input. Enter the valid input.")

    if largest_num is not None and smallest_num is not None:
        print(f"\nThe largest number is: {largest_num}")
        print(f"The smallest number is: {smallest_num}\n")
    else:
        print("No valid numbers were entered\n")

if __name__=="__main__":
    number_from_user() 