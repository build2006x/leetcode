### hey hi this is barath kumar 

word="apple"
abbr="a4"

pointer = 0
new_check = 0


while pointer < len(abbr):
        if word[pointer] == abbr[pointer]:
              pointer +=1
        else:  
            new_check = len(word[pointer:])
            if int(abbr[pointer]) >= new_check:
                   pointer +=1
            else:
                  print('False')

