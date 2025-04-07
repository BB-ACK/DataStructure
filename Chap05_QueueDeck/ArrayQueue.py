class ArrayQueue:
    # 생성자
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.front = -1
        self.rear = -1
        self.array = [None] * capacity

    def isEmpty(self):
        return self.front == self.rear # 요소가 하나라도 존재한다면 같을 수 없음
    
    def isFull(self):
        return self.rear == self.capacity - 1
    
    # push같은 함수: 제일 뒤에 추가
    def enqueue(self, e):
        if not self.isFull():
            self.rear += 1
            self.array[self.rear] = e
        else:
            print("Overflow!")

    # pop같은 함수: 제일 앞에 요소를 반환
    def dequeue(self):
        if not self.isEmpty():
            self.front += 1
            return self.array[self.front]
        else:
            print("Underflow")

    # 현재 큐를 출력
    def display(self):
        print("Front : %d, Rear : %d" % (self.front, self.rear))
        print(self.array[self.front+1:self.rear+1])

if __name__ == "__main__":
    Q = ArrayQueue()

    data = ['A', 'B', 'C', 'D', 'E']
    
    for e in data:
        Q.enqueue(e)
    
    Q.display()
    
    print("Dequeue -->", Q.dequeue())
    print("Dequeue -->", Q.dequeue())    
    Q.display()


    for e in data:
        Q.enqueue(e)
    
    Q.display()
    
    print("Dequeue -->", Q.dequeue())
    print("Dequeue -->", Q.dequeue())    
    Q.display()

    Q.enqueue('F')
    Q.display()