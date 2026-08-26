### hey hi today i am working on the Find Words That Can Be Formed by Characters
from collections import Counter
words = ["cat","bt","hat","tree"]
chars = "atach"
result = 0
char_count = Counter(chars)


for word in words:
     word_count = Counter(word)
     if all(word_count[c] <= char_count[c] for c in word):
           result += len(word)

print(result)