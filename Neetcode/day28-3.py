### hey hi today i am working on Pascal's Triangle II

###understanding of my question 

### basically the algorithm works in a way 


"""

pointer = 1
i will append one in the end and check is number exist means i will add and fit them inside the pattern 


append 1 in the end and front and start tranversal at each pair of number and append the array

"""

n = 0

result = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

p1 = 0
p2 =  1
T = 1


if n <= len(result):
     print(result[n])

else:
    while T != 0:
        new = []
        new.append(1)
        while p2 < len(result[-1]):
            add = result[-1][p1] + result[-1][p2]
            new.append(add)
            p2 +=1
            p1 +=1
        new.append(1)
        print(new)
        T -=1


