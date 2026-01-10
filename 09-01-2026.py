### striver 2 second pattern problem 
### based on to build logical thinking 
## this is small logic behind this sums 

result = [1,0]
check = ""

for i in range(1,6):
    if i%2 == 0:
        check = str(0) + check
        print(check)
    else:
        check = str(1) + check
        print(check)
