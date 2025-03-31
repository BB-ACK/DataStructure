class ArrayStack:
    # 생성자
    def __init__(self, capacity = 30):
        self.capacity = capacity
        self.top = -1
        self.array = [None] * capacity

    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.capacity + 1
    
    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = e
        else:
            print("Overflow.")

    def pop(self):
        if not self.isEmpty():
            e = self.array[self.top]
            self.top -= 1
            return e
        else:
            print("Underflow.")

    # pop과 달리 원소를 제거하지 않음 
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            print("Underflow.")

    def display(self):
        print()
        for i in range(self.top, -1, -1):
            print(" | %s |" % (self.array[i]))
            # print("  --- ")
        print()

if __name__ == "__main__":
    s = ArrayStack()
    data = ["a", "v", "d", "sda", "asda", "qwe"]

    for item in data:
        s.push(item)
    
    s.display()
    print(s.peek())
