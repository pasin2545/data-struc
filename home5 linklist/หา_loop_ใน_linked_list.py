class SinglyLinkedListNoDummy :
    class Node :
        def __init__(self, value, next = None) :
            self.value = value
            if next is None :
                self.next = None
            else :
                self.next = next
        
    def __init__(self):                
            self.head = None
            self.size = 0
            
    def __str__(self):    # แสดงข้อมูลทุกตัวใน linked list
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value)
        if cur.next != None :
            s += "->"
        while cur.next != None:
            s += str(cur.next.value)
            if cur.next.next != None :
                s += "->"
            cur = cur.next
        return s
        
    def __len__(self) :               # เพิ่ม เมื่อ เติมข้อมูล  ลด เมื่อ นำข้อมูลออก
        return self.size         
            
    def isEmpty(self) :               # ตรวจสอบว่ามีข้อมูลใน linked list ไหม
        return self.head == None
        
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
        if self.isEmpty() :
            self.head = self.Node(data)
            self.size += 1
        else :
            t = self.head
            while t.next :
                t = t.next
            t.next = self.Node(data)
            self.size += 1
    
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
    
    def changetar(self,pos,pos2):
        n1 = self.Node(None)
        n2 = self.Node(None)
        itr = self.head
        s = "Set node.next complete!, index:value = " + str(pos) + ":"
        while itr :
            if pos == 0 :
                n1 = itr
                s += str(n1.value) + " -> " + str(pos2) + ":"
            pos -= 1
            itr = itr.next
        itr = self.head
        while itr :
            if pos2 == 0 :
                n2 = itr
                s += str(n2.value)
            pos2 -= 1
            itr = itr.next
        n1.next = n2
        return s

    def isLoop(self) :
        if self.isEmpty() :
            return False
        idList = []
        itr = self.head
        while itr.next :
            if id(itr) in idList :
                return True
            idList.append(id(itr))
            itr = itr.next
        return False

check = 0
L = SinglyLinkedListNoDummy()

inp = input("Enter input : ").split(',')

for i in inp:
    i = i.split(' ')
    if i[0] == 'A':
        L.append(str(i[1]))
        print(L)

    if i[0] == 'S':
        m = i[1].split(':')
        if L.isEmpty() :
            print("Error! {list is empty}")
        elif int(L.__len__()) < int(m[0])+1 and L.isEmpty() == 0:
            print("Error! {index not in length}:",str(m[0]))
        elif int(L.__len__()) < int(m[1])+1 and L.isEmpty() == 0:
            L.append(str(m[1]))
            print("index not in length, append :",str(m[1]))
        else:
            print(L.changetar(int(m[0]),int(m[1])))

if L.isLoop() :
    print("Found Loop")
else :
    print("No Loop")
    print(L)


                
            
            