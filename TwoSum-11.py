numbers = [2, 7, 11, 15] 
target = 9 
p1 = 0
p2 = len(numbers) - 1 

while p1 < p2:
        if numbers[p1]+numbers[p2] == target:
                print(p1+1,p2+1)
        elif numbers[p1]+numbers[p2]  <target: 
                p1 +=1
        else:
                p2 -=1
