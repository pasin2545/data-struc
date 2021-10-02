class QueueReal:
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

class QueueMirror:
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

class KeepM: 
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
    
class KeepR: 
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

class BombM: 


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

class KeepQR: 

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
    
    def Clear(self):
        return self.items.clear()

class notsumQR: 

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
    
    def Clear(self):
        return self.items.clear()

class notsumQM: 

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
    
    def Clear(self):
        return self.items.clear()

class keerchecker: 

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
    
    def Clear(self):
        return self.items.clear()

class keercheckerM: 

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
    
    def Clear(self):
        return self.items.clear()



BM = BombM()
KM = KeepM()
KR = KeepR()
QR = QueueReal()
QM = QueueMirror()
keepQR = KeepQR()
notQR = notsumQR()
notQM = notsumQM()
checker = keerchecker()
checkerM = keercheckerM()
keep =[]
keepM = []
comboR = 0
comboM = 0
failinter =0
check = 0
checkM = 1

inp = input("Enter Input (Normal, Mirror) : ").split()

kk = inp[0]
pp = inp[1]

for i in pp:
    keepM.append(i)
while checkM !=0:
#for i in range(2):
    for i in keepM[::-1]:
        QM.enQueue(i)
        if QM.size()>=3:
            if QM.items[-1] == QM.items[-2] and QM.items[-2] == QM.items[-3]:
                #print("***1***")
                BM.enQueue(QM.items[0])
                QM.deQueue()
                QM.deQueue()
                QM.deQueue()
                #combo +=1
                comboM +=1
            else:
                #print("***2***")
                KM.enQueue(QM.items[0])
                QM.deQueue()
            
    if QM.size() <=2:
        #print("***1.2***")
        for l in QM.items:
            notQM.enQueue(l)
        for p in notQM.items:
            KM.enQueue(p)
            QM.deQueue()
        notQM.Clear()
    checkM = 0
    keepM = []

    for i in KM.items:
        keepM.append(i)
        if len(keepM)>=3:
            if keepM[-1] == keepM[-2] and keepM[-2] == keepM[-3]:
                checkM = 1
                KM.deQueue()
                KM.deQueue()
                KM.deQueue()
        #print(len(keepM))

    '''print(BM.items)
    print(KM.items)
    print(QM.items)
    print(keepM)'''

for i in kk:
    checker.enQueue(i)

check = 1
while check != 0:
    #print("lol")
    for i in checker.items:
        #print("---",i)
        QR.enQueue(i)
        if QR.size()>=3:
            if QR.items[-1] == QR.items[-2] and QR.items[-2] == QR.items[-3]:
                #print("***3***")
                keep.append(QR.items[0])
                QR.deQueue()
                if BM.size() > 0:
                    #print("***4***")
                    QR.enQueue(BM.items[0])
                    BM.deQueue()
                QR.enQueue(keep[0])
                keep = []
                #print("///",QR.items)
                for j in QR.items:
                    keepQR.enQueue(j)
                if QR.items[0] == QR.items[1] and QR.items[1] == QR.items[2]:
                    if QR.size()>=4:
                        #print("***5***")
                        #KR.enQueue(QR.items[0])
                        QR.deQueue()
                        QR.deQueue()
                        QR.deQueue()
                        failinter += 1
                        '''print(BM.items)
                        print(KR.items)
                        print(QR.items)'''
                        #comboR +=1
                    else :
                        #print("***5.5***")
                        QR.deQueue()
                        QR.deQueue()
                        QR.deQueue()
                        '''print(BM.items)
                        print(KR.items)
                        print(QR.items)'''
                        comboR +=1
                else:
                    #print("***6***")
                    for k in keepQR.items:
                        #print(keepQR.items)
                        #print(QR.items)
                        #print(k)
                        KR.enQueue(k)
                        QR.deQueue()
                    #print(KR.items)
                #combo +=1
                keepQR.Clear()
            else:
                #print("***7***")
                for l in QR.items:
                    notQR.enQueue(l)
                KR.enQueue(notQR.items[0])
                QR.deQueue()
                notQR.Clear()
                '''print(BM.items)
                print(KR.items)
                print(QR.items)'''
    if QR.size() <=2:
        #print("***7.2***")
            #print(checker.items[-1])
        for l in QR.items:
            notQR.enQueue(l)
        for p in notQR.items:
            KR.enQueue(p)
            QR.deQueue()
        notQR.Clear()
        '''print(BM.items)
        print(KR.items)
        print(QR.items)'''
    check = 0
    checker.Clear()
    for i in KR.items:
        checker.enQueue(i)
        if checker.size()>=3:
            if checker.items[-1] == checker.items[-2] and checker.items[-2] == checker.items[-3]:
                check = 1
                KR.deQueue()
                KR.deQueue()
                KR.deQueue()

#print(KR.items)
#print(KM.items)
showR = ''
showM = ''
print("NORMAL :")
if KR.size() > 0:
    print(KR.size())
    for i in KR.items[::-1]:
        showR+=i
    print(showR)
else:
    print("0")
    print("Empty")
print(comboR,"Explosive(s) ! ! ! (NORMAL)")
if failinter >=1:
    print("Failed Interrupted",failinter,"Bomb(s)")
print("------------MIRROR------------")
print(": RORRIM")
if KM.size() > 0:
    print(KM.size())
    for i in KM.items[::-1]:
        showM+=i
    print(showM)
else:
    print("0")
    print("ytpmE")
print("(RORRIM) ! ! ! (s)evisolpxE",comboM)


