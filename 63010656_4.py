Give = []
total = []
num = [0]*3
x = input("Enter Your List : ").split()
for i in range(len(x)) :
    x[i] = int(x[i])
    Give.append(x[i])
if len(Give) < 3:
    print('Array Input Length Must More Than 2')
else :
    for i in range(0,len(x)):
        for j in range(i+1,len(x)):
            for k in range(j+1,len(x)):
                if x[i]+x[j]+x[k] == 5:
                    num[0] = x[i]
                    num[1] = x[j]
                    num[2] = x[k]
                    num.sort()
                    total.append(num.copy())             
    last = []
    for i in total:
        if i not in last:
            last.append(i)
    print(last)
