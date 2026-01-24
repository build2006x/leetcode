### today i learning the hashing

### for solving the common approach of solving the counting number of given input 

### common approach for sovling hash problem is using the 

### --- brute force by maintaing the counter variable 
### --- using dict of storing the count as value and index as to key 
### --- another way of solving using hashing 

#### -- the one liner of the hashing is prestore and fecthing them **** important point --


### -- hashing is where used to optimized the problem with avoiding the 0(n*5) complexity to 0(n) constant time 

### in the strivers sheet 

### three topic to be covered and have to learn the approach
##1-how to do the integer hashing 
##2- how to the char hashing 
# ###3 - how to optimized for the size of big hashing 

# arr = "hello"
# hash_map  = {}
# final = []

# for i in arr:
#     if i in hash_map:
#         hash_map[i] +=1
#     else:
#         hash_map[i] =1

# max = max(hash_map.values())
# print(hash_map.get(max))
### here in python we use dict to store the value likely prestoring to avoid the query again and again 
     
### --- today i going through the topic of hashing 
### --- basically hashing is conecpt in the python of indicating the dict 
### --- storing in the data in key value pair 

### -- storing the large value in the dict we use the hash table 
### -- for acessing the index we will map the index to the value of the key and store the 
### -- for the mapping the index to the key we create a hash function 
### -- during this creation of hash function same key is generating means 
### -- we get into the colloison 

### --- for sovling this problem two techinque -- open addressing and closed addressing 
### started learning from the video resource of the hashing 

# arr = [1,3,3,2,1,4]
# array = {}

# for i in arr:
#     if i in array:
#         array[i] +=1
#     else:
#         array[i] = 1

# print(array)
#### one strong way of understanding now i am having in the hash 
### storing the key and values 


### now trying the hashing way of solving this problem 

arries = [1,2,3,1]
arr = [0] * 4

for i in arries:
    if i in arr:
        arr[i] +=1
    else:
        arr[i] =1 

print(arr)