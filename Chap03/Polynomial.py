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

if __name__ == '__main__':
    a = Poly()
    a.readPoly()
    a.printPoly()
    
    #a.add()

# 과제 설명
# 1. 이 코드에서 add, 임의의 x값을 전달해서 결과 값을 출력하는 것
# 2. 교제 3.4 라인편집기
# 명령 i d r p l s 구현 -> 파일 입출력도 필요한듯? text.html
# 입력, 삭제, 변경, 출력, 읽기, 저장, 종료
# from ArrayList import ArrayList
# 다시 시작하면 라인 에디터에서는 0부터 시작 
# 로드를 하게 되면 기전의 텍스트 불러오기
