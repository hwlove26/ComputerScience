class Stack:
    def __init__(self, max):
        self.stack = []
        self.max = max

    def isEmpty(self):
        #check if the stack is empty
        return len(self.stack) == 0

    def push(self, value):
        #add value to stack
        if not self.isFull():
            self.stack.append(value)
        else:
            raise IndexError('Stack is full')

    def pop(self):
        #remove value from stack and remove
        if not self.isEmpty():
            return self.stack.pop()
        else:
            raise IndexError('Stack is empty')

    def peek(self):
        #return the top value without removing it
        if not self.isEmpty():
            return self.stack[-1]
        else:
            raise IndexError('Stack is empty')

    def size(self):
        return len(self.stack)

    def isFull(self):
        return len(self.stack) == self.max


def main():
    stack = Stack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)

    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.isEmpty())

if __name__ == '__main__':
    main()