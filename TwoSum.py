## today i am working on the two sum problem 

nums = [3,2,4] 
target = 6

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
           print(i,j)
           break
    
### using brute well work for this question insead i tried a sliding window approach and two pointer 

### bascially i learned something from this most question can be solve by brute force its better think first card placing thinknig of brute force and 
## then we can think about the optimal way of using pattern 

### twopointer always works on the sorted array and sliding window approach wont be possible 
