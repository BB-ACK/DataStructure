import queue

class Node:
    # 생성자
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class AVLTree:
    # 생성자
    def __init__(self):
        self.root = None

    # 해당 노드의 길이를 계산하는 함수
    def cal_height(self, node):
        if node == None:
            return 0
        
        hleft = self.cal_height(node.left)
        hright = self.cal_height(node.right)

        # 더 큰 값에 +1
        if hleft > hright:
            return hleft + 1
        else:
            return hright + 1
    
    # 해당 노드의 균형 값을 계산하는 함수
    def cal_balance(self, node):
        if node == None:
            return 0
        return self.cal_height(node.left) - self.cal_height(node.right)
    
    # LL -> 왼쪽 자식에 왼쪽 서브트리에 삽입되어서 균형이 무너짐
    def rotateLL(self, node):
        lNode = node.left
        node.left = lNode.right
        lNode.right = node
        
        return lNode # lnode가 부모노드가 되어서 반환

    # RR -> 오른쪽 자식에 오른쪽 서브트리에 삽입되어서 균형이 무너짐
    def rotateRR(self, node):
        rNode = node.right
        node.right = rNode.left
        rNode.left = node

        return rNode 
    
    # LR -> 왼쪽 자식에 오른쪽 서브트리에 삽입되어서 균형이 무너짐 -> 자식부터 RR - LL 순으로 회전
    def rotateLR(self, node):
        node.left = self.rotateRR(node.left)

        return self.rotateLL(node) # RR의 lnode가 다름 -> 회전 후 달라짐 
    
    # RL -> 오른쪽 자식에 왼쪽 서브트리에 삽입되어서 균형이 무너짐 -> 자식부터 LL - RR 순으로 회전
    def rotateRL(self, node):
        node.right = self.rotateLL(node.right)

        return self.rotateRR(node)
    
    # 원소 삽입함수 -> 균형이 무너지면 맞춤
    def insert(self, node, e):
        if node == None:
            return Node(e)
        
        if e < node.data:
            node.left = self.insert(node.left, e)
        elif e > node.data:
            node.right = self.insert(node.right, e)

        bf = self.cal_balance(node) # 삽입 후 균형 확인

        if bf > 1: # 왼쪽 노드의 불균형 발생
            if e < node.left.data: # 왼쪽에 삽입됨 -> LL
                return self.rotateLL(node)
            else: # 오른쪽에 삽입됨 -> LR
                return self.rotateLR(node)
        
        elif bf < -1: # 오른쪽 서브트리에서 불균형 발생
            if e > node.right.data: # 오른쪽에 삽입됨 -> RR
                return self.rotateRR(node)
            else: # 왼쪽에 삽입됨 -> RL
                return self.rotateRL(node)

        return node

    # 큐를 이용한 레벨 순회 -> BFS와 유사
    def levelOrder(self, root):
        Q = queue.Queue()
        Q.put(root)

        while not Q.empty():
            root = Q.get() 
            print("[%d]" % root.data, end="")

            # 자식 노드가 존재한다면 큐에 삽입
            if root.left != None:
                Q.put(root.left)

            if root.right != None:
                Q.put(root.right)
        print()

if __name__ == "__main__":
    node = [7,8,9,2,1,5,3,6,4]
    avl = AVLTree()

    for n in node:
        avl.root = avl.insert(avl.root ,n)

    avl.levelOrder(avl.root)