### hey hi today i am working on the 2161. Partition Array According to Given Pivot



"""
steps to sovle this question i have my perspective of solving this question

find the index of the pivot index (first loop before the main loop)
assign that index to a variable 

vaild index of storing would be less than the index (pivot) (less value than the pivot--variable_value)
vaild index of storing would be greatern than indxe (pivot) (greater than the value of the pivot__variable_value)


logic gain 

3loop --- one for and two while to arrange range pivot_index - 1 and pivot_index + 1

"""

nums = [-3,4,3,2]
s = sorted(nums)
pivot = 2
small = []
big = []
main_idx = 0
l = 0 
r = 1 


for idx,val in enumerate(nums):
    if val == pivot:
         main_idx = idx
         l = main_idx - 1
         r = main_idx + 1
         break

for idx,i in enumerate(s):
     if i < pivot and idx != main_idx:
          small.append(i)
     elif i >= pivot and idx != main_idx:
         big.append(i)

small = sorted(small)
big = sorted(big)

for i in small:
    if l >= 0:
        nums[l] = i
        l -= 1

for j in big:
    if r < len(nums):
         nums[r] = j
         r +=1

print(nums)