class DoublyLinkedListNoDummy :
    class Node :
        def __init__(self,data,prev = None,next = None) :
            self.data = data

            if prev is None :
                self.prev = None
            else :
                self.prev = prev

            if next is None :
                self.next = None
            else :
                self.next = next
        
    def __init__(self):                
            self.head = None
            self.size = 0
            
    def __str__(self):
        s = 'linked data : '
        p = self.head
        for i in range(len(self)) :
            s += str(p.data) + ' '
            p = p.next
        return s

    def __len__(self) :
        return self.size
        
    def isEmpty(self) :
        return self.size == 0
    
    def indexOf(self,data) :
        q = self.head
        for i in range(len(self)) :
            if q.data == data :
                return i
            q = q.next
        return -1
    
    def isIn(self,data) :
        return self.indexOf(data) >= 0
    
    def nodeAt(self,i) :
        p = self.head
        for j in range(0,i) :
            p = p.next
        return p
    
    def insert(self,q,data) :
            p = q.prev
            x = self.Node(data,p,q)
            p.next = q.prev = x
            self.size += 1
        
    def append(self,data) :
        if self.head == None :
            self.head = self.Node(data)
            self.size += 1
        else :
            q = self.nodeAt(len(self)-1)
            x = self.Node(data,q,None)
            q.next = x
            print(q.next)
            self.size += 1
    
    def removeNode(self,q) :
        p = q.prev
        x = q.next
        p.next = x
        x.prev = p
        self.size -= 1
        
    def delete(self,i) :
        if i == 0 :
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
        elif i == len(self) - 1 :
            x = self.nodeAt(i)
            p = x.prev
            p.next = None
            print("****",p.prev)
            self.size -= 1
        else:
            self.removeNode(self.nodeAt(i))


l2 = DoublyLinkedListNoDummy()
l2.append('a')
print(l2)
l2.append('b')
print(l2)
l2.append('c')
l2.append('d')
l2.append('e')
print(l2)
l2.append('z')
print(l2)
l2.delete(0)
print(l2)
#print(l2.indexOf('c'))
l2.insert(0x000001FFB47ACFD0,'A')
print(l2)
l2.delete(3)
print(l2)