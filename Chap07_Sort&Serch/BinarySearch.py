import random

# 순차 탐색
def seqSearch(A, key):
    n = len(A)

    for i in range(n):
        if A[i] == key:
            return i
    return None


if __name_ == "__main__":
    A = []
    for i in range(15):
        A.append(random.randint(1, 100))
    
    print("A[] = ", A)

    key = int(input('Input Search Key : '))
    idx = seqSearch(A, key)

    print()
    if idx != -1:
        print("Find at pos %d." %idx)
    else:
        print("No key to find.")
    