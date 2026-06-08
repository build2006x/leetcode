### today i am working on the subarray sums equals to k 

array = [3,1, 2, 4]
k=6

left = 0
right = 1
actual = 0

while right < len(array):
      while right < len(array):
            if array[left] + array[right] == k:
                  print([left,right])
            right +=1
      left = right + 1





