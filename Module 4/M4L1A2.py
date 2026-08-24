def match_words(words):
    ctr=0
    matching=[]
    for i in words:
        if len(i)>1 and i[0]==i[-1]:
            ctr+=1
            matching.append(i)
    print(matching)
    return ctr
ctr=match_words(["five", "ice", "teapot", "summer", "1991"])
print(ctr)