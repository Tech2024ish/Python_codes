import math

def numbers(a,b,c):
    if a==0:
        print("This is not a quadratic.\n")
        return
    d=b**2-4*a*c
    if d>0:
        x1=(-b+math.sqrt(d))/(2*a)
        x2=(-b-math.sqrt(d))/(2*a)
        print(f" There is two real roots: {x1},{x2}\n")
    elif d==0:
        x=-b/(2*a)
        print(f"There is a single real root: {x}\n")
    else:
        real_part=-b/(2*a)
        imaginary_part=math.sqrt(-d)/(2*a)
        print(f"""There is complex roots:
            {complex(real_part,imaginary_part),
             complex(real_part,-imaginary_part)}\n""")
while True:
    try:
        a=int(input("\nEnter the value of a: ")) 
        b=int(input("Enter the value of b: ")) 
        c=int(input("Enter the value of c: "))
        numbers(a,b,c)
    except ValueError:
        print("Wrong input. Please enter the valid input.")
    __continue__=input("Do you want to continue? ").strip().lower()
    if __continue__=="no":
        print("Thank you for using this service. Have a nice day.\n")
        break