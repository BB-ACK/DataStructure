# 진행괴정을 확인하기 위한 함수
def printStep(A, idx):
    print("       Step %d : " %idx, end="")
    print(A)


def insertionSort(A):
    n = len(A)

    for i in range(1, n):
        key = A[i] # 내가 지금 순서를 맞출 요소
        j = i-1 # 그 전 값부터 비교

        while j >= 0 and A[j] > key:
            A[j + 1] = A[j] # 한 칸씩 미는 과정
            j -= 1

        A[j + 1] = key
        printStep(A, i)

if __name__ == "__main__":
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    
    L = list(data)
    print("Befor         :", L)

    insertionSort(L)
    print("InsertionSort :", L)