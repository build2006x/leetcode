### hey hi today i am working on question 
##Count the Number of Consistent Strings

allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]

reader = 0
base_pointer = 0
count = 0
result = 0

while base_pointer < len(words):
      for i in words[base_pointer]:
            if i in allowed:
                  count +=1
            else:
                  break
      if count == len(words[base_pointer])-1:
             result +=1  
      base_pointer +=1
      count = 0

print(result)
