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



# for i in string:
#     if i in arr_dict:
#         stack.append(i)
#     else:
#         if not stack:    
#            print('no openning string')
#         top = stack.pop()
#         if arr_dict[top] != i:
#            print('invaild')
    

def VaildPara(string):
    arr_dict  = {'[':']','{':'}','(':')'}
    stack = []
    for i in string:
        if i in arr_dict:
            stack.append(i)
        else:
            if not stack:    
               return False
            top = stack.pop()
            if arr_dict[top] != i:
               return False  
    return True

result = VaildPara("()")

print(result)

### basically the algorithm works by put the opening first in the stack and see weather the check the crossponding to the closing bracket is there means 
### pop the matched pairs in the stack 

