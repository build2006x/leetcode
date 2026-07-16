flowerbed=[0,0,1,0,0,0,0,0,1,0,0]
n=4 


new =  [0] + flowerbed  + [0]

pointer = 1

while pointer < len(new) - 1:
          if new[pointer-1] ==0 and new[pointer+1] == 0 and new[pointer]  ==0:
                                   new[pointer] = 1
                                   n -=1
          pointer +=1

print(n<=0)
