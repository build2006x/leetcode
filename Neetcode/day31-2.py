### Largest 3-Same-Digit Number in String (problem)
### today august 27 --- 2026
### problem goals is to return the longest same integer from integer as string 
num="2300019"

static = 0
dynamic = 1
pointer = 0
result = ""
max_char = 0

while pointer < len(num):
        if len(num[static:dynamic+1]) == 3 and num[dynamic] == num[dynamic-1]:
                result = num[static:dynamic+1]
                print(max(0,int(result)))
                break
                max_char = max(int(result),max_char)   
                static = dynamic + 1
                dynamic = static + 1
        elif dynamic < len(num) and num[static] == num[dynamic]:
                dynamic +=1
        else:
            static +=1
            dynamic = static + 1
        pointer +=1
     
print(max_char)