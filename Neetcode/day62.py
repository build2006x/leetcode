############ hey hi today i am working on the Grumpy Bookstore Owner
customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1] 
minutes = 3
sum_val = 0 

for i in range(0,len(customers)):
    if grumpy[i] == 0:
           sum_val += customers[i]


window_sum = 0 
l = 0
r = minutes
new = 0 

# Step 2: Initialize the VERY FIRST window (0 to minutes - 1)
window_sum = 0
for i in range(minutes):
        if grumpy[i] == 1:
                window_sum += customers[i]
                
# Step 3: Your exact 2-pointer sliding window loop!
l = 0
r = minutes
current_extra = window_sum

while r < len(customers):
        if grumpy[r] == 1:
                current_extra += customers[r]
                
        if grumpy[l] == 1:
                current_extra -= customers[l]
                
        window_sum = max(window_sum, current_extra)

        r += 1
        l += 1

print(current_extra)