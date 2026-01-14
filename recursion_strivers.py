### today i working ont he recursion basic problem sovling them 

def recursion_times(count):
    if count == 0:
         return ""
    print("ashisha",end=" ")
    return recursion_times(count-1) 

result = recursion_times(count=3)
print(result)