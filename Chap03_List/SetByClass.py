class ArraySet:
    
    def __init__(self, capacity = 100):
        self.capacity = capacity # 용량의 사이즈를 넉넉히
        self.size = 0 # 아직 아무것도 집어넣지 않아서 0
        self.array = [None] * capacity # 0보다는 진짜 의미없는 값인 None사용

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity
    
    def __str__(self):
        return str(self.array[0:self.size])
    
    # 여기까지 리스트와 동일
    # 원소가 포함되어 있는 지 확인
    def contains(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                return True # 중간에 발견하면 True를 반환하고 끝남
        
        return False
    
    # 배열의 원소를 삽입
    def insert(self, e):
        if not self.contains(e) and not self.isFull(): # 원소가 없고 꽉 차지 않았을 때
            self.array[self.size] = e
            self.size += 1

    # 배열의 원소를 삭제
    def delete(self, e):
        for i in range(self.size): # 삭제를 해야기에 contains함수는 애매함
            if self.array[i] == e:
                self.array[i] = self.array[self.size-1]
                self.size -= 1 # 정렬 순서는 바뀌지만 집합임
                return

    # 합집합 연산
    def union(self, setB):
        setC = ArraySet() # 합집합을 표현할 집합을 생성
        for i in range(self.size):
            setC.insert(self.array[i]) # 일단 A집합의 원소를 다 대입
        
        for i in range(setB.size):
            if not setC.contains(setB.array[i]): # B에서 C에 없는 것만 대입
                setC.insert(setB.array[i]) 

        return setC
    
    # 교집합 연산
    def intersect(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            if setB.contains(self.array[i]):
                setC.insert(self.array[i])
        
        return setC

    # 차집합 연산
    def difference(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            setC.insert(self.array[i]) # 일단 대입
        
        for i in range(setB.size):
            if setC.contains(setB.array[i]):
                setC.delete(setB.array[i])

        return setC
    
if __name__ == '__main__':
    S = ArraySet()
    S.insert(10)
    S.insert(20)
    S.insert(30)
    S.insert(10) # 중복값 대입
    print("S =", S)

    # S.delete(10)
    # print("S =", S)

    T = ArraySet()
    T.insert(15)
    T.insert(25)
    T.insert(35)
    T.insert(10)
    print('T =', T)
    
    print("S U T =", S.union(T))
    print("S ^ T =", S.intersect(T))
    print("S - T =", S.difference(T))