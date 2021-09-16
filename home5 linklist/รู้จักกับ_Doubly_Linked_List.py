class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.Size = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        #Code Here
        if self.head == None :
            self.head = Node(item)
            self.Size += 1
        else :
            self.insertapp(self.Size-1,item) 
            
    def insertapp(self, pos, item):
        q = self.nodeAtnext(pos)
        p = Node(item)
        p.next = None
        q.next = p
        p.previous = q
        self.tail = p
        #q.next = self.Node(data,q.next)
        self.Size += 1

    def addHead(self, item):
        #Code Here
        if self.Size == 0:
            if self.head == None :
                self.head = Node(item)
                self.tail = self.head
                self.Size += 1
        else :
            self.inserthead(0,item)

    def inserthead(self, pos, item):
        #Code Here
        q = self.nodeAtnext(pos)
        p = Node(item)
        p.previous = None
        p.next = q
        q.previous = p
        self.head = p
        self.Size += 1

    def insert(self, pos, item):
        #Code Here
        if(pos<0):
            check=pos*-1
        else:
            check=pos
        if self.Size == 0:
            if self.head == None :
                self.head = Node(item)
                self.tail = self.head
                self.Size += 1
                return
            else :
                q = self.nodeAtnext(self.Size-1)
                x = Node(item)
                x.previous = q
                x.next = None
                q.next = x
                self.Size += 1
                return
        if(self.Size>= check):
            if pos>0:
                if(self.Size>pos):
                    islen=pos-1
                    node=self.head
                    for i in range(islen):
                        node=node.next
                        ISnode=Node(item)
                        Cnode=node.next
                        node.next=ISnode
                        ISnode.next=Cnode
                        ISnode.previous=node
                        Cnode.previous=ISnode
                else:
                    Innode=Node(item)
                    Innode.previous=self.tail
                    self.tail.next = Innode
                    self.tail = Innode 
            if pos<0:
                sq1=(self.Size+pos)-1
                if(self.Size>sq1):
                    node=self.head
                    for i in range(sq1):
                        node=node.next
                    ISnode=Node(item)
                    Cnode=node.next
                    node.next=ISnode
                    ISnode.next=Cnode
                    ISnode.previous=node
                    Cnode.previous=ISnode
                else:
                    Innode=Node(item)
                    Innode.next=self.head
                    self.head.previous = Innode
                    self.head = Innode 
            if(pos==0):
                if self.isEmpty():
                    self.head = Node(item)
                    self.tail = self.head
                    return 0
                elif(self.tail is None and self.head is not None):
                    node = self.head
                    self.tail=node
                    self.head = Node(item)
                    self.head.next = node
                    node.previous=self.head
                elif(self.tail is not None and self.head is not None):
                    Anode= self.head
                    self.head = Node(item)
                    Anode.previous=self.head
                    self.head.next=Anode
        else:
            if(pos>0):
                if self.isEmpty():
                    self.head = Node(item)
                    self.tail = self.head
                    return 0
                else:
                    Innode=Node(item)
                    cnode2=self.tail
                    Innode.previous=self.tail
                    cnode2.next = Innode
                    self.tail = Innode 
            if(pos<0):
                if self.isEmpty():
                    self.head = Node(item)
                    self.tail = self.head
                    return 0
                else:
                    Innode=Node(item)
                    CnodeN2 = self.head
                    Innode.next=self.head
                    CnodeN2.previous = Innode
                    self.head = Innode   
        self.Size += 1

    def search(self, item):
        #Code Here
        if self.found(item) == 0:
            return 'Not Found'
        else:
            return 'Found'

    def found(self,item):
        return self.indexOf(item) >= 0
    
    def indexOf(self,item) :
        q = self.head
        for i in range(self.Size) :
            if q.value == item :
                return i
            q = q.next
        return -1

    def index(self, item):
        #Code Here
        p = self.head
        for i in range(self.Size) :
            if p.value == item :
                return i
            p = p.next
        return -1

    def size(self):
        #Code Here
        return self.Size

    def pop(self, pos):
        #Code Here
        if pos<0 or pos>=self.Size:
            return 'Out of Range'
        if pos == 0 :
            self.head = self.head.next
            self.previous = None
            self.Size -= 1
        elif pos == self.Size - 1 :
            x = self.nodeAtnext(pos)
            p = x.previious
            p.next = None
            self.Size -= 1
        else:
            self.removeNode(self.nodeAtnext(pos))
        return 'Success'
    
    def pint(self):
        if self.Size == 0:
            return 'Emtpy'
        current = self.head
        s = ''
        while current:
            s+=str(current.value)+' '
            current = current.next
        return s

    def removeNode(self,q) :
        p = q.previous
        x = q.next
        p.next = x
        x.previous = p
        self.Size -= 1

    def nodeAtnext(self,i) :              # หาค่าตำแหน่งของโหนด เทียบกับ อินเด็กซ์
        p = self.head
        for j in range(i) :
            p = p.next
        return p

    def nodeAtprev(self,i) :              # หาค่าตำแหน่งของโหนด เทียบกับ อินเด็กซ์
        p = self.tail
        for j in range(i) :
            p = p.next
        return p

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())