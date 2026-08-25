### hey hi today i am working on the Find Words That Can Be Formed by Characters

words = ["cat","bt","hat","tree"]

chars = "atach"


for i in words:
    for idx,val in enumerate(i):
        if val in chars:
            print(i)
            break\
        else:
            break
            


