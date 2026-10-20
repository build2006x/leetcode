### hey hi today i am working on the Divide Players Into Teams of Equal Skill question 

skill=[3,2,5,1,3,4]

l = 1
r = len(skill) -2 
n = sorted(skill)

sum_val = n[0]+n[-1]
res = n[0]*n[-1]

while l < r: 
        if n[l]+n[r] == sum_val:
                res += n[l] * n[r]
                l +=1
                r -=1
        else:
            print('no')
            break
    
print(res)
     

