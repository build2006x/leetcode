### today sum is about the find the next greater element and stacking in the array 
### in this question itself they given the logic to solve this 
### logic on mind pop up now 

## have a while to 0 to n-1 base loop 
## this second loop have for finding the same element in the num1 
## if find check the next element where greater means have them in the result array 
## or else keep -1 in the result array 
## at last return the array

nums1 = [4,1,2]
nums2 = [1,3,4,2]

point1 = 0
point2 = 0

result = []

while point1 < len(nums1):
      check = 0
      next_greater = 0
      while point2 < len(nums2):
            if nums1[point1] == nums2[point2]:
                  check = point2 + 1
            point2 +=1  
      while nums2[check] < len(nums2):
            if nums1[point1] > nums2[check]:
                  next_greater = nums2[check]
                  break
      check +=1
      result.append(next_greater)
      point1 +=1
      check = 0
      point2 = 0


print(result)
    

