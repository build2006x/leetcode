people = [1,3,2,3,2]
limit = 3

l = 0
r = len(people) - 1
n = sorted(people)
count = 0

while l < r:
        if n[l]+n[r] <= limit:
                print(n[l],n[r])
                count +=1
                l +=1
                r -=1
              
        elif n[l]+n[r] > limit:
                  r -=1
                  count +=1
        else:
                l +=1
                count +=1

while l<=r:
     count +=1
     l +=1
        
print(count)