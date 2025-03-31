class Poly:

    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.degree = 0 # 차수
        self.coef = [None] * capacity
    
    # 다항식의 차수를 입력하는 함수?
    def readPoly(self):
        self.degree = int(input("다항식 차수 입력 : "))
        for i in range(self.degree, -1, -1): # n차항부터 상수까지지
            c = int(input(' %d차 항의 계수 : ' % i))
            self.coef[i] = c
    
    def printPoly(self):
        for i in range(self.degree, 0, -1):
            print('%dx^%d + ' % (self.coef[i], i), end ='')
        print(self.coef[0])

    def add(self, polyB):
        polyC = Poly()
        # 더 높은 차수로 설정정
        if self.degree >= polyB.degree:
            polyC.degree = self.degree
        else:
            polyC.degree = polyB.degree
        
        for i in range(polyC.degree, -1, -1):
            # 다항식마다 차수가 다르므로 조건문 제어어
            if self.coef[i] == None:
                polyC.coef[i] = polyB.coef[i]
            elif polyB.coef[i] == None:
                polyC.coef[i] = self.coef[i]
            else:
                polyC.coef[i] = self.coef[i] + polyB.coef[i]

        return polyC
    
    def eval(self, scalar):
        sum = 0
        mul = 1

        for i in range(self.degree+1):
            sum += self.coef[i] * mul
            mul *= scalar
        
        return sum
    
if __name__ == '__main__':
    a = Poly()
    a.readPoly()
    a.printPoly()

    b = Poly()
    b.readPoly()
    b.printPoly()

    c = a.add(b)
    c.printPoly()
    print("C(2) =", c.eval(2))