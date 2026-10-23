### hey hi today i am working on the 
colors = "aabbc"
neededTime = [4,1,2,7,3]

l = 0
r = l  + 1 
res = ""

for i in colors:
    if i not in res:
          res +=i

l = 0
reader = l + 1
pointer = 0
count = 0

while pointer < len(res):
        while reader < len(colors):
                if colors[l] == colors[r]:
                        count += min(neededTime[l],neededTime[r])
                r +=1
             
