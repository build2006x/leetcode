#### hey hi today i am working on the 2161. Partition Array According to Given Pivot
### again starting out to sovle this time with more understandning of the question 


""""

here the best point of learning is about we want still tarck of the piviot index 

if we are remove a el in left half obousively the array going to shrink based on the left and right we des or incr the array is important

"""

nums = [9,12,5,10,14,3,10]
pivot = 10
off_idx = []
reader = 0
pivot_index = 0

for idx,val in enumerate(nums):
    if val == pivot:
        pivot_index = idx
        break

pointer = 0

while pointer < pivot_index:
        if nums[pointer] < pivot:
            pointer +=1
        elif nums[pointer] > pivot:
              val = nums.pop(pointer)
              nums.insert(pivot_index,val)
              pivot_index -=1

j = pivot_index + 1

while j < len(nums):
        if nums[j] > pivot:
            j+=1
        elif nums[j] < pivot:
              val = nums.pop(j)
              nums.insert(pivot_index-1,val)
              pointer -=1
        elif nums[j] == pivot:
              val = nums.pop(j)
              nums.insert(pivot_index+1,val)
              j +=1

print(nums)