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

prices = [7,6,4,3,1]

market_entry  = prices[0] 
market_exit   = 0

for num in range(1,len(prices)):
    market_entry = min(market_entry,prices[num])
    market_exit = max(market_exit,prices[num])


print(market_exit)