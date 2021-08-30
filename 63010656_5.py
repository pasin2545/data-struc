a = 0
def bon(w):
	### Enter Your Code Here ###
    for i in range(0,len(w)) :
        for j in range(i+1,len(w)):
            if w[i] == w[j]:
                if w[i]=='a':
                    a = 1
                elif w[i]=='b':
                    a = 2
                elif w[i]=='c':
                    a = 3
                elif w[i]=='d':
                    a = 4
                elif w[i]=='e':
                    a = 5
                elif w[i]=='f':
                    a = 6
                elif w[i]=='g':
                    a = 7
                elif w[i]=='h':
                    a = 8
                elif w[i]=='i':
                    a = 9
                elif w[i]=='j':
                    a = 10
                elif w[i]=='k':
                    a = 11
                elif w[i]=='l':
                    a = 12
                elif w[i]=='m':
                    a = 13
                elif w[i]=='n':
                    a = 14
                elif w[i]=='o':
                    a = 15
                elif w[i]=='p':
                    a = 16
                elif w[i]=='q':
                    a = 17
                elif w[i]=='r':
                    a  = 18
                elif w[i]=='s':
                    a = 19
                elif w[i]=='t':
                    a = 20
                elif w[i]=='u':
                    a = 21
                elif w[i]=='v':
                    a   = 22
                elif w[i]=='w':
                    a = 23
                elif w[i]=='x':
                    a = 24
                elif w[i]=='y':
                    a = 25
                elif w[i]=='z':
                    a = 26
                a = a*4
                b = str(a)
    return b

secretCode = input("Enter secret code : ")
print(bon(secretCode))