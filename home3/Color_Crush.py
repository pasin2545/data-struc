class Stack:

    def __init__(self):
        self.items = []

    def push(self, value):
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
    '''def Baam(self,m,k):
        if m.items[k] == m.items[k-1] and m.items[k] == m.items[k-2]:
            m.items[k] = -99999
            m.items[k-1] = -99999
            m.items[k-2] = -99999
            m.items.remove(-99999)'''


inp = input('Enter Input : ').split()

S = Stack()

### Enter Your Code Here ###

for i in inp:
    S.push(i)
    for i 

'''for i in range(len(inp)):
    if i!=0 and i!=1:
        S.Baam(S,i)'''

print(S.items)
#print(S.size())

### Enter Your Code Here ###

