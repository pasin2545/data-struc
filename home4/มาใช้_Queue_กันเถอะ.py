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
show = ''
showend = ''
sam = []
havede =0
haveen = 0

inp = input("Enter Input : ").split(',')

for i in inp:
    
    if len(i)>1:
        i = i.split()
        if i[0] == 'E':
            haveen +=1
            Q.enQueue(i[1])
            for j in Q.items:
                if j != Q.items[-1]:
                    show += j
                    show += ", "
                else:
                    show += j
            print(show)
            show = ''
            #print(Q.items)
    if i == 'D':
        havede +=1
        for j in Q.items:
                if j != Q.items[-1] and j != Q.items[0]:
                    show += j
                    show += ", "
                elif j != Q.items[0]:
                    show += j
        if Q.isEmpty()==0:
            sam.append(Q.items[0])
            Q.deQueue()
            if Q.isEmpty()==1:
                print(sam[-1],"<-","Empty")
            else:
                print(sam[-1],"<-",show)
            show = ''
        elif Q.isEmpty()==1:
            print("Empty")
            show =''
        
        
if Q.isEmpty()==1 :
    if haveen >= 1:
        for j in sam:
            if j != sam[-1]:
                showend+= j
                showend += ", "
            else:
                showend += j
        print(showend,":","Empty")
    elif haveen ==0:
        print("Empty",":","Empty")
else:
    if havede >= 1:
        for j in sam:
            if j != sam[-1]:
                showend+= j
                showend += ", "
            else:
                showend += j
        for j in Q.items:
            if j != Q.items[-1]:
                show += j
                show += ", "
            else:
                show += j
        print(showend,":",show)
    elif havede == 0:
        for j in Q.items:
            if j != Q.items[-1]:
                show += j
                show += ", "
            else:
                show += j
        print("Empty",":",show)
        



