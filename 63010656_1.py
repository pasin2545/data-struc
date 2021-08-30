Num = []
class translator:

    def deciToRoman(self, num):

        while num > 0 :

            if num-1000 >=0 :
                num-=1000
                Num.append('M')
            elif num-900 >= 0:
                num-=900
                Num.append('CM')
            elif num-500 >= 0:
                num-=500
                Num.append('D')
            elif num-400 >= 0:
                num-=400
                Num.append('CD')
            elif num-100 >= 0:
                num-=100
                Num.append('C')
            elif num-90 >= 0:
                num-=90
                Num.append('XC')
            elif num-50 >= 0:
                num-=50
                Num.append('L')
            elif num-40 >= 0:
                num-=40
                Num.append('XL')
            elif num-10 >= 0:
                num-=10
                Num.append('X')
            elif num-9 >= 0:
                num-=9
                Num.append('IX')
            elif num-5 >= 0:
                num-=5
                Num.append('V')
            elif num-4 >= 0:
                num-=4
                Num.append('IV')
            elif num-1 >= 0:
                num-=1
                Num.append('I')
        Roman = ''
        for i in range(len(Num)):
            Roman += str(Num[i])
        return Roman
        


    def romanToDeci(self, s):

        deci = 0
        ### Enter Your Code Here ###
        for i in range(len(Num)):
            
            if Num[i] == 'M':
                deci += 1000
            elif Num[i] == 'CM':
                deci += 900
            elif Num[i] == 'D':
                deci += 500
            elif Num[i] == 'CD':
                deci += 400
            elif Num[i] == 'C':
                deci += 100
            elif Num[i] == 'XC':
                deci += 90
            elif Num[i] == 'L':
                deci += 50
            elif Num[i] == 'XL':
                deci += 40
            elif Num[i] == 'X':
                deci += 10
            elif Num[i] == 'IX':
                deci += 9
            elif Num[i] == 'V':
                deci += 5
            elif Num[i] == 'IV':
                deci += 4
            elif Num[i] == 'I':
                deci += 1
        
        return str(deci)

num = int(input("Enter number to translate : "))
#print("4")
print(translator().deciToRoman(num))
Num = []
print(translator().romanToDeci(translator().deciToRoman(num)))