# Dictionary를 이용한 BFS 탐색
Graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D', 'E'],
    'D': ['B', 'C', 'F'],
    'E': ['C', 'G', 'H'],
    'F': ['D'],
    'G': ['E', 'H'],
    'H': ['E', 'G']
}

visted = {}

from queue import Queue

def BFS(s):
    Q = Queue()

    Q.put(s)
    visted[s] = True
    print("[%c] " % s, end="")

    while not Q.empty():
        s = Q.get() # 일단 뺌

        for t in Graph[s]:
            if t not in visted: # 똑같이 방문하지 않았다면 
                visted[t] = True
                print("[%c] " %t, end="")
                Q.put(t)

if __name__ == '__main__':
    print("BFS : ", end="")
    BFS('B') # 1번 정점부터 시작