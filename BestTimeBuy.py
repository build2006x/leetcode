### hey hi man today 
### i am working on the best time to buy the stock and sell them 
### -- output - 5 

prices = [7,6,4,3,1]

min_entry = prices[0]
idx_min = 0
max_entry = 0

for idx,val in enumerate(prices):
    if val < min_entry:
        min_entry = val
        idx_min = idx

for n in range(idx_min+1,len(prices)):
    if prices[n] > max_entry:
        max_entry = prices[n]

print(max_entry-min_entry)

### above code use the burte force to sovle the problem ...now we think to solve the problem using the any pattern 

### likely the two pointer or sliding window 