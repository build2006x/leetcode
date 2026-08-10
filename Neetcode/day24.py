discount = [50,60]
prices = [10,30,21]


track = []
result = []
pick_max = 0
pointer = len(discount) - 1

while pointer != -1:
      pick_max = max(prices)
      track.append(pick_max)
      dis_price = (pick_max * (100-discount[pointer]))//100
      result.append(dis_price)
      prices.remove(pick_max)
      pointer -=1
      pick_max =0

for i in prices:
      if i not in track:
            result.append(i)

print(track)
print(sum(result))