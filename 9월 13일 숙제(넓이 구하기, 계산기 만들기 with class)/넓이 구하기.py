
class Area():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def square(self):
        return self.num1 * self.num2
    def triangle(self):
        return self.num1 * self.num2 / (1/2)   
    def circle(self):
        return (self.num1/(1/2))*2 *3.14 

Area1 = Area(10, 20)
print(Area1.square()) # 사각형의 넓이
print(Area1.triangle()) # 삼각형의 넓이
print(f'{Area1.circle():.2f}') # 원의 넓이