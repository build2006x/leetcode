## hey hi 

s = "foo"
t = "bar"

freq1 = {}
freq2 = {}

for chr_s,chr_t in zip(s,t):
    if chr_s in freq1 and freq2[chr_t] != chr_t:
        print('False')
    freq1[chr_s] = chr_t 
    freq2[chr_t] = chr_s       
         
        
