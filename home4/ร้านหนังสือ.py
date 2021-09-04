class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def enQueue(self,i):
        self.items.append(i)

    def deQueue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return -1
    
    def peek(self):
        if not self.isEmpty():
            return self.items[0]
        return -1
    

Q = Queue()
Keep1 = []
Keep2 = []
keep1 =[]
keep2 = []
check = 0
get = ''
gotit =0

inp = input("Enter Input : ").split("/")

kk = inp[0].split()
get = inp[1].split(',')
for g in kk:
    Q.enQueue(g)
for i in get:
    keep2.append(i)
#print(Q.items)

for i in keep2:
    if len(i) > 1:
        j = i.split()
        if j[0] == 'E':
            Q.enQueue(j[1])
    elif i == 'D':
        Q.deQueue()


for i in range(0,len(Q.items)):
        for j in range(i+1,len(Q.items)):
            if Q.items[i] == Q.items[j]:
                gotit = 1

#print(Q.items)

if gotit == 0:
    print("NO Duplicate")
else:
    print("Duplicate")

#print(Keep1)
#print(Keep2)'''

