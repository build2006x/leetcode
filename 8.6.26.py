### today i am working on the subarray sums equals to k 

array = [3,1, 2, 4]
k=6

for left in range(len(array)): ### keeping the left as a fixed lock ----
    current_sum = 0
    for right in range(left, len(array)): #### keep the left as fixed and expand the right forwards 
        current_sum += array[right]
        if current_sum == k:
            print(array[left:right+1])

#### next i wanted to learn the siliding window technique ? 

# window = array[0] + array[1]
      
