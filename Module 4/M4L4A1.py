import array as fruit_counts
fruit={"apple","banana","coconut","kiwi", "dragonfruit"}
fruit2={"mango","lychee","coconut","dragonfruit"}
fruit2.add("cherry")
inte=fruit.intersection(fruit2)
fruit_count=fruit_counts.array("i",[1,1,2,1,2,1])
fruit_count.append(1)
fruit_count.insert(4,1)
coun=fruit_count.count(1)
print(f"""---Class Fruit Basket Organizer---
First basket: {fruit}
Second basket: {fruit2}
{inte} was the found in basket 1 and basket 2.
Fruit count: {fruit_count}
There were {coun} 1s found in the fruit count.""")
fruit_count.reverse()
print(f"Fruit count reversed: {fruit_count}")