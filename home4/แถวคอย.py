class Queue1:
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

class Queue2:
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

class Queue3:
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

Q1 = Queue1()
Q2 = Queue2()
Q3 = Queue3()
x = 0
Keep = []
k = 0
check1 = 0
chk1 = 0
check2 = 0
chk2 = 0
get = ''
inp = input("Enter people and time : ").split(' ')

for i in inp:
    Keep.append(i)
#print(Keep)
for j in Keep[0]:
    Q1.enQueue(j)
#print(int(Keep[1]))
#print(Q1.items)
k = int(Keep[1])
for j in range(k):
    if Q2.size()>=1:
        chk1+=1
        #print("1")
    if Q3.size()>=1:
        chk2+=1
        #print("2")
    if Q1.isEmpty() == 0 : 
        check1+=1           #เช็คเข้าเเถว 1
        get = Q1.items[0]
        Q1.deQueue()
        #print("3")
    if chk1 == 3:
        Q2.deQueue()
        chk1 =0 
        check1 -= 1
        #print("4")   
    if Q2.size() >=0 and Q2.size()<5 and Q1.isEmpty() == 0:          #เเถว 1
        Q2.enQueue(get)
        #print("6")
    if check1 > 5:
        if Q3.size() >= 0 and Q3.size() <5:
            Q3.enQueue(get)
            #print("7")
            check1 -= 1
    if chk2 ==2:
        Q3.deQueue()
        chk2 = 0
        #print("8")
    print(j+1,Q1.items,Q2.items,Q3.items)
                
                
        
            
            



        #print(i)

