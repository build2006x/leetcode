### striver 2 second pattern problem 
### based on to build logical thinking 

result = [1,0]
check = ""


for i in range(0,6):
    if i % 2 == 0:
        check = check + str(1)
        print(check)
    else:
        check = check + str(0)
        print(check)