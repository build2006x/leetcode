### hey hi today  i am working on the leetcode question on finding the majority element in the array 

# nums = [7, 0, 0, 1, 7, 7, 2, 7, 7] 

# freq = {}

# for i in nums:
#     if i in freq:
#         freq[i] +=1
#     else:
#         freq[i] = 1

# maxval = 0
# count = 0
# for i,p in freq.items():
#     count +=1
#     maxval = max(maxval,p)
#     if count == len(freq):
#        for idx,pointer in freq.items():
#            if maxval == pointer:
#                print(idx)

### brute force approach to solve the majority element in the array 
   
### in the above code like the point i am missing is this majority there is a condition was if the element times is greater than 

# nums =  [2,2,1,1,1,2,2]

# freq = {}

# for i in nums:
#     if i in freq:
#         freq[i] +=1
#     else:
#         freq[i] = 1

# for idx,val in freq.items():
#     if val > len(nums)//2:
#         print(idx)


