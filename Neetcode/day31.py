### hey hi today i am working on the Ransom Note (problem)
from collections import Counter
ransomNote = "aa"
magazine = "ab"

mag_count = Counter(magazine)
ran_count = Counter(ransomNote)

for key,val in ran_count.items():
    if ran_count[key] <= mag_count[key]:
           pass
    else:
          print('Flase')
