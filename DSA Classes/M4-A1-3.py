class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

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

    def clear(self):
        self.stack.clear()
        print("Stack has been cleared.")


s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

s.clear()

s.display()