### hey hi today i am working on the Reverse Words in a String III

s = "Let's take LeetCode contest"
left = 0 
rigth = 1
final  = ""

while rigth < len(s):
     if s[rigth] == ' ' or s[rigth] == '':
            string_new = s[left:rigth]
            final += string_new[::-1] + " "
            left = rigth + 1 
            
     rigth +=1

s = ""

s = final
print(s)