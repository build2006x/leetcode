### hey hi today i am working on the problem rearrange according to the postive and negative in the order 

# arr = [3,1,-2,-5,2,-4]
# p = []
# n = []

# for i in arr:
#     if i < 0:
#         n.append(i)
#     else:
#         p.append(i)

# result = []
# read = 0
# for i in range(0,len(arr)):
#     if i < len(p):
#       arr[read] = p[i]
#       read +=1
#     if  i < len(n):
#       arr[read] = n[i]
#       read +=1

# print(arr)

### let us think in the two pointer method to avoid the extra  memory useage 

arr = [3, 1, -2, -5, 2, -4]
left  = 0
right = 1

while right < len(arr):
      if ( arr[left] > 0 and arr[right] < 0 ):
              left +=2
              right = left + 1

      elif ( arr[left] < 0 and arr[right] > 0 ):
             arr[left],arr[right] = arr[right],arr[left]
             left +=2
             right = left + 1   

      elif ( arr[left] > 0 and arr[right]>0 ):
             next_pos = right + 1
             if next_pos < len(arr)  and arr[next_pos] < 0 :
                     arr[right],arr[next_pos] = arr[next_pos],arr[right]
                     left +=2
                     right = left +1
             next_pos = 0

      elif ( arr[left] < 0 and arr[right] < 0 ):
             next_el = right + 1
             if next_el < len(arr)  and arr[next_el] > 0:
                     arr[left],arr[next_el] = arr[next_el],arr[left]
                     left +=2
                     right = left +1
             next_el = 0
 
print(arr)
              

