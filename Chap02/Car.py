class Car:
    # 무조건 첫 번째 매개변수는 self다
    # 생성자, 생성자 안에서 객체가 가질 변수를 선언
    def __init__(self, color, speed = 0):
        self.color = color # 생성자 매개변수와 같게 하는 것이 좋다
        self.speed = speed

    def speedUp(self):
        self.speed += 10

    def speedDown(self):
        self.speed -= 10

    def __str__(self):
        return "Color : %s - Speed : %d" %(self.color, self.speed)

if __name__ == '__main__':
    car1 = Car('Black', 123)
    car2 = Car('Red', 50)

    print(car1)
    print(car2)

    car1.speedDown()
    print(car1)

