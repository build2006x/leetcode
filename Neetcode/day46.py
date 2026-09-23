### hey hi today i am working on Two Integer Sum II since in this problem the array is 1 indexded array 

numbers = [1,2,3,4]
target = 3

l = 0 
r = len(numbers) - 1


while l < r:
        if numbers[l]+numbers[r] == target:
                  print(l+1,r+1)
        elif numbers[l]+numbers[r] < target:
                    l +=1
        elif numbers[l]+numbers[r] > target:
                   r -=1
   
     

