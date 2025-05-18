class TNode:
    # 생성자
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
    
    # 단말 노드인지지
    def isLeaf(self):
        return self.left is None and self.right is None
    
# 전위순회 : 루트 -> 왼쪽 -> 오른쪽
def preOrder(n):
    if n is not None:
        print(n.data, end="")
        preOrder(n.left)
        preOrder(n.right)


# 중위순회 : 왼쪽 -> 루트 -> 오른쪽
def inOrder(n):
    if n is not None:
        inOrder(n.left)
        print(n.data, end="")
        inOrder(n.right)

# 후위순회 : 왼쪽 -> 오른쪽 -> 루트
def postOrder(n):
    if n is not None:
        postOrder(n.left)
        postOrder(n.right)
        print(n.data, end="")
    
# 이진트리 노드 수 계산
def countNode(n):
    if n is None:
        return 0
    else:
        return 1 + countNode(n.left) + countNode(n.right)

# 단말노드 수 계산
def countLeaf(n):
    if n is None:
        return 0
    elif n.isLeaf():
        return 1
    else:
        return countLeaf(n.left) + countLeaf(n.right)

# 이진트리 높이 계산 : 더 큰 값에 + 1
def countHeight(n):
    if n is None:
        return 0
    hLeft = countHeight(n.left)
    hRight = countHeight(n.right)

    if hLeft > hRight:
        return hLeft + 1
    else:
        return hRight + 1

if __name__ == "__main__":
    print("\n======= 이진트리 테스트 ===================================") 
    d = TNode('D', None, None)
    e = TNode('E', None, None)
    b = TNode('B', d, e)
    f = TNode('F', None, None)
    c = TNode('C', f, None)
    root = TNode('A', b, c)

    print('\n   In-Order : ', end='')
    inOrder(root)
    print('\n  Pre-Order : ', end='')
    preOrder(root)
    print('\n Post-Order : ', end='')
    postOrder(root)
    print()

    print(" 노드의 개수 = %d개" % countNode(root))
    print(" 단말의 개수 = %d개" % countLeaf(root))
    print(" 트리의 높이 = %d" % countHeight(root))
