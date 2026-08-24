L=[1,2,3,4,5]
ctr=0
for i in L:
    ctr+=i
avg=ctr/len(L)
print(f"Total sum: {ctr}\nAverage:{avg}")
L.sort()
print(f"Smallest integer: {L[0]}\nLargest integer: {L[-1]}")