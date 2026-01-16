### reverse array 
### 

###using the built in function 

N = 5
arr = [5,4,3,2,1]

def reverse_arr():
    return arr[::-1]

result = reverse_arr()



### using the brute force approach 
array = [5,4,3,2,1]
n = 5

result  = []
end  = len(array) 
for i in range(0,len(array)):
        result.append(end)
        end -=1




### better approach in place using the two pointer 
arries = [5,4,3,2,1]
lenght = 5

start = 0
end = len(arries)-1

while start<end:
      arries[start],arries[end]=arries[end],arries[start]
      start +=1
      end -=1

print(arries)