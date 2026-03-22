### today i working on the leetcode contest 

# Q1. Construct Uniform Parity Array 

### likely they give the array to consturct a another array - 2 like the first array - 1

# arr1 = [27,7]

### arr 2 should be two way of chossing them 

# -- one is arr2[i] = arr1[i]
# -- two is arr2[i] = arr[i] - arr[j] and i != j 

# count = 0

# for i in range(0,len(arr1)):
#     if arr1[i] %  2 == 0:
#          count +=1
#     else:
#         for j in range(0,len(arr1)):
#             val = arr1[i] - arr1[j] 
#             if val %2 == 0:
#                 count +=1
#                 break
#             val = 0
    

# print(count)


### -- Q2. Construct Uniform Parity Array II

### the second question is about the constructing a array which 

arr1 = [1,4,7]
count = 0

for i in range(0,len(arr1)):
    if arr1[i]%2 == 0:
         count +=1
    else:
        for j in range(0,len(arr1)):
            val = arr1[i] - arr1[j] 
            if val >= 1 and val % 2 == 0:
                count +=1
                break
            val = 0
count1 = 0
for idx in range(0,len(arr1)):
    if arr1[idx]%2 != 0:
         count1 +=1
    else:
        for idx2 in range(0,len(arr1)):
            val = arr1[idx] - arr1[idx2] 
            if val >= 1 and val % 2 != 0:
                count1 +=1
                break
            val = 0
     
print(count1)

if count == len(arr1):
    print('true')
elif count1 == len(arr1):
    print('true')
else:
    print('false')