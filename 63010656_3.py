l = []
class TorKham:
    def __init__(self):
        self.words = []

    def restart(self):
        self.words.clear()
        return "game restarted"

    def play(self, word):
        if (len(self.words)==0 or (self.words[len(self.words)-1][::-1][0:2][::-1]).upper() == (word[1][0:2]).upper()) and word[0]=='P':
            self.words.append(word[1])
            return self.words
        return "game over"

torkham = TorKham()

print("*** TorKham HanSaa ***")


S = input("Enter Input : ").split(',')


for i in S:
    if len(i)>1 :
        if i[0] != 'P' and i[0] != 'X':
            print( '\'' + i + '\'' + ' is Invalid Input !!!')
            break
        i = i.split()
        print('\''+i[1]+'\'',end=' -> ')
        print(torkham.play(i))
    elif i=='R':
        print(torkham.restart())