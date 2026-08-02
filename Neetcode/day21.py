#### hey hi today i am working on the finding the missing values int he 2 d array 

grid = [[1,2,3,4,5,6,7,8,9,10,11],[12,13,14,15,16,17,18,19,20,21,22],[23,24,25,26,27,28,29,30,31,32,33],[34,35,36,37,38,39,40,41,42,43,44],[45,46,47,48,49,50,51,52,53,54,55],[56,57,58,59,60,61,62,63,64,65,66],[67,68,69,70,71,72,73,74,75,76,77],[78,79,10,81,82,83,84,85,86,87,88],[89,90,91,92,93,94,95,96,97,98,99],[100,101,102,103,104,105,106,107,108,109,110],[111,112,113,114,115,116,117,118,119,120,121]]

### first finding the repeated values in the grid 
### second we need to find the missing values 

pointer = 0
reader = 0

store = []
arr = []

final = []

miss = 0
repeat = 0

while pointer < len(grid):
        reader = 0
        while reader < len(grid[pointer]):
                arr.append(grid[pointer][reader])
                if grid[pointer][reader] in store:
                       repeat = grid[pointer][reader]
                       break
                else:
                       store.append(grid[pointer][reader]) 
                reader +=1
        pointer +=1
        

for i in range(1,len(arr)+1):
        if i not in arr:
                miss = i
                break

final.append(repeat)
final.append(miss)

print(final)

        
