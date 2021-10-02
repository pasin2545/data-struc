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

Me = Queue1()
You = Queue2()
Keep1 = []
Keep2 = []
MyAct = []
YourAct = []
MyPos = []
YourPos = []
temp = []
temp2 = []
semifinalMe = []
semifinalYou = []
Keepmeitems = ''
Keepyouitems = ''
finalme =''
finalyou = ''
Ans = ""
score = 0

inp = input("Enter Input : ").split(',')

for i in inp:
    Keep1.append(i)

for i in Keep1:
    Keep2.append(i.split())

for i in range(len(Keep2)):
    for j in range(2):
        if j%2 == 0:
            Me.enQueue(Keep2[i][j])
        elif j%2 == 1:
            You.enQueue(Keep2[i][j])

for i in range(len(Me.items)):
    temp.append(Me.items[i].split(':'))

for i in range(len(You.items)):
    temp2.append(You.items[i].split(':'))

for i in Me.items:
    if i != Me.items[-1]:
        Keepmeitems += i
        Keepmeitems += ", "
    else:
        Keepmeitems += i

for i in You.items:
    if i != You.items[-1]:
        Keepyouitems += i
        Keepyouitems += ", "
    else:
        Keepyouitems += i

for i in range(len(temp)):
    if temp[i][0] == temp2[i][0] and temp[i][1] != temp2[i][1]:
        score += 1
    elif temp[i][0] != temp2[i][0] and temp[i][1] == temp2[i][1]:
        score += 2
    elif temp[i][0] == temp2[i][0] and temp[i][1] == temp2[i][1]:
        score += 4
    elif temp[i][0] != temp2[i][0] and temp[i][1] != temp2[i][1]:
        score -= 5
    
for i in range(len(temp)):
    if temp[i][0] == '0':
        MyAct.append("Eat")
    elif temp[i][0] == '1':
        MyAct.append("Game")
    elif temp[i][0] == '2':
        MyAct.append("Learn")
    elif temp[i][0] == '3':
        MyAct.append("Movie")
    if temp[i][1] == '0':
        MyPos.append("Res.")
    elif temp[i][1] == '1':
        MyPos.append("ClassR.")
    elif temp[i][1] == '2':
        MyPos.append("SuperM.")
    elif temp[i][1] == '3':
        MyPos.append("Home")

for i in range(len(temp2)):
    if temp2[i][0] == '0':
        YourAct.append("Eat")
    elif temp2[i][0] == '1':
        YourAct.append("Game")
    elif temp2[i][0] == '2':
        YourAct.append("Learn")
    elif temp2[i][0] == '3':
        YourAct.append("Movie")
    if temp2[i][1] == '0':
        YourPos.append("Res.")
    elif temp2[i][1] == '1':
        YourPos.append("ClassR.")
    elif temp2[i][1] == '2':
        YourPos.append("SuperM.")
    elif temp2[i][1] == '3':
        YourPos.append("Home")

for i in range(len(MyAct)):
    semifinalMe.append(MyAct[i])
    semifinalMe.append(MyPos[i])

for i in range(len(YourAct)):
    semifinalYou.append(YourAct[i])
    semifinalYou.append(YourPos[i])

for i in range(len(semifinalMe)):
    if i%2 == 0:
        finalme += semifinalMe[i]
        finalme += ':'
    elif i%2 ==1:
        if i != len(semifinalMe)-1:
            finalme += semifinalMe[i]
            finalme += ", "
        else:
            finalme += semifinalMe[i]

for i in range(len(semifinalYou)):
    if i%2 == 0:
        finalyou += semifinalYou[i]
        finalyou += ':'
    elif i%2 ==1:
        if i != len(semifinalYou)-1:
            finalyou += semifinalYou[i]
            finalyou += ", "
        else:
            finalyou += semifinalYou[i]

if score >= 7:
    Ans = "Yes! You're my love!"
elif score<7 and score > 0:
    Ans = "Umm.. It's complicated relationship!"
else:
    Ans = "No! We're just friends."


print("My   Queue =",Keepmeitems)
print("Your Queue =",Keepyouitems)
print("My   Activity:Location =",finalme)
print("Your Activity:Location =",finalyou)
print(Ans,": Score is",str(score)+'.' )

'''print(Me.items)
print(You.items)
print(temp)
print(temp2)
print(semifinalMe)
print(semifinalYou)
print(finalme)
print(finalyou)'''