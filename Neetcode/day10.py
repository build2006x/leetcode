pointer  = 0 
move_pointer = 0
result  = []

strs=["act","pots","tops","cat","stop","hat"]

while pointer < len(strs):
    result.append(strs[pointer])
    while move_pointer < len(strs):    
        for index,val in enumerate(strs[pointer]):
            if val in strs[move_pointer]:
                if index == len(strs[move_pointer]):
                    result.append(strs[move_pointer])
            else:
               break
        move_pointer +=1
    move_pointer = 0
    pointer +=1

print(result)