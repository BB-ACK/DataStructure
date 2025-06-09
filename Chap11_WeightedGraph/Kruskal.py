# 크루스칼을 이용한 최소 신장 트리리
Graph = {
    'A':[('B', 29), ('F', 10)],
    'B':[('A', 29), ('C', 16), ('G', 15)],
    'C':[('B', 16), ('D', 12)],
    'D':[('C', 12), ('E', 22), ('G', 18)],
    'E':[('D', 22), ('F', 27), ('G', 25)],
    'F':[('A', 10), ('E', 27)],
    'G':[('B', 15), ('D', 18), ('E', 25)]
}

eList = []
vertices = [-1, -1, -1, -1, -1, -1, -1] # 유니온 파인드를 위한 정점들의 부모-자식 관계 / -1은 개별적인 집합의 의미

# 간선을 정렬하는 함수
def edgeSort():
    for v in Graph: # 'A', 'B' ....
        for e in Graph[v]: # (B, 29), (F, 10) ...
            if v < e[0]: # 간선의 중복을 방지하기 위한 사전순 비교
                eList.append([v, e[0], e[1]])

    eList.sort(key=lambda e: e[2], reverse=True) # 가중치 기준 내림차순 -> pop을 위해서 역순순

def find(vNum):
    while vertices[vNum] != -1:
        vNum = vertices[vNum]

    return vNum

def union(vNum1, vNum2):
    vertices[vNum2] = vNum1

def kruskal():
    # 최우선은 간선 정렬
    edgeSort()

    eCnt = 0 # 간선 갯수
    vCnt = len(vertices) # 정점의 갯수

    # 종료 조건 -> 간선 : 정점수- 1
    while eCnt < vCnt - 1: 
        e = eList.pop() # 'A', 'B', 29 ... 

        # 사이클이 생기지 않는지 확인
        vNum1 = find(ord(e[0]) - 65)
        vNum2 = find(ord(e[1]) - 65)

        if vNum1 != vNum2: # 부모가 다르면
            eCnt += 1
            print('%d. [%s%s %d]' %(eCnt, e[0], e[1], e[2]))
            union(vNum1, vNum2)

if __name__ == "__main__":
    kruskal()