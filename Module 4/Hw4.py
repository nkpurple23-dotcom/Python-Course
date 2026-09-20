import array as ar
snack_box1={"chips","juice","apple","chips", "cookies"}
snack_box2={"cookies","juice","sandwich","sandwich"}
snack_box1.add("banana")
print(snack_box1)
shared=snack_box1.intersection(snack_box2)
snack_counts=ar.array("i",[4,2,7,5])
snack_counts.insert(0,7)
snack_counts.append(4)
snack_counts.count(7)
snack_counts.reverse()
print(snack_box1,"\n",snack_box2,"\n",shared,"\n",snack_counts)