### hi today i am working on the 

text = "loonbalxballpoon"
s = "ballon"

## lets think the approach 
"""
just how you can think means s pointer should be there to have loop where if s_pointer should be in the loop 
and like keep a condition like while s_pointer != len(s): --- loops should run --> and if 
the text more to len means again reassign to the start 
"""
count  = 0
result = 0

while True:
        for i in s:
            for idx,j in enumerate(text):
                if i == j:
                    text = text[0:idx] + text[idx+1:]
                    count +=1
                    break
        if count == len(s):
            count = 0
            result +=1
        else:
            break

print(result)