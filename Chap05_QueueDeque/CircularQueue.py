class CircularQueue:
    # 생성자
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.array = [None] * capacity

    def isEmpty(self):
        return self.front == self.rear # 요소가 하나라도 존재한다면 같을 수 없음
    
    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity # 끝 기준 한 칸 앞에 있을 때
    
    # push같은 함수: 제일 뒤에 추가
    def enqueue(self, e):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = e
        else:
            print("Overflow!")

    # pop같은 함수: 제일 앞에 요소를 반환
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else:
            print("Underflow")

    # 맨 앞의 요소를 반환
    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        else:
            print("Underflow")

    # 원소의 개수를 반환
    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity

    # 현재 큐를 출력
    def display(self):
        print("Front : %d, Rear : %d" % (self.front, self.rear))

        i = self.front

        while i != self.rear:
            i = (i+1) % self.capacity
            print("[%c] " % self.array[i],end="")
        print()
        
if __name__ == "__main__":
    Q = CircularQueue()

    data = ['A', 'B', 'C', 'D', 'E']
    
    for e in data:
        Q.enqueue(e)
    
    Q.display()
    
    print("Dequeue -->", Q.dequeue())
    print("Dequeue -->", Q.dequeue())    
    Q.display()

    data = ['F', 'G', 'H', 'I']

    for e in data:
        Q.enqueue(e)
    
    Q.display()
    
    print("Dequeue -->", Q.dequeue())
    print("Dequeue -->", Q.dequeue())    
    Q.display()

    Q.enqueue('Z')
    Q.display()