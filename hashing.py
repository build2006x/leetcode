### today i learning the hashing
### -- hashing is where used to optimized the problem with avoiding the 0(n*5) complexity to 0(n) constant time 

### in the strivers sheet 

### three topic to be covered and have to learn the approach
##1-how to do the integer hashing 
##2- how to the char hashing 
###3 - how to optimized for the size of big hashing 

arr = "hello"
hash_map  = {}
final = []

for i in arr:
    if i in hash_map:
        hash_map[i] +=1
    else:
        hash_map[i] =1

max = max(hash_map.values())
print(hash_map.get(max))
### here in python we use dict to store the value likely prestoring to avoid the query again and again 
     