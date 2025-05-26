class TreeNode:
    # 생성자
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# 전위 순회
def preOrder(root):
    if root != None:
        print("%2d " %root.key, end="")
        preOrder(root.left)
        preOrder(root.right)

# 전위 순회 방식으로 메세지 출력
def display(root, msg):
    print(msg, end="")
    preOrder(root)
    print()

# 삽입 연산자
def insert(root, key):
    # 맨 처음 루트가 None이라면 -> 트리가 형성되어 있지 않음 -> 트리를 만듦듦
    if root == None:
        return TreeNode(key)

    # 키 값에 따라 왼쪽 오른쪽 구분, 하위 노드를 root로 건내주어 재귀귀
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        pass

    return root # 메인에서 트리노드를 사용할 수 있도록, 삽입연산자 뿐만 아니라 다른 연산자들에서도 리턴해줘야함

# 삭제 연산자 -> 먼저 탐색을 해줘야함 
def delete(root, key):
    # 삭제할 노드를 찾지 못함
    if root == None:
        return None

    # 삭제할 노드를 찾는 과정
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    # 찾은 경우
    else:
        # case 1: 단말노드이거나 오른쪽 자식만 있는 경우 -> 왼쪽 자식이 없음음
        if root.left == None:
            return root.left # 해당 노드가 none으로 바뀐채 리턴됨
        
        # case 2: 자식노드가 하나인 경우 -> 왼쪽 자식만 존재
        elif root.right == None:
            return root.left # 왼쪽이 부모노드가 됨

        # case 3: 자식노드가 둘 다 존재하는 경우 -> case 1,2와 다름 
        # 구조를 바꾸기 보다 키값을 유효한 값으로 바꿔줘야함 -> 왼쪽 노드의 최댓값 또는 오른쪽 노드의 최솟값이 값을 만족
        else:
            succ = getMinNode(root.right) # 계승자 : 오른쪽 노드의 최솟값
            root.key = succ.key
            root.right = delete(root.right, succ.key)

    return root # 메인에서 트리노드를 사용할 수 있도록, 삽입연산자 뿐만 아니라 다른 연산자들에서도 리턴해줘야함

# 해당 루트 노드의 최솟값을 찾음
def getMinNode(root):
    while root != None and root.left != None:
        root = root.left

    return root

if __name__ == "__main__":
    root = None
    data = [35, 18, 7, 26, 3, 22, 30, 12, 26, 68, 99]

    for key in data:
        root = insert(root, key)
        display(root, "[insert %2d] : " %key)

    print()

    # root = delete(root, 30)
    # display(root, "[delete 30] : ")

    # root = delete(root, 26)
    # display(root, "[delete 26] : ")

    root = delete(root, 18)
    display(root, "[delete 18] : ")