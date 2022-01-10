class Stack:
    def __init__(self, limit=10):
        self.stk = []
        self.limit = limit

    def isEmpty(self):
        return len(self.stk) <= 0
        pass

    def push(self, item):
        if len(self.stk) >= self.limit:
            print("Stack Overflow!")
        else:
            self.stk.append(item)
            print("Stack after Push", self.stk)

    def pop(self):
        if len(self.stk) <= 0:
            print("Stack Underflow!")
            return 0
        else:
            return self.stk.pop()

    def peek(self):
        if len(self.stk) <= 0:
            print('Stack Underflow!')
            return 0
        else:
            return self.stk[-1]

    def size(self):
        return len(self.stk)


if __name__ == '__main__':
    our_stack = Stack(5)
    our_stack.push(10)
    our_stack.push(20)
    our_stack.push(30)
    our_stack.push(40)
    our_stack.push(50)
    print(our_stack.peek())
    print(our_stack.pop())
    print(our_stack.peek())
    print(our_stack.pop())
    print(our_stack.peek())
    print(our_stack.pop())
    print(our_stack.size())
