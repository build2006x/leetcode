###today sum is like 

s = "221"

arr = list(s)

endPoint = len(s) - 1

while True:
    if int(arr[-1])% 2 != 0:
        arr.pop()
    elif int(arr[-1])% 2 == 0:
        break

string = "".join(arr)
print(string)
