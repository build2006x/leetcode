### today sum is about the find the next greater element and stacking in the array 
###  

nums1 = [4,1,2]
nums2 = [1,3,4,2]
result = []
point1 = 0
checkPoint = 0

while point1 < len(nums1):
      while checkPoint < len(nums2):
            if nums1[point1] > nums1[checkPoint]:
                 result.append(checkPoint)
                 checkPoint +=1
            else:
                result.append(-1)              
      checkPoint =0 
      point1 +=1