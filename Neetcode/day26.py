### hey hi today i am working on the height checker 

heights = [1,1,4,2,1,3]


expected = sorted(heights) 

pointer = 0 
count = 0

while pointer < len(heights):
        if expected[pointer] != heights[pointer]:
                count +=1
                pointer +=1
        else:
            pointer +=1

print(expected)
print(count)