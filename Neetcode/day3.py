### hi today i am working on the issubsquency problem on the neetcode 

s = "node"
t = "neetcode"

scount = 0
tcount = 0

while tcount < len(t):
    if s[scount] == t[tcount]:
          scount +=1
    if scount == len(s):
         print(scount)
         print('true')
    tcount +=1





          

