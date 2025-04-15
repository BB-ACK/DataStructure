from CircularQueue import *

class CircularDeque(CircularQueue):
    # 클래스의 생성자는 상속되지 않음
    def __init__(self, capacity=10):
        super().__init__(capacity) # super()를 통해 부모의 생성자를 호출

    # isEmpty, isFull, size, display는 원형큐와 동일하므로 정의할 필요 없음 

    # 뒤에 원소를 넣는 것으로 원형큐 enqueue연산과 동일
    def addRear(self, e):
        self.enqueue(e)

    # 뒤에 원소를 빼고 반환 -> dequeue와 동일
    def deleteFront(self):
        return self.dequeue()
    
    # 맨 앞의 요소 참조 -> peek과 동일
    def getFront(self):
        return self.peek()

    # 맨 앞에 요소를 추가하는 함수
    def addFront(self, e):
        if not self.isFull():
            self.array[self.front] = e
            self.front = (self.front - 1 + self.capacity) % self.capacity
        else:
            pass
    
    # 맨 뒤에 요소를 제거하는 함수
    def deleteRear(self):
        if not self.isEmpty():
            e = self.array[self.rear]
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return e
        else:
            pass
    
    # 맨 뒤에 요소를 참조하는 함수
    def getRear(self):
        if not self.isEmpty():
            return self.array[self.rear]
        else:
            pass

    def __str__(self):
        if(self.front < self.rear):
            return str(self.array[self.front+1:self.rear+1])
        else:
            return str(self.array[self.front+1:self.capacity] + self.array[0:self.rear+1]) # 프론트 부터 끝까지, 그리고 0부터 rear까지
         

if __name__ == "__main__":
    dq = CircularDeque()

    for i in range(9):
        if i % 2 == 0:
            dq.addRear(i)
        else:
            dq.addFront(i)
    print("홀수 -> 전단, 짝수 -> 후단:", dq)

    for i in range(2):
        dq.deleteFront()
    for i in range(3):
        dq.deleteRear()
    print("전단 삭제X2, 후단 삭제X3:", dq)