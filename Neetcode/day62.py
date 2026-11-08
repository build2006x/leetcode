############ hey hi today i am working on the Grumpy Bookstore Owner
customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1] 
minutes = 3

# 

# for i in range(len(customers)-minutes,len(customers)):
#          sum_val +=customers[i]

# pointer = 0

# while pointer < len(customers)-minutes:
#          if grumpy[pointer] == 0:
#                    sum_val += customers[pointer]
#          pointer +=1


# print(sum_val)
    
sum_val = 0
pointer = 0

while pointer < len(customers):
      if grumpy[pointer] == 0:
               
                    sum_val +=customers[pointer]
      pointer +=1


pointer = 0
count = 0

s_array = sorted(customers)


while count < minutes and pointer < len(customers):
        if grumpy[pointer] == 1:
                 
                    sum_val +=customers[pointer]
                    count +=1
        pointer +=1

                
            
                 