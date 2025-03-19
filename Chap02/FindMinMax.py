import random

def findMinMax(A):
    min = max = A[0] # 초기값 설정

    for i in range(1, len(A)):
        if min > A[i]:
            min = A[i]

        if max < A[i]:
            max = A[i]

    return (min, max)

# 파일 자체 내에서 실행시킨 경우에만 실행, 즉 모듈로 사용할 때는 X
if __name__ == '__main__':
    A = []
    for _ in range(10):
        A.append(random.randint(1, 100))

    print(A)
    print(findMinMax(A))