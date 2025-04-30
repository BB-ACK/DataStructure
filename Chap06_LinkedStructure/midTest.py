class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class StackType:
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        return self.top == None

    def push(self, data):
        node = Node(data, self.top)
        self.top = node

    def pop(self):
        if not self.isEmpty():
            p = self.top
            self.top = p.next
            return p.data
        else:
            pass

    def peek(self):
        if not self.isEmpty():
            return self.top.data
        else: pass

    def printList(self):
        p = self.top

        while p != None:
            print("[%s] -> " % p.data, end="")
            p = p.next
        
        print('\b\b\b\b ')

    def sortedList(self, data):
        if(self.isEmpty() or data < self.peek()):
            self.push(data)
        else:
            temp = self.pop()
            self.sortedList(data)
            self.push(temp)


if __name__ == "__main__":
    S = StackType()

    input = ['A', 'C', 'B', 'F', 'D', 'C']

    for i in range(6):
        S.sortedList(input[i])
        S.printList()