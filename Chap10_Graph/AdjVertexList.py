# 인접 정점 리스트를 통한 그래프
vName = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
visited = [False] * len(vName)

Graph = [
    [1, 2],
    [0, 3],
    [0, 3, 4],
    [1, 2, 5],
    [2, 6, 7],
    [3],
    [4, 7],
    [4, 6]
]

# 내장 스택
from queue import LifoQueue # 필요한 peek()가 제공되지 않음

class Stack(LifoQueue):
    # 제일 위 값을 보는 함수
    def peek(self):
        if not self.empty():
            return self.queue[-1] # 제일 위에 값을 값만 보냄
        raise Exception("Empty")
    
def iDFS(s):
    S = Stack()
    
    S.put(s) # 시작 정점을 스택에 넣어줌
    visited[s] = True # 시작 정점은 방문
    print("[%c] " %vName[s], end="")

    while not S.empty():
        s = S.peek() # 0번에서 시작했다면 1 과 2가 차례로 드어옴
        flag = False

        for t in Graph[s]:
            if visited[t] == False: # 아직 방문하지 않았다면
                S.put(t)
                visited[t] = True
                print("[%c] " %vName[t], end="")

                flag = True
                break
        
        # 이미 방문해서 로직이 돌아가지 않은 경우
        if flag == False:
            S.get() # pop된 것
            

if __name__ == '__main__':
    print("iDFS : ", end="")
    iDFS(1) # 1번 정점부터 시작