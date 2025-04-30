def printStep(A, idx):
    print("   Step %d : " % idx, end="")
    print(A)

def selectionSort(A):
    n = len(A)

    for i in range(n-1):
        minIdx = i
        for j in range(i+1, n):
            if A[j] < A[minIdx]:
                minIdx = j
            
        A[i], A[minIdx] = A[minIdx], A[i]
        printStep(A, i+1)

if __name__ == "__main__":
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]

    L = list(data)
    print("Befor     :", L)

    selectionSort(L)
    print("After     :", L)
