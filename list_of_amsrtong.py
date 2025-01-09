def check_number(number):
    amstrong_num=[]
    for num in range(number):
        num_str=str(num)
        
        total=sum(int(i)**len(num_str) for i in num_str)
        if total==num:
            amstrong_num.append(total)  
    return amstrong_num   
while True:
    try:
        number1=int(input("\nEnter the number: "))
        print(f"\nResult is: {check_number(number1)}\n")
    except ValueError:
        print("Invalid input. Enter the valid integer.")
    __con__=input("Continue? ").lower()
    if __con__=="no":
        print("Thank you for checking. Nice day.\n")
        break