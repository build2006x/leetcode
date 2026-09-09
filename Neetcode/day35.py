#### hey hi today i am working on the 

s="0P"

alphabet = [chr(i) for i in range(97, 123)]
main = ""
pointer = len(s) - 1

while pointer != -1:
        if s[pointer].lower() in alphabet:
                main +=s[pointer].lower()
        pointer -=1

