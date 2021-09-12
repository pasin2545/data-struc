class SinglyLinkedListNoDummy :
    class Node :
        def __init__(self, data, next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
        
    def __init__(self):                
            self.head = None
            self.size = 0
            
    def __str__(self):    # แสดงข้อมูลทุกตัวใน linked list
        s = 'linked data : '
        p = self.head
        while p != None :
            s += str(p.data) + ' '
            p = p.next
        return s
        
    def __len__(self) :               # เพิ่ม เมื่อ เติมข้อมูล  ลด เมื่อ นำข้อมูลออก
        return self.size         
            
    def isEmpty(self) :               # ตรวจสอบว่ามีข้อมูลใน linked list ไหม
        return self.size == 0
        
    def indexOf(self,data) :          # หา อินเด็กของข้อมูลว่าอยู่ที่ตำแหน่งใด
        p = self.head
        for i in range(len(self)) :
            if p.data == data :
                return i
            p = p.next
        return -1
            
    def isIn(self,data) :             # ตรวจสอบว่าใน linked list นี้ มีข้อมูลตัวนี้ไหม
        return self.indexOf(data) >= 0
    
    def nodeAt(self,i) :              # หาค่าตำแหน่งของโหนด เทียบกับ อินเด็กซ์
        p = self.head
        for j in range(0,i) :
            p = p.next
        return p
    
    def append(self,data):            # เพิ่ม ข้อมูล ไปที่ด้านท้ายของ linked list
        if self.head == None :
            self.head = self.Node(data,None)
            self.size += 1
        else :
            self.insertAfter(len(self)-1,data)   #len(self) = จำนวนสมาชิก - 1 คือ index
    
    def insertAfter(self,i,data) :       #มีสายข้อมูลอยู่แล้ว
        q = self.nodeAt(i)
        p = self.Node(data)
        p.next = q.next
        q.next = p
        #q.next = self.Node(data,q.next)
        self.size += 1
    
    def deleteAfter(self,i) :            #มีสายข้อมูลอยู่แล้ว
        if self.size > 0 :
            q = self.nodeAt(i)
            q.next = q.next.next
            self.size -= 1
    
    def delete(self,i) :                 #ลบข้อมูลที่ อินเด็กซ์ที่กำหนด
        if i == 0 and self.size > 0 :    #ลบตัวแรก
            self.head = self.head.next
            self.size -= 1
        else :
            self.deleteAfter(i-1)          #ลบตัวก่อนหน้า
        
    def changehead(self,k,i):
        if i > k and self.size >0:
            self.insertAfter(len(self)-1,self.head.data)
            self.head = self.head.next
            self.size -= 1

    def prit(self):
        s='After : '
        p = self.head
        for i in range(int(self.__len__())):
            if i+1 != int(self.__len__()) :
                s += str(p.data) + ' <- '
                p = p.next
            else:
                s += str(p.data)
        return s




L1 = SinglyLinkedListNoDummy()

print(" *** Locomotive ***")
inp = input("Enter Input : ").split()
print("Before : ",end='')
for i in inp:
    L1.append(i)
    if i != inp[-1]:
        print(i,"<-",end=' ')
    else:
        print(i)

j=0
#print(L1)
#print(L1.indexOf('0'))
for i in range(len(L1)):
    if L1.indexOf('0') == i:
        for k in range(int(i)):
            L1.changehead(k,i)
        break
        #print("1")
print(L1.prit())


