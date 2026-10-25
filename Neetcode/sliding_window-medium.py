### hey hi today i am working on the sliding window -- medium level problem 
s = "pwwkew"
look_up = []
l = 0
look_up.append(s[0])
r = l + 1
l_length = 0

while r < len(s):
            if s[r] not in look_up:
                s_lenght = len(s[l:r+1])
                look_up.append(s[r])
                l_length = max(l_length,s_lenght)
                r +=1
            else:
                l = r
                look_up = []
                look_up.append(s[l])
                r = l + 1
print(l_length)
        



      