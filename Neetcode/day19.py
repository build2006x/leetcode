#### hey hi today i am working on the Kth Distinct String in an Array
# arr = ["a","b","a"]
# k = 2

# string = ""
# result = []

# for i in range(0,len(arr)):
#     for j in range(0,len(arr)):
#             if arr[i] == arr[j] and i != j:
#                   string = ""
#                   break
#             else:
#                   string = arr[i] 

#     if string != "":
#           result.append(string)
#           string = ""

# print(result)                  

result = [2,1,3]
k = 4

if 0 <= k < len(result):
    print(result[k])
else:
    print("")