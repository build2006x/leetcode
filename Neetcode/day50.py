#### hey hi today i am working on the 2161. Partition Array According to Given Pivot
### again starting out to sovle this time with more understandning of the question 
""""
here the best point of learning is about we want still tarck of the piviot index 
if we are remove a el in left half obousively the array going to shrink based on the left and right we des or incr the array is important
"""
nums = [9,12,5,10,14,3,10]
pivot = 10
p1 = 0
p2 = len(nums) -1 
res = [0] * len(nums)

for i in range(0,len(nums)):
                j = len(nums) - 1 - i 
                if nums[i] < pivot:
                                res[p1] = nums[i]
                                p1 +=1
                if nums[j] > pivot:
                                res[p2] = nums[j]
                                p2 -=1
            
while p1 <= p2:
            res[p1] = pivot
            p1 +=1

print(res)