capacity = 100 # 용량의 사이즈를 넉넉히
size = 0 # 아직 아무것도 집어넣지 않아서 0
array = [None] * capacity # 0보다는 진짜 의미없는 값인 None사용

def isEmpty():
    return size == 0

def isFull():
    return size == capacity

# 배열에 값을 넣는 함수
def insert(pos, e):
    global size
    if not isFull() and 0 <= pos <= size:
        for i in range(size, pos, -1):
            array[i] = array[i-1]
        array[pos] = e
        size += 1
    else:
        print("Overflow or Invalid Position.")

# 배열의 값을 삭제하는 함수
def delete(pos):
    global size
    if not isEmpty() and 0 <= pos < size:
        e = array[pos]
        for i in range(pos, size-1):
            array[i] = array[i-1]
        size -= 1
        return e
    else:
        print("Underflow or Invalid Position.")

def getEntry(pos):
    if 0 <= pos < size:
        return array[pos]
    else:
        return None


if __name__ == "__main__":
    insert(0, 'A')
    insert(1, 'B')
    insert(1, 'C')
    print(array[0:size])

    print("[%c] is deleted." % delete(2))
    print(array[0:size])
