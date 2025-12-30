##today sum is about product of three number in the array 
### the approach intiall like mix of storing
nums = [-10, -10, 5, 2]

result1 = 1
result2 = 1
start = 0
end = 0

while start < 4:
    result1 *= nums[start]
    start +=1
    result2 *= nums[end]
    end -=1

resulting = max(result1,result2)

print(resulting)  

