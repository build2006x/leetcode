### today i am working on the checking the given array 
### is being sorted or not 
### simple like iterate through the compare two elments 

### the logic is about checking that if the condition breaks means i need to rotate them and checks onces again to check
### weather the array is being can be vaild again 

"""
Docstring for leetcode.CheckArrSorted

#### 


"""

breaking  =  0  
nums = [3,4,5,1,2]
index = 0
new_lista = []

for i in range(0,len(nums)-1):
    if nums[i] > nums[i+1]:
        breaking = False 
        index = i

if breaking == False:
    new_lista.extend(nums[index+1:len(nums)])
    new_lista.extend(nums[0:index+1])



for j in range(0,len(nums)-1):
    breaking = True
    if new_lista[j] > new_lista[j+1]:
        breaking = False
        break


print(breaking)