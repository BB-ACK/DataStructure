import random

# 순차 탐색
def seqSearch(A, key):
    n = len(A)

    for i in range(n):
        if A[i] == key:
            return i
    return None

# 반복문을 통한 이진 탐색
def iBinaraySearch(A, Key):
    low = 0
    high = len(A) - 1

    while(low <= high):
        middle = (low + high) // 2 # 중앙 인덱스

        if key == A[middle]:
            return middle
        elif key < A[middle]: # 더 작기에 high값을 조절
            high = middle - 1
        else:                 # 더 크다면 low값을 조절
            low = middle + 1

    return -1

# 이진 탐색을 위한 삽입정렬
def insertionSort(A):
    n = len(A)

    for i in range(1, n):
        key = A[i]
        j = i - 1

        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        
        A[j+1] = key

if __name__ == "__main__":
    A = []
    for i in range(15):
        A.append(random.randint(1, 100))
    
    insertionSort(A)
    print("A[] = ", A)

    key = int(input('Input Search Key : '))
    # idx = seqSearch(A, key)
    idx = iBinaraySearch(A, key)


    print()
    if idx != -1:
        print("Find at pos %d." %idx)
    else:
        print("No key to find.")
    