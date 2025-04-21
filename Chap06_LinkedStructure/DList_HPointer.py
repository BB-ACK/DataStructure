class Node():
    # 생성자
    def __init__(self, data, prev = None,next=None):
        self.data = data # 노드의 데이터
        self.next = next # 다음 노드를 가리키는 링크
        self.prev = prev # 이전 노드를 가리킴
    
class DListType():
    # 생성자
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    def insertFirst(self, data): # 맨 앞에 삽입
        node = Node(data, next=self.head)

        if self.isEmpty():
            self.head = self.tail = node
        else:
            self.head.prev = node
            self.head = node
        
        self.size += 1

    def insertLast(self, data): # 맨 뒤에 삽입
        node = Node(data, prev=self.tail)

        if self.isEmpty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        
        self.size += 1

    def printList(self):
        p = self.head 

        while p != None:
            print("[%s] <-> " % (p.data), end="")
            p = p.next

        print("\b\b\b\b        ")

if __name__ == "__main__":
    DL = DListType()

    DL.insertFirst('A'); DL.printList()
    DL.insertFirst('B'); DL.printList()
    DL.insertLast('C'); DL.printList()

# deletLast, deleteFirst는 직접 구현해보기
# 중간 문제 갯수는 10개 이상
# 객관식, 코딩, 주관식 등 다 존재
# 전체 코드 완성은 필기라 힘들고 길면 10줄 정도 작성하는거
# 박스 치고 코드 빈칸 채우기 같은 유형
# 난이도는 조금 낮춤? -> 중간에 따른 기말유형 결정
# 개별적으로 A4 필요할것 같으면 챙겨오기 
# 필기구 상관 x 