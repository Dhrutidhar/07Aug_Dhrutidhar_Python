# Q 23.) Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.


class rectangle():
    def area(self):
        self.lenght = float(input("Enter Lenght of Rectangle: ")) 
        self.breath = float(input("Enter Breath of Rectangle: ")) 
        self.area = self.lenght*self.breath 
        print("The Area of Rectangle is: ",self.area)
a = rectangle()
a.area()
