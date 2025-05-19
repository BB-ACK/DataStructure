import queue

class TNode:
    # 생성자
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
    
    # 단말 노드인지
    def isLeaf(self):
        return self.left is None and self.right is None

class BTree:
    def __init__(self):
        self.root = None
    
    # 전위순회 : 루트 -> 왼쪽 -> 오른쪽
    def preOrder(self, root):
        if root is not None:
            print("[%c]" % root.data, end="")
            self.preOrder(root.left)
            self.preOrder(root.right)


    # 중위순회 : 왼쪽 -> 루트 -> 오른쪽
    def inOrder(self, root):
        if root is not None:
            self.inOrder(root.left)
            print("[%c]" % root.data, end="")
            self.inOrder(root.right)

    # 후위순회 : 왼쪽 -> 오른쪽 -> 루트
    def postOrder(self, root):
        if root is not None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print("[%c]" % root.data, end="")
            
    # 큐를 이용한 레벨 순회 -> BFS와 유사
    def levelOrder(self, root):
        Q = queue.Queue()
        Q.put(root)

        while not Q.empty():
            root = Q.get() 
            print("[%c]" % root.data, end="")

            # 자식 노드가 존재한다면 큐에 삽입
            if root.left != None:
                Q.put(root.left)

            if root.right != None:
                Q.put(root.right)
        print()

    # 이진트리 노드 수 계산
    def countNode(self, root):
        if root is None:
            return 0
        else:
            return 1 + self.countNode(root.left) + self.countNode(root.right)

    # 단말노드 수 계산
    def countLeaf(self, root):
        if root is None:
            return 0
        elif root.isLeaf():
            return 1
        else:
            return self.countLeaf(root.left) + self.countLeaf(root.right)

    # 이진트리 높이 계산 : 더 큰 값에 + 1
    def countHeight(self, root):
        if root is None:
            return 0
        hLeft = self.countHeight(root.left)
        hRight = self.countHeight(root.right)

        if hLeft > hRight:
            return hLeft + 1
        else:
            return hRight + 1

if __name__ == "__main__":
    print("\n======= 이진트리 테스트 ===================================") 
    BT = BTree()

    d = TNode('D', None, None)
    e = TNode('E', None, None)
    b = TNode('B', d, e)
    f = TNode('F', None, None)
    c = TNode('C', f, None)
    root = TNode('A', b, c)

    print('\n    In-Order : ', end='')
    BT.inOrder(root)
    print('\n   Pre-Order : ', end='')
    BT.preOrder(root)
    print('\n  Post-Order : ', end='')
    BT.postOrder(root)
    print('\n Level-Order : ', end='')
    BT.levelOrder(root)


    print()

    print(" 노드의 개수 = %d개" % BT.countNode(root))
    print(" 단말의 개수 = %d개" % BT.countLeaf(root))
    print(" 트리의 높이 = %d" % BT.countHeight(root))
