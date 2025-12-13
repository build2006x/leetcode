s = "ab"
t = "ahbgd"  

#so the problem i am undergoing is find the subsequence of the string
#s to t 

#like i am thinking keep two pointer at the start of the two string one is s and another one is t 
#like the way i will move the pointer based on the compare of the both string 

def sequence(s,t):
    sender = 0
    finder = 0
    pointer = len(t) 
    char = list(s)
    while pointer != 0:
          if s[sender] == t[finder]:
                sender +=1
                finder +=1
                char.pop()
          elif s[sender] != t[finder]:
                finder +=1
          pointer -=1
    if char:
          print(char)
          return False
    else:
          return True        
 
result = sequence(s,t)
print(result)











