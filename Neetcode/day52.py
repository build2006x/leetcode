######## hey hi today i am working on the Container With Most Water


height = [1,7,2,5,4,7,3,6]
### my understanding of the problem  ---> 
### what is the compute we need to do
"""
take the indices and minus them and take the both values and do the 
compute push to a array or maintain the max container water 
"""

pointer= 0
max_water = 0
reader = pointer + 1
width = 0
tall = 0

while pointer < len(height):
        while reader <  len(height):
                width = reader - pointer 
                tall = min(height[pointer],height[reader])
                val = width * tall
                if val > max_water:
                        max_water = width*tall
                widht = 0
                tall = 0
                val = 0
                reader +=1
        pointer +=1
        reader = pointer + 1