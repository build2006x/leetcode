string = "{[()]}"

open = "{[(])}"

open_result = []
close_result = []


close = [')','}',')']

for i in string:
    if i in open:
        open_result.append(i)
    else:
        close_result.append(i)


print(len(open_result)==len(close_result))