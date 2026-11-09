############ hey hi today i am working on the Grumpy Bookstore Owner
customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1] 
minutes = 3
 sum_val = 0 

        pointer = 0

        while pointer < len(customers): 
                if grumpy[pointer] == 0:
                      sum_val += customers[pointer]
                pointer +=1
        print(sum_val)
        window_sum = sum(customers[0:minutes])
   
        max_size = window_sum
        l = 0
        r = minutes - 1

        while r < len(customers):
                window_sum = window_sum - customers[l] + customers[r] 
                if window_sum >max_size:
                            max_size = window_sum
                r +=1
                l +=1

        print(max_size)
        
        return sum_val +  window_sum
                 