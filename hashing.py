### today i learning the hashing
### -- hashing is where used to optimized the problem with avoiding the 0(n*5) complexity to 0(n) constant time 

### in the strivers sheet 

### three topic to be covered and have to learn the approach
##1-how to do the integer hashing 
##2- how to the char hashing 
###3 - how to optimized for the size of big hashing 


arr = "abcdabefc"
hash = [0] * 5

for num in str(arr):
     hash[int(num)] +=1
 
print(hash[3])