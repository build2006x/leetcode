### Word Pattern

pattern = "aaaa"
s = "dog cat cat dog"

arr = s.split(" ")

barath = {}

for idx,i in enumerate(pattern):
        if i in barath:
            if barath[i] != arr[idx]:
                 print('False')
                 break
        else: 
            barath[i] = arr[idx]
      