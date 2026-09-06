test_dict={'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
print(test_dict)
K=2
res=0
for key in test_dict:
    if test_dict[key]==2:
        res+=1
print("Final frequency count:",res)