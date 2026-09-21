class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        if isinstance(data, int) and data % 3 == 0:
            self.stack.append(data)
            print(data, "added to stack.")
        else:
            print("Only integers divisible by 3 are allowed.")

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            print("Stack is empty!")

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            print("Stack is empty!")

    def display(self):
        print("Stack:", self.stack)


s = Stack()

s.push(3)
s.push(6)
s.push(10) 
s.push(15)

s.display()
