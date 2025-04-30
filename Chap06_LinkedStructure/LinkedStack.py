class Node():
    # 생성자
    def __init__(self, elem, link=None):
        self.elem = elem # 노드의 데이터
        self.link = link # 다음 노드를 가리키는 링크

class LinkedStack():
    # 생성자
    # 연결된 구조이기에 용량을 저장할 필요가 없음, 배열도 물론, 
    def __init__(self):
        self.top = None # 시작노드를 가리키는 top

    def isEmpty(self):
        return self.top == None

    def isFull(self):
        return False # 연결구조에서 포화상태는 의미없음

    def push(self, e):
        self.top = Node(e, self.top)

    def pop(self):
        if not self.isEmpty():
            n = self.top # 제일 위를 가리킴
            self.top = n.link # top이 제일 위의 다음을 가리킴
            return n.elem # 제일 위의 데이터를 반환
    
    def peek(self):
        if not self.isEmpty():
            return self.top.elem
        
    def size(self):
        node = self.top
        count = 0
        while not node == None:
            node = node.link # 다음 주소를 가리키게 함
            count += 1
        return count
    
    def __str__(self):
        arr = []
        node = self.top
        while not node == None:
            arr.append(node.elem)
            node = node.link
        return str(arr)
    
if __name__ == "__main__":
    ls = LinkedStack()

    ls.push(1)
    ls.push(2)
    ls.push(3)
    print(ls)