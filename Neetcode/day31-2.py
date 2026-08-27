### Largest 3-Same-Digit Number in String (problem)

### today august 27 --- 2026


### problem goals is to return the longest same integer from integer as string 

num = "6777133339"


static = 0
dynamic = 1
pointer = 0

while pointer < len(num):
        if num[static] == num[dynamic]:
                dynamic +=1
        else:
            static +=1
            dynamic = static + 1
        pointer +=1
     

print(num[static:dynamic+1])
