### today i learning much fundamental for my dsa jounery  



def recursive(n,number):
    if n < 0 :return False
    if pow(3,number) == n:
        return True
    return recursive()
    
result = recursive(4,number)
print(result)

