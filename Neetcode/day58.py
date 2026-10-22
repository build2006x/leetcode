### hey hi today i am working on K-th Symbol in Grammar
n=30
k=536870912
# number = "0"
# pointer = 0
# res = ""

# while pointer < n-1:
#         for i in number:
#                 if int(i) == 0:
#                     res +="01"
#                 else:
#                     res +="10"
#         number = res
#         res = ""
#         pointer +=1


### this algo is learned after watching the solution 
## how they think is doing a search ,,, insead of generating the whole tree is heavy task ,,

pointer = 0
n=19
k=45876
left = 0
right = 2**n-1

for i in range(n-1):
        mid = (left+right)//2
        if k<= mid:
            right =  mid 
        else:
                left = mid  +1
                if pointer == 1:
                    pointer  = 0
                else:
                    pointer = 1
print(pointer)
                
    











