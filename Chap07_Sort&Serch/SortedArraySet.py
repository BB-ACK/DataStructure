class SortedArraySet:
    # 생성자
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def __str__(self):
        return str(self.array[0:self.size])

    # 배열에 해당요소가 있는지 확인하는 함수
    def contains(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                return True
            
        return False
    
    # 집합에 원소를 삽입정렬함함
    def insert(self, e):
        if self.contains(e) or self.isFull():
            return
        
        self.array[self.size] = e
        self.size += 1

        # 집합을 정렬하기 위해서
        for i in range(self.size-1, 0, -1):
            if self.array[i-1] < self.array[i]: # 들어온 요소가 더 크면 끝내면 됨
                break
            
            self.array[i-1], self.array[i] = self.array[i], self.array[i-1]

    # 집합에 요소를 삭제 후 정렬
    def delete(self, e):
        if not self.contains(e):
            return
        
        i = 0
        while self.array[i] < e: # 삭제할 요소의 위치를 찾음
            i += 1

        self.size -= 1

        while i < self.size: # 삭제할 요소 뒤에부터 앞으로 당기면 됨
            self.array[i] = self.array[i+1]
            i += 1

    # 합집합 
    def Union(self, setB):
        setC = SortedArraySet()
        i = 0 # A를 순회할 인덱스
        j = 0 # B를 순회할 인덱스

        while i < self.size and j < setB.size:
            a = self.array[i]
            b = setB.array[j]

            if a == b: # 같으면 둘 중하나 넣으면 됨
                setC.append(a)
                i += 1; j += 1
            elif a < b:
                setC.append(a)
                i += 1
            else:
                setC.append(b)
                j += 1

        # 둘 중 하나가 먼저 끝나서 a나 b중에 요소가 남아 있을 수 있음
        while i < self.size:
            setC.append(self.array[i])
            i += 1

        while i < setB.size:
            setC.append(setB.array[i])
            j += 1

        return setC

if __name__ == "__main__":
    import random
    setA = SortedArraySet()
    for i in range(5):
        setA.insert(random.randint(1, 9))

    print("Set A :", setA)