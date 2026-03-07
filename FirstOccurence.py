#### finding the first occurence of the index in the given string 


# haystack = "sadbutsad"
# needle = "sad"

# for idx,val in enumerate(haystack):
#     if val == needle[0]:
#         print(idx)
#         break

### this above logic will fails in the edge case what if the actually 
### problem asking as to check whole string present or not so we cant 
### make this as only the start of the index of the searched value 

## i am thikning to go for two pointer method 

# haystack = "leetcode"
# needle = "leeto"

# read = 0
# view = 0
# index = -1 

# while read < len(haystack):
#      if haystack[read] == needle[view]:
#             read +=1
#             view +=1
#      elif haystack[read] != needle[view]:
#              view =0
#              read +=1
              
     
# if view <= len(index) - 1:
#       print()
# else:
#       print(-1) 
     

haystack = "leetcode"
needle = "leeto"

read = 0
view = 0
index = -1
length = len(haystack)

while length < len(haystack):
      if haystack[read] == needle[view]:
             view +=1
             if view == len(needle)-1:
                  index = read - view + 1            
      view =0
      read +=1

print(index)


       

    
