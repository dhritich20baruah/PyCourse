# USING LIST AS A STACK
s = []
s.append('http://www.cnn.com/')
s.append('https://www.cnn.com/world')
s.append('https://www.cnn.com/india')
s.append('https://www.cnn.com/china')

print(s.pop())
print(s)

# USING DEQUE AS A STACK
from collections import deque
stack = deque()
# print(dir(stack))
stack.append('https://www.cnn.com/')
print(stack)


stack.append('https://www.cnn.com/world')
print(stack)

stack.append("https://www.cnn.com/india")
stack.append("https://www.cnn.com/china")
print(stack)

#IMPLEMENT STACK CLASS USING A DEQUE
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)

s = Stack()
s.push(5)

print(s.is_empty())