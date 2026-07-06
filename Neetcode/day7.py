#### 

def function_map():
    arr =["a","a","a"]

    if not arr:
        print('nope cant find string in the array')


    shortest = min(arr, key=len)
    prefix = ""

    for i in range(0,len(shortest)):
        char = arr[0][i]  # reference char
        for word in arr:  # compare across all strings
            if word[i] != char:
                return prefix
        prefix += char
    return prefix

result = function_map()

print(result)