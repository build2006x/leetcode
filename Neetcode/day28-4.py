### hey hi today i am working on the Find Words That Can Be Formed by Characters

words = ["cat","bt","hat","tree"]

chars = "atach"


static = 0 
reader = 0 
p1 = 0
result = 0

while p1 < len(words):
        while reader < len(chars) and static < len(words[p1]):
                if words[p1][static] == chars[reader]:
                            static +=1
                            reader  +=1
                else:
                    reader +=1
        if static == len(words[p1])-1:
                result += len(words[p1])
        static = 0
        reader  = 0
        p1 +=1
print(result)


