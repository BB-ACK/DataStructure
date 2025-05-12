M = 13

class Node:
    def __init__(self, data, next = 0):
        self.data = data
        self.next = next

class HahsTable:
    def __init__(self):
        self.table = [None] * M

    def hashFn(self, key):
        return key % M 
    
    def insert(self, key):
        bucket = self.hashFn(key) # 연결리스트 구현이기에 오버플로우 발생 안함

        node = Node(key)
        node.next = self.table[bucket]
        self.table[bucket] = node

    def display(self):
        for i in range(M):
            print("HT[%2d] : " % i, end="")
            n = self.table[i]

            while n is not None:
                print(n.data, end=" ")
                n = n.next
            print()


if __name__ == "__main__":
    import random
    
    HT = HahsTable()

    for i in range(20):
        HT.insert(random.randint(10, 99))
    
    HT.display()