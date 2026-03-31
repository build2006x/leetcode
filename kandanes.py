nums = [2, 3, 5, -2, 7, -4]

window = 1
clear = 0
result = 0

while window < len(nums):
      start = 0 
      while start + window <= len(nums):
            clear += sum(nums[start:window+start])
            print(nums[start:window+start])
            if clear > result:
                  result = clear
            start +=1
            clear = 0
      window  +=1

print(result)

            