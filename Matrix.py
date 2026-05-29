### hi today i am working on the matrix sum 
### if the array contains a 0 means it should be 0 all rows and columns 

#### the solution == brute force 
### if one find means --- change it as to -1 and again iterate over the array --- change the -1 into 0 

matrix=[
        [1,1,0],
        [1,0,1],
        [1,1,1]
]

for i in matrix:
    for idx,j in enumerate(i):
      if j == 0:
        for k in range(0,3):
            i[k] = -1
            for q in matrix:
                q[idx] = -1 

for i in matrix:
    for idx,j in enumerate(i):
       if j == -1:
         i[idx] = 0
         
for i in matrix:
   print(i)

