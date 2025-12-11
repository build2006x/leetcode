#so i tried this sum to get easy with the prespective to solve the string reserver sums 
#to solve using the two pointer method 

def plaindrome():
    s = "hello"
    p1 = 0 
    p2 = len(s) - 1

    while p1 != p2:
        if s[p1] != s[p2]:
            return False
        else:
            p1 +=1
            p2 -=1
    return True


result = plaindrome()

print(result)