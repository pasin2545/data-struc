class Stack:

    ### Enter Your Code Here ###
    def __init__(self):
        self.items = []

    def push(self, i):
        self.items.append(i)

    def pop(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        if(len(self.items)==0):
            return 1
        else:
            return 0

S = Stack()


inp = input('Enter Input : ').split(',')

### Enter Your Code Here ###