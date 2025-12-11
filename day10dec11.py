s = "Let's take LeetCode contest"
text = s.split()
final = []
add = ""

for words in text:
    add = words[::-1]
    final.append(add)
    add = ""

result = " ".join(final)
print(result)
print(final)