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

for i in inp:
    if len(i) > 1:
        i = i.split()
        if i[0] == 'A':
            for j in range(S.size()):
                #print("1")
                if int(i[1]) > int(S.items[-1]) or int(i[1]) == int(S.items[-1]) : 
                    #print("**2**")
                    #print(S.items[-1])
                    S.pop()
                    

            S.push(i[1])
            #print(S.items)
    if i == 'B':
        print(S.size())