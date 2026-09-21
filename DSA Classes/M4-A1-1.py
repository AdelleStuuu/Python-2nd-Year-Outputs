class Stack:
    def __init__(self):
        self.stack = []
        self.max_size = 5

    def push(self, data):
        if len(self.stack) < self.max_size:
            self.stack.append(data)
            print(data, "added to stack.")
        else:
            print("Stack is full! Maximum of 5 items only.")

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

s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.push(60)  

s.display()
