### hey hi today i am working on the 

### hey hi i have got some logic in mind today to solve but its brute force approach 
# res = ""

# for i in colors:
#     if i  not in res:
#          res +=i

# ## now find the each char big value number --> 
# max_val = 0
# for i in range(0,len(res)):
#     for j in range(0,len(colors)):
#          if i ==j:
#             max_val = max(neededTime[i],neededTime[j])
#     max_val =    

### above approach can be heavy computational ----> 

colors = "aaaa"
neededTime = [3,8,5,2]
l = 0
r = l + 1
count = 0

while r < len(colors):
        if colors[l] != colors[r]:
                l +=1
                r = l + 1
        elif  colors[l] == colors[r] and neededTime[l] > neededTime[r]:
                   count += neededTime[r]
                   r +=1
        else:
            count += neededTime[l]
            l = r
            r = l + 1

print(count) 

            