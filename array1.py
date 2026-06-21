### today i am working on the leetcode array -- 2 question 4. Median of Two Sorted Arrays

nums1 = [1,2]
nums2 = [3,4]

for i in range(len(nums2)):
    nums1.append(nums2[i]) 
    
nums1.sort()

if len(nums1) % 2 !=0:
     index = len(nums1)/2 
     print(nums1[index.__floor__()])

else:
    index = len(nums1)/2
    final = nums1[(index-1).__floor__()] + nums1[(index).__floor__()]   
    print(final/2)


print(5/2)
    

