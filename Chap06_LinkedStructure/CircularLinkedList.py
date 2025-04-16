class Node():
    # 생성자
    def __init__(self, data, next=None):
        self.data = data # 노드의 데이터
        self.next = next # 다음 노드를 가리키는 링크

class CircularLinkedList():
    # 생성자
    # 연결된 구조이기에 용량을 저장할 필요가 없음, 배열도 물론, 
    def __init__(self):
        self.tail = None # 가장 끝에 요소 / 여기서는 가장 마지막 인덱스 느낌
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    def insertLast(self, data): # insertFront()
        node = Node(data)

        if self.isEmpty(): # 처음이자 끝인경우
            node.next = node # 다음 노드는 자기 자신 / 나는 나를 가리킴
            self.tail = node # 누군가도 나를 가리킴
        else:
            node.next = self.tail.next # 자신이 가리키는 것 / 제일 앞부분을 계속 계승
            self.tail.next = node # 제일 마지막 요소는 이제 자신임
            self.tail = node
        
        self.size += 1

    def insertFirst(self, data): # insertRear()
        node = Node(data)

        if self.isEmpty(): # 처음이자 끝인경우
            node.next = node
            self.tail = node 
        else:
            node.next = self.tail.next 
            self.tail.next = node 
        
        self.size += 1

    def deleteFirst(self): # deleteFront()
        if not self.isEmpty():
            p = self.tail # 마지막 노드
            q = p.next # 처음 노드

            if p == q: # 노드가 하나라면
                self.tail = None
            else:
                p.next = q.next

            self.size -= 1
            return q.data
    
        else:
            print("Underflow.")

    def deleteLast(self): # deleteRear()
        if not self.isEmpty():
            p = self.tail # 마지막 노드
            q = p.next # 처음 노드

            if p == q: # 노드가 하나라면
                self.tail = None
            else:
                while q.next != p: # 처음 노드가 마지막 노드 전까지 이동
                    q = q.next
                
                q.next = p.next # 마지막 전 노드가 시작 노드를 가리키도록
                self.tail = q # 마지막 전 노드가 마지막이됨

            self.size -= 1
            return p.data
    
        else:
            print("Underflow.")

    def printList(self):
        p = self.tail # 마지막 노드를 가리킴

        if not self.isEmpty():
            while True:
                print("[%s] -> " % (p.next.data), end="") # 첫노드부터 시작
                p = p.next

                # 마지막 노드이면
                if p == self.tail:
                    break

            print("\b\b\b    ")

if __name__ == "__main__":
    cll = CircularLinkedList()

    cll.insertLast('A')
    cll.insertLast('B') 
    cll.insertLast('C')

    cll.insertFirst('D')
    cll.insertFirst('E')
    cll.insertFirst('F')

    cll.printList()

    cll.deleteFirst()
    cll.deleteLast()

    cll.printList() 