from ArrayStack import ArrayStack

map = [
    ['1', '1', '1', '1', '1', '1'],
    ['e', '0', '0', '0', '0', '1'],
    ['1', '0', '1', '0', '1', '1'],
    ['1', '1', '1', '0', '0', 'x'],
    ['1', '1', '1', '0', '1', '1'],
    ['1', '1', '1', '1', '1', '1']
]

SIZE = 6

def isValidPosition(row, col):
    if 0 <= row < SIZE and 0 <= col < SIZE:
        if map[row][col] == "0" or map[row][col] == "x":
            return True
        
    return False

def DFS():
    print("DFS: ")
    S = ArrayStack()
    S.push((1, 0)) # 시작 지점

    while not S.isEmpty():
        pos = S.pop()
        (r, c) = pos
        print(pos, end= " -> ")

        if(map[r][c] == "x"):
            return True

        else:
            map[r][c] = "." # 방문표시
            if isValidPosition(r - 1, c): S.push((r - 1, c))
            if isValidPosition(r + 1, c): S.push((r + 1, c))
            if isValidPosition(r, c - 1): S.push((r, c - 1))
            if isValidPosition(r, c + 1): S.push((r, c + 1))

        print(S.array[S.top::-1])

    return False

if __name__ == "__main__":
    result = DFS()

    if result:
        print("Succcess")
    else:
        print("Fail")