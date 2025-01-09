class Shaps:
    def area(self):
        return "Area is not defined"

class Rectangle(Shaps):
    def __init__(self):
        self.length=int(input("\nEnter the length of rectangle: "))
        self.width=int(input("Enter the width of rectangle: "))

    def area(self):
        return (f"\nArea of Rectangle is: {self.length*self.width}")

class Circle(Shaps):
    def __init__(self,):
        self.radius=int(input("Enter the radius of circle: "))

    def area(self):
        return (f"Area of Circle is: {3.14*self.radius**2}\n")
#polymorphism
Shaps=[Rectangle(),Circle()]
for shape in Shaps:
    print(shape.area())