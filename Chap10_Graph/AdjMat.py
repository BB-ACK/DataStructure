# 인접 행렬을 통한 그래프
vName = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
visited = [False] * len(vName)

Graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0]
]

# 재귀를 통한 DFS
def rDFS(s):
    visited[s] = True # 시작 정점은 방문
    print("[%c] " %vName[s], end="")

    for t in range(len(vName)):
        if(Graph[s][t] == 1 and visited[t] == False): # 인접 정점이여야하고 방문 전 이여야한다
            rDFS(t) # 재귀 접근으로 t노드에 접근

if __name__ == '__main__':
    print("rDFS : ", end="")
    rDFS(1) # 1번 정점부터 시작