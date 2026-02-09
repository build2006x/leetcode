arr =[9, 8, 7, 6] 

## finding the second largest element in the arr 

first = 0
second = 0
for i in arr:
     first = max(first,i)
     if i != first:   
       second = max(second,i)

print(f"first largest:{first} second largest{second}")
