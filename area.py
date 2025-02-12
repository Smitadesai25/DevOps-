# Class to represent a rectangle and calculate its area
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
class circle(rectangle):
    def __init__(self,r):
        self.r=r

    def calculate_area2(self):
        return 3.14*self.r*2

    def calculate_area(self):
        return self.length * self.width

# Example usage:
rectangle_instance = Rectangle(5, 8)
rectangle_instance = circle(5)
result = rectangle_instance.calculate_area()
result1 = rectangle_instance.calculate_area1()
print(f"Area of Rectangle: {result}")
print(f"Area of circe: {result1}")

