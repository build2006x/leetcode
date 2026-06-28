s="xx"
t="x"


checker = 0
        
while  checker  != len(s):
    for index ,reader in enumerate(t):
        if s[checker] == t[index]:
                print(t)
                s = s[:index] + s[index+1:]
                break
    checker +=1

if s == "":
    print('true')
else:
    print('false')
                                            