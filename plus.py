### today 
### i am working on the plus one sum 

digits = [9,9]
main = digits[::-1]
read = 0

### the logic perfectly works like if the 9 is there put the zero until up and next pointer increment them if not end the read means append a one 

if main[read] != 9:
       main[read] +=1
       print(read[::-1])
else:
    while read < len(digits) and main[read] ==9:
          main[read] = 0
          read +=1
    if read < len(digits):
           main[read] +=1
    else:
         main.append(1)
         print(main[::-1]) 
        
  



 