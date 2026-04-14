### hey hi man today 
### i am working on the best time to buy the stock and sell them 
### -- output - 5 

# prices = [7,6,4,3,1]
# min_entry = prices[0]
# idx_min = 0
# max_entry = 0

# for idx,val in enumerate(prices):
#     if val < min_entry:
#         min_entry = val
#         idx_min = idx

# for n in range(idx_min+1,len(prices)):
#     if prices[n] > max_entry:
#         max_entry = prices[n]

# print(max_entry-min_entry)

### above code use the burte force to sovle the problem ...now we think to solve the problem using the any pattern 

### likely the two pointer or sliding window 


### likely today i wanted to try some other way to solve the problem of the best time to buy the stock 

prices = [7,1,5,3,6,4]

min_prices  = float('inf')
profit = 0
#### we always use teh inf to track of the lowest number to track 
#### -inf is used to track of the largest num

### the logic to solve this problem using single loop

for rate in prices:
    if rate < min_prices:
        min_prices = rate
    elif rate - min_prices > profit:
            profit = rate - min_prices

print(profit)