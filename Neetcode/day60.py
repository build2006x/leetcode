#### hey hi toady i am working on the 
prices = [10,8,7,5,2]

l = 0 
r = 1
min_price = prices[0]
max_price = 0

while r < len(prices): 
        if r <len(prices) and prices[l] < prices[r]:
            min_price = min(min_price,prices[l])
            max_price = max(max_price,prices[r])
            r +=1
        else:
             l = r
             r +=1

        
if (max_price-min_price) < 0:
       print('no profit cant make')

else:
      print(max_price-min_price)

         
