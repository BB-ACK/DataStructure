class Node():
    # 생성자
    def __init__(self, data, prev = None,next=None):
        self.data = data # 노드의 데이터
        self.next = next # 다음 노드를 가리키는 링크
        self.prev = prev # 이전 노드를 가리킴
    
class DListType():
    # 생성자
    def __init__(self):
        self.head = Node(0) # 의미없는 값을 가진 노드를 생성, next로 첫 노드를 가리켜야함
        self.tail = Node(0) # 마지막노드를 가리킴, prev로 마지막 노드를 가리켜야함
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def insert(self, pos, data):
        if pos <= 0 or pos > self.size + 1:
            print("Invalid")
            return
        
        p = self.head # 탐색을 위한 첫 위치

        for _ in range(1, pos):
            p = p.next

        node = Node(data) # 삽입할 노드를 생성
        node.prev = p # 생성된 노드를 세팅
        node.next = p.next 
        p.next.prev = node # 기존 노드들 변경
        p.next = node

        self.size += 1

    def delete(self, pos):
        if pos <= 0 or pos > self.size:
            print("Invalid Position")
            return
        
        p = self.head # 탐색을 위한 첫 위치

        for _ in range(pos):
            p = p.next # 삭제할 노드를 가리키게됨

        data = p.data

        p.prev.next = p.next
        p.next.prev = p.prev

        self.size -= 1

        return data

    def printList(self):
        p = self.head.next # 헤드 포인터를 제외한 첫 노드를 가리킴

        while p != self.tail:
            print("[%s] <-> " % p.data, end="")
            p = p.next

        print("\b\b\b\b        ")

if __name__ == "__main__":
    DL = DListType()

    DL.insert(1, 'A'); DL.printList()
    DL.insert(1, 'B'); DL.printList()
    DL.insert(2, 'C'); DL.printList()
    DL.insert(4, 'D'); DL.printList()

    print("[%s] is deleted." % DL.delete(3)); DL.printList()