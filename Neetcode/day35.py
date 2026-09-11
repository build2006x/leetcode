
#### hey hi today i am working on the 

s="aca"

alphabet = [chr(i) for i in range(97, 123)]
numbers = [chr(k) for k in range(48,58)]
main = ""
pointer = len(s) - 1

while pointer != -1:
        if s[pointer].lower() in alphabet:
                main +=s[pointer].lower()
        pointer -=1


print(s)