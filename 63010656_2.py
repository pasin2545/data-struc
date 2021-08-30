def weirdSubtract(n,k):
        final = n
        for i in range(k):
                if final%10 != 0 :
                        final-=1
                elif final%10 == 0:
                        final = final/10
        return int(final)


n,s = input("Enter num and sub : ").split()

print(weirdSubtract(int(n),int(s)))