class StackK:
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
    
    def Del(self,m,k):
        for i in range(m.size()):
            if (int(k) == int(m.items[i])):
                if m.items[i]!=100000:
                    print("Delete = "+k)
                m.items[i] =100000
        if 100000 in m.items:
            m.items.remove(100000)
        if m.isEmpty() == 1:
            print("-1")

    def LD(self,m,k):
        for i in range(m.size()-1,-1,-1):
            if (int(k) > int(m.items[i])):
                if m.items[i]!=100000:
                    print("Delete = "+ str(m.items[i]) + " Because " + str(m.items[i]) + " is less than " + str(k))
                m.items[i] = 100000
        if 100000 in m.items:
            m.items.remove(100000)
        if m.isEmpty() == 1:
            print("-1")
    
    def MD(self,m,k):
        for i in range(m.size()-1,-1,-1):
            if (int(k) < int(m.items[i])):
                if m.items[i]!=100000:
                    
                    print("Delete = "+ str(m.items[i]) + " Because " + str(m.items[i]) + " is more than " + str(k))
                m.items[i] = 100000
        if 10000 in m.items:
            m.items.remove(100000)
        if m.isEmpty() == 1:
            print("-1")


stackK = StackK()
getin = input("Enter Input : ").split(",")

for i in getin:
    if len(i)>1:
        i = i.split()
        if i[0] == 'A':
            stackK.push(i[1])
            print("Add =",i[1])
        if i[0] == 'D':
            stackK.Del(stackK,i[1])
        if i[0] == 'LD':
            stackK.LD(stackK,i[1])
        if i[0] == 'MD':
            stackK.MD(stackK,i[1])
    elif i == 'P'and stackK.size()>1:
        print("Pop =",stackK.peek())
        stackK.pop()
    elif i == 'P' and stackK.isEmpty()==1:
        print("-1")

num = ''
j=0
for i in stackK.items:
    j+=1
    k = stackK.size()
    if i != 100000:
        num += i
        if j != k:
            num += ", "
print("Value in Stack ="+" ["+num+"]")
