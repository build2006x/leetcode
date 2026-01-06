### today sum is about the find the next greater element and stacking in the array 
### in this question itself they given the logic to solve this 
### logic on mind pop up now 

## have a while to 0 to n-1 base loop 
## this second loop have for finding the same element in the num1 
## if find check the next element where greater means have them in the result array 
## or else keep -1 in the result array 
## at last return the array




nums1 = [2,4]
nums2 = [1,2,3,4]
result = []

for i in nums1:
    next_greater = -1
    index = nums2.index(i)
    print(index)
    for j in range(index+1,len(nums2)):
        if i  < nums2[j]:
            next_greater = nums2[j]
            break
    result.append(next_greater)


print(result)

    

