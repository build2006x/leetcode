### today i am working on the pascal's triangle 


numsRow = 7
result = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
main = []

if numsRow < 1:
     print([1])
elif numsRow < 6:
     for i in range(numsRow):
          main.append(result[i])
else:
        for i in range(5):
                 if i < numsRow:
                     main.append(result[i])
        for i in range(numsRow - 5):
                new_arr = [1,1]
                next_pos  = 1
                left , right = 0,1
                while right < len(result[-1]):
                    sum_val = result[-1][left] + result[-1][right]
                    if next_pos < len(result[-1]):
                            new_arr.insert(next_pos,sum_val)
                            sum_val = 0
                            next_pos +=1
                    left +=1
                    right +=1
                result.append(new_arr)
                main.append(new_arr)
                new_arr = []
        
        

        
print(main)

