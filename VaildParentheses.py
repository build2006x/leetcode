string = "{[()]}"

# open = "{[(])}"

# open_result = []
# close_result = []
# close = [')','}',')']

# for i in string:
#     if i in close:
#         close_result.append(i)
#     else:
#         open_result.append(i)

# print(len(open_result)==len(close_result))
### this above way of approach is not working out 

string = "((())"

arr_dict  = {'[':']','{':'}','(':')'}
stack = []

for i in string:
    if i in arr_dict:
        stack.append(i)
        if arr_dict[i] in string:
             stack.pop()
    
print(stack)