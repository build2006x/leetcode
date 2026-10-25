### hey hi today i am praciting the binnary search -- 
nums = [2, 5, 8, 12, 16, 23, 38, 56, 72]
target = 23

l = 0
r = len(nums) -1 

while l <= r :
        mid = (l+r)//2
        if nums[mid] == target:
                print(mid)
                break
                
        elif nums[mid] < target:
                l = mid + 1
            
        else:
               r = mid - 1
    
        