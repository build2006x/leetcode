####### hey hi today i am working 
####### on the Merge Two 2D Arrays by Summing Values


nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]
result = []
p = 0

sum_val = 0

while p < len(nums1):
     if nums1[p][0] == nums2[p][0]:
             sum_val = nums2[p][1] + nums1[p][1]
             result.append([nums1[p][0],sum_val])
     p +=1

print(result)
