class Stack:

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

### Enter Your Code Here ###
combo =0
inp = input('Enter Input : ').split()
S = Stack()
for i in inp:
    S.push(i)
    if S.size()>=3:
        if S.items[-1] == S.items[-2] and S.items[-2] == S.items[-3]:
            S.pop()
            S.pop()
            S.pop()
            combo +=1

print(S.size())

num = ''
if S.isEmpty() ==0:
    for i in S.items[::-1]:
        num+=i
    print(num)
    
if S.isEmpty() == 1:
    print("Empty")
if combo >=2:
        print("Combo : "+str(combo)+" ! ! !")




### Enter Your Code Here ###

