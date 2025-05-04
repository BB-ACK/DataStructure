# 진행괴정을 확인하기 위한 함수
def printStep(A, idx):
    print("       Step %d : " %idx, end="")
    print(A)


def BubbleSort(A):
    n = len(A)

    for i in range(n-1): # 전체 반복 범위
        flag = False 
        
        for j in range(1, n-i): # 맨 뒤부터 요소가 정리되기에 점점 줄어듦
            if(A[j-1] > A[j]): # 붙어 있는 앞 뒤 요소를 비교
                A[j-1], A[j] = A[j], A[j-1]
                flag = True

        if not flag: # 중간에 교체 연산이 이루어지지 않았다면 다음에도 교체할 필요가 없음
            break 

        printStep(A, i)


if __name__ == "__main__":
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    
    L = list(data)
    print("Befor         :", L)

    BubbleSort(L)
    print("BubbleSort    :", L)