#### hey hi this is barath kumar today i am working on the 

s = "ab#"
t = "ad#c"
pointer = 0
pointer_1 = 0
result = []
result_1 = []



while pointer < len(s):
            if s[pointer] != "#":
                    result.append(s[pointer])
            else:
                if result:
                    result.pop()
            pointer +=1

while pointer_1 < len(s):
            if s[pointer_1] != "#":
                    result_1.append(s[pointer_1])
            else:
                if result_1:
                    result_1.pop()
            pointer_1 +=1

s_1 = "".join(result)
t_1 = "".join(result_1)

print(s_1==t_1)
