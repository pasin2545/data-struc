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
    
    def POpleft(self):
        self.items.pop(0)

S = Stack()
Mush=[]
Nub = []
Lol = 0
y=0
check = 0
check2 =0
num =0
num2 =0
inp = input('Enter Input : ').split(',')

for i in inp:
    if len(i) > 1:
        i = i.split()
        if i[0] == 'A':
            check2+=1
            S.push(i[1])
    if i == 'S':
        for j in S.items:
            if int(j)%2 == 0:
                y = int(j)-1
                Mush.append(str(y))
            if int(j)%2 == 1:
                y = int(j)+2
                Mush.append(str(y))
            '''print(S.items)
            print("**********")
            print(Mush)'''
        S.items=[]
        for k in Mush:
            S.push(k)
        #print(S.items)
        Mush=[]


    if i == 'B':
        for i in S.items:
            #print(i)
            for j in range(len(Nub)):
                #print("1")
                '''if int(i) > int(Nub[-1]):
                    print("Correct")
                if int(i) == int(Nub[-1]):
                    print("equal")'''
                if int(i) > int(Nub[-1]) or int(i) == int(Nub[-1]) : 
                    #print("**2**")
                    #print(S.items[-1])
                    Nub.pop()
                    
            Nub.append(i)
            #print(Nub)
        """for i in S.items[::-1]:
            if int(S.items[-1]) <= int(i):
                Lol += 1
                check +=1
                if check == 1:
                    num = int(i)
                    check = 1
                if check == 2:
                    num2 = int(i)
                    check = 1
                if num2 > num:
                        check=0
                elif num2 == num:
                        Lol-=1
                        check = 0
                '''print(num)
                print("///////")
                print(num2)'''"""
        #if(check2 >= 1):
            #Lol +=1
            #print("..........")
        print(len(Nub))
        Nub = []
            #print("..........")
            #Lol = 0
            #check =0
        #else:
            #print("..........")
            #print(Nub)
            #print("..........")
            #Lol=0
            #check =0
