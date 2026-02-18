#### today i working on the sum where i need to find the number which have 1 count 

# from collections import Counter

# arr = [2,2,1]

# Count = Counter(arr)

# for i,j in Count.items():
#     if j == 1:
#         print(i)

#### here we are using the frequency module to get the count of the each element

arr = [2,2,2,1]

arr_final  = [0] * len(arr)

for i in arr:
    if i in arr_final:
            arr_final[i] +=1
    else:
          arr_final[i] +=1

for i in range(0,len(arr)):
      if arr_final[i] == 1:
            print(i)

#### using hasing solved the above problem 
### two values -- one is store the pre define zero set to update them 
### later by mapping the value to the array 