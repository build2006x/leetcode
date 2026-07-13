#### hey hi 
s = "foo"
t = "bar"

result = []
left = 0 

while left < len(s):
     result.append({s[left]:t[left]})
     left +=1

pointer = 0
dynamic = 1


for i in result:
     for k,m in i.items():
        for q,p in i.items():
            print(k,m)
            break
            if k == q and m !=p:
                print('False')
       
        
            