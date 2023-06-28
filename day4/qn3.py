# Stack
class Stack:
    def __init__(self):
        self.stack = []
        pass

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is empty")


n = Stack()

n.push(1)
n.push(2)
n.push(3)

print(n.is_empty())
print(n.pop())

# USE CASE


def match_parenthesis(string):
    n.stack = []
    opening_brackets = '([{'
    closing_brackets = ')}]'

    for i, char in enumerate(string):
        if char in opening_brackets:
            n.stack.push(char)
        elif char in closing_brackets:
            n.stack.peek
