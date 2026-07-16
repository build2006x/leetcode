flowerbed=[0,0,1,0,0,0,0,0,1,0,0]
n=4


pointer = 0

while pointer < len(flowerbed):
     if flowerbed[pointer] == 0 and pointer < len(flowerbed)-1:
          if flowerbed[pointer-1] and flowerbed[pointer+1] ==0:
                         flowerbed[pointer] = 9
          elif flowerbed[pointer+1]==0:
                    if flowerbed[pointer] ==0:
                         flowerbed[pointer] = 9
          elif flowerbed[pointer+1] and flowerbed[pointer-1] ==0:
                    if flowerbed[pointer] == 0:
                         flowerbed[pointer] = 9
     pointer +=1  
 

print(flowerbed)