# 프림 알고리즘을 통한 최소비용 신장트리
Graph = {
    'A':[('B', 29), ('F', 10)],
    'B':[('A', 29), ('C', 16), ('G', 15)],
    'C':[('B', 16), ('D', 12)],
    'D':[('C', 12), ('E', 22), ('G', 18)],
    'E':[('D', 22), ('F', 27), ('G', 25)],
    'F':[('A', 10), ('E', 27)],
    'G':[('B', 15), ('D', 18), ('E', 25)]
}

vCnt = len(Graph) # 정점의 갯수
INF = 1000 # 임의의 큰값
dist = [INF] * vCnt # 각 정점의 거리 배열
visited = [False] * vCnt # 각 정점의 방문 정보


def findMin():
    minDist = INF
    minV = 0 # 0번 인덱스 정점
    
    for v in range(vCnt):
        if visited[v] == False and dist[v] < minDist:
            minDist = dist[v]
            minV = v

    return minV

# 프링 알고리즘 -> 시작정점을 인자로 받음
def prim(vName):
    dist[ord(vName) - 65] = 0 # 무한대였던 거리를 자신인 0으로 변경

    for i in range(vCnt):
        
        for j in range(vCnt):
            if dist[j] == INF:
                print('  * ', end="")
            else:
                print("%3d " % dist[j], end="")
        print()
            
        vNum = findMin() # 처음에는 시작정점이 반환됨
        vName = chr(vNum + 65) # 인덱스를 이름으로 변환

        visited[vNum] = True
        # print('[%c(%d)] ' %(vName, dist[vNum]), end="")

        for e in Graph[vName]: # 찾은 정점의 인접 정접들을 방문
            vNum = ord(e[0]) - 65 # 이름을 인덱스로 변환
            if visited[vNum] == False and e[1] < dist[vNum]: # G에서 인접 정점들이 방문하지 않았고 거리가 더 짧다면 
                dist[vNum] = e[1]
 
if __name__ == "__main__":
    prim('G')