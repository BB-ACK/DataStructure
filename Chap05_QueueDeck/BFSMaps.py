from CircularQueue import CircularQueue

map = [
['1', '1', '1', '1', '1', '1'],
['e', '0', '1', '0', '0', '1'],
['1', '0', '0', '0', '1', '1'],
['1', '0', '1', '0', '1', '1'],
['1', '0', '1', '0', '0', 'x'],
['1', '1', '1', '1', '1', '1']
]

SIZE = 6

def isValidPosition(row, col):
    if 0 <= row < SIZE and 0 <= col < SIZE:
        if map[row][col] == "0" or map[row][col] == "x":
            return True
        
    return False

def BFS():
    print("DFS: ")
    Q = CircularQueue()
    Q.enqueue((1, 0)) # 시작 지점

    while not Q.isEmpty():
        pos = Q.dequeue()
        (r, c) = pos
        print(pos, end= " -> ")

        if(map[r][c] == "x"):
            return True

        else:
            map[r][c] = "." # 방문표시
            if isValidPosition(r - 1, c): Q.enqueue((r - 1, c))
            if isValidPosition(r + 1, c): Q.enqueue((r + 1, c))
            if isValidPosition(r, c - 1): Q.enqueue((r, c - 1))
            if isValidPosition(r, c + 1): Q.enqueue((r, c + 1))

        print(Q.array[Q.front + 1:Q.rear + 1])

    return False

if __name__ == "__main__":
    result = BFS()

    if result:
        print("Succcess")
    else:
        print("Fail")