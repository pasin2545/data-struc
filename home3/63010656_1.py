class StackV:
    def __init__(self):
        self.items = []

    def push(self, i):
        self.items.append(i)

    def pop(self):
        self.items.pop()

    def isEmpty(self):
        if(len(self.items)==0):
            return 1
        else:
            return 0
    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]


class StackS:
    def __init__(self):
        self.items = []

    def push(self, i):
        self.items.append(i)

    def pop(self):
        self.items.pop()

    def isEmpty(self):
        if(len(self.items)==0):
            return 1
        else:
            return 0
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[-1]
    def peek2(self):
        return self.items[-2]

stackV = StackV()
stackS = StackS()

getin = input("Enter Input : ").split(",")
j = 0
for i in getin:
    if len(i) > 1:
        i = i.split()
        if i[0] == 'A':
            if j == 0 and stackS.isEmpty()==1:
                stackS.push(0)
            j +=1
            stackS.push(j)
            stackV.push(i[1])
            print("Add =",stackV.peek(),"and Size =",stackS.peek())
    elif i == 'P'and stackS.size()>1:
        j-=1
        print("Pop =",stackV.peek(),"and Index =",stackS.peek2())
        stackS.pop()
        stackV.pop()
        if stackV.isEmpty()==1 and stackS.isEmpty() ==0:
            stackS.pop()
    elif i == 'P' and stackS.isEmpty()==1:
        print("-1")



Show = ''
if stackV.isEmpty()==0:
    for i in range(len(stackV.items)):
        Show += str(stackV.items[i])
        Show += " "
    print("Value in Stack = "+Show)
elif stackV.isEmpty()==1:
    print("Value in Stack = Empty")