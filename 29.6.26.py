#### this file i am creating to test few codes for leetcode contest 


fixed = 0
arr = []
nums = [6,1,2,9]
mul = 2
k = 3
result = 1

while fixed < len(nums):
        result = 0
        for i in range(fixed,k):
            if mul:
                result *=nums[i]
                mul -=1
            else:
                 result +=nums[i]
        fixed +=1
        arr.append(result)

print(max(arr))