#### hey hi toady i am working on the 
prices=[2,1,2,0,1]

l = 0 
r = 1
max_profit = 0

while r < len(prices): 
        if r <len(prices) and prices[l] < prices[r]:
            if (prices[r] - prices[l]) > max_profit:
                    max_profit = prices[r] - prices[l]
            r +=1
        else:
             l = r
             r +=1

if (max_profit) < 0:
       print('no profit cant make')
else:
      print(max_profit)

         
