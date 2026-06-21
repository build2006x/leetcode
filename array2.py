### today 21.6.26 , i am working on Write a function to find the longest common prefix string amongst an array of strings.

strs = ["flower","flow","flight"]


pointer = 0

while True:  
      if strs[0][pointer] == strs[1][pointer] == strs[2][pointer]:
              pointer +=1
      else:
            break
for i in strs:
       print(i[0:pointer])
       break

