pointer  = 0 
move_pointer = pointer + 1
result  = []

strs = ["act","pots","tops","cat","stop","hat"]

while pointer < len(strs):
     result.append([strs[pointer]])
     while move_pointer < len(strs):
            if move_pointer != pointer:
                   if sorted(strs[pointer]) == sorted(strs[move_pointer]):
                        result[pointer].append(strs[move_pointer])
            move_pointer +=1
     move_pointer = 0
     pointer +=1

new_result = []

for i in result:
      new = sorted(i)
      if new not in new_result:
            new_result.append(new)
      new = []
    
print(new_result)