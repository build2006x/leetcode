s = "   fly me   to   the moon  "

count  = 0

string = s.split(" ")

for i in string[::-1]:
    if i not in (" "):
       print(len(i))
       break