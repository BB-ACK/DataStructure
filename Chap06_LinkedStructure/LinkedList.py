class Node():
    # 생성자
    def __init__(self, elem, link=None):
        self.elem = elem # 노드의 데이터
        self.link = link # 다음 노드를 가리키는 링크

class LinkedList():
    # 생성자
    def __init__(self):
        self.head = None # 시작노드를 가리키는 head를 지칭

    def isEmpty(self):
        return self.head == None # head가 None이면 공백
    
    def isFull(self):
        return False # 연결된 구조는 포화상태가 될 수 없음
    
    def getNode(self, pos):
        if pos < 0:
            return False
        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        
        return node
    
    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None:
            return None
        else:
            return node.elem
        
    def insert(self, pos, e):
        before = self.getNode(pos-1)
        if before == None: # 시작 위치에 삽입하는 경우
            self.head = Node(e, self.head)
        else:
            node = Node(e, before.link) # B가 C를 가리키던 것을 사이에 들어가서
            before.link = node # 새로 만든 노드를 가리키게 함
        
    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None: # 시작 위치를 삭제하는 경우
            if self.head is not None: # 다음 요소가 존재하면 
                self.head = self.head.link # 시작요소가 시작요소의 다음 노드가 된다
        elif before.link != None:
            before.link = before.link.link # 다음 다음 요소를 가리키도록 B C D에서 C를 삭제한다면 B가 D를 가리키도록

    def size(self):
        node = self.head
        count = 0
        while not node == None:
            node = node.link # 다음 주소를 가리키게 함
            count += 1
        return count
    
    def __str__(self):
        arr = []
        node = self.head
        while not node == None:
            arr.append(node.elem)
            node = node.link
        return str(arr)