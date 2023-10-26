# Q 24.) Write a Python class named Circle constructed by a radius and two 
#        methods which will compute the area and the perimeter of a circle.


import math
class circle():
    radius = float(input("Enter radius of circle: "))

    def area(self):
        area = math.pi*(self.radius)*(self.radius)
        print(f"Area of circle with radius {self.radius} is :", area)

    def perimeter(self):
        per = (math.pi*(self.radius))
        print(f"The perimeter of circle with radius {self.radius} is : ", 2*per)
    
c = circle()
c.area()
c.perimeter()