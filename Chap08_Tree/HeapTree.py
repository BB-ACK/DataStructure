N = 20

class MaxHeap:
    # 생성자
    def __init__(self):
        self.heap = [None] * N
        self.heapSize = 0 # 원소의 갯수

    # 등반과정 - 삽입 연산시
    def upHeap(self):
        i = self.heapSize # 현재 마지막 노드의 위치
        key = self.heap[i] # 그 위치의 값

        # 올라가는 과정
        while (i != 1) and (key > self.heap[i // 2]): # 부모노드가 존재하고 그 값보다 커야함
            self.heap[i] = self.heap[i // 2]
            i = i // 2

        self.heap[i] = key

    # 하산과정 - 삭제연산시
    def downHeap(self):
        key = self.heap[1]
        p = 1 # 부모 인덱스
        c = 2 # 자식 인덱스

        while c <= self.heapSize: # 자식 노드가 존재한다면
            if (c < self.heapSize) and (self.heap[c+1] > self.heap[c]): # 형제 노드가 존재하고 오른쪽 노드가 크다면
                c += 1

            if (key >= self.heap[c]): # 부모노드가 더 크면 더 내려갈 필요가 없음
                break
            
            self.heap[p] = self.heap[c]
            p = c
            c *= 2
        
        self.heap[p] = key
    
    # 원소 삽입
    def insertItem(self, item):
        self.heapSize += 1 # 0번 인덱스 사용 X
        self.heap[self.heapSize] = item
        self.upHeap() # 맞는 위치까지 올라가기

    # 원소 삭제
    def deleteItem(self):
        key = self.heap[1]

        self.heap[1] = self.heap[self.heapSize]
        self.heapSize -= 1 
        # 여기까지 1번과정 

        self.downHeap()

        return key

if __name__ == "__main__":
    H = MaxHeap()

    data = [9, 7, 6, 5, 4, 3, 2, 2, 1, 3]

    for d in data:
        H.insertItem(d)
        print("Heap :", H.heap[1:H.heapSize+1])

    print("--------------------------------------")
    H.insertItem(8)
    print("Heap :", H.heap[1:H.heapSize+1])
    print("--------------------------------------")


    print("[%d] is deleted:"% H.deleteItem()) 
    print(H.heap[1:H.heapSize+1])
    print("--------------------------------------")
