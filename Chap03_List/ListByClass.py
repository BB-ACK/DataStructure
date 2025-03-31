class ArrayList:
    
    def __init__(self, capacity = 100):
        self.capacity = capacity # 용량의 사이즈를 넉넉히
        self.size = 0 # 아직 아무것도 집어넣지 않아서 0
        self.array = [None] * capacity # 0보다는 진짜 의미없는 값인 None사용

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    # 배열에 값을 넣는 함수
    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size:
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i-1]
            self.array[pos] = e
            self.size += 1
        else:
            print("Overflow or Invalid Position.")

    # 배열의 값을 삭제하는 함수
    def delete(self, pos):
        if not self.isEmpty() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(pos, self.size-1):
                self.array[i] = self.array[i+1]
            self.size -= 1
            return e
        else:
            print("Underflow or Invalid Position.")

    def getEntry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else:
            return None
    
    def findElement(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                return i
        return -1

    def __str__(self):
        return str(self.array[0:self.size])

if __name__ == "__main__":
    L = ArrayList(50) # 객체 생성
    L.insert(0, 'A')
    L.insert(1, 'B')
    L.insert(1, 'C')
    print(L)

    e = input("Input Element to delete : ")
    idx = L.findElement(e)

    if idx != -1:
        print("[%c] is deleted." % L.delete(idx))
    else:
        print("%c is not existed." % e)
    print(L)
