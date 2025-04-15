# 우선순쉬 큐는 순서가 없기에 선형 자료구조가 아니다
# 따라서 배열을 정리할 필요가 없고 가장 우선순위 요소만 찾아주어 인덱싱 하면 된다

class priorityQueue():
    # 생성자
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def enqueue(self, e):
        if not self.isFull():
            self.array[self.size] = e
            self.size += 1
    
    # 우선순위 기준이 가장 큰 항목
    def findMaxIndex(self):
        if self.isEmpty():
            return -1
        highest = 0
        for i in range(0, self.size): #O(n)
            if self.array[i] > self.array[highest]:
                highest = i
        
        return highest
    
    def dequeue(self):
        highest = self.findMaxIndex()
        if highest != -1:
            self.size -= 1
            # 가장 뒤로 보냄
            self.array[highest], self.array[self.size]  =\
                self.array[self.size], self.array[highest]
            return self.array[self.size]
    
    def peek(self):
        highest = self.findMaxIndex()
        if highest != -1:
            return self.array[highest]
    
    def __str__(self):
        return str(self.array[0:self.size])
    
if __name__ == "__main__":
    pq =priorityQueue()

    pq.enqueue(34)
    pq.enqueue(18)
    pq.enqueue(27)
    pq.enqueue(45)
    pq.enqueue(15)
    
    print("PQueue:", pq)
    while not pq.isEmpty():
        print("Max Priority = ", pq.dequeue())
