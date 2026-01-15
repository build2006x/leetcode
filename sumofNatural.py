### sum of n natural numbers 


def naturalNumber(n,count):
    if n == 0:
        return count
    count +=n
    return naturalNumber(n-1,count)

result = naturalNumber(n=6,count=0)
print(result)

