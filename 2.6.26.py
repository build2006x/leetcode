### hey hi today i am working on the daily solving problem


### like a game is there we need to find who can finish the things up in the less time  ---

### water ride and land ride 

landStartTime = [5]
landDuration = [3] 
waterStartTime = [1]
waterDuration = [10]

result_possible = []
min_val1 = float('inf')
min_val2 = float('inf')

for i in range(len(landStartTime)):
      val1 = landStartTime[i] + landDuration[i]
      min_val1 = min(min_val1,val1)
     
for i in range(len(waterStartTime)):
    val2 = waterStartTime[i] + waterDuration[i]
    min_val2 = min(min_val2,val2)


print(min_val1+min_val2)
