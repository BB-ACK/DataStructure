INF = 1000

vName = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
Graph = [
    [ 0, 7, INF, INF, 3, 10, INF],
    [ 7, 0, 4, 10, 2, 6, INF],
    [INF, 4, 0, 2, INF, INF, INF],
    [INF, 10, 2, 0, 11, 9, 4],
    [ 3, 2, INF, 11, 0, 13, 5],
    [ 10, 6, INF, 9, 13, 0, INF],
    [INF, INF, INF, 4, 5, INF, 0]
]

vCnt = len(Graph) # 정점의 갯수
dist = [INF] * vCnt # 각 정점의 거리 배열
visited = [False] * vCnt # 각 정점의 방문 정보

# 방문하지 않은 정점 중 최솟거리 정점을 찾는 함수수
def findMin():
    minDist = INF
    minV = 0 # 0번 인덱스 정점
    
    for v in range(vCnt):
        if visited[v] == False and dist[v] < minDist:
            minDist = dist[v]
            minV = v

    return minV

# 거리의 배열을 보여주는 함수
def display():
    for i in range(vCnt):
        if dist[i] == INF:
            print(' * ', end="")
        else:
            print("%2d " % dist[i], end="")
    print()

def dijkstra(s):
    dist[ord(s) - 65] = 0

    for i in range(vCnt):
        s = findMin()
        visited[s] = True

        for t in range(vCnt):
            # 원래의 거리보다 경유 거리가 더 짧으면 갱신
            if dist[t] > dist[s] + Graph[s][t]:
                dist[t] = dist[s] + Graph[s][t]

        print('[%c] : ' %vName[s], end="")
        display()

if __name__ == "__main__":
    dijkstra('A')