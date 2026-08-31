def check(p):
    f=len(p)-1
    l=0
    while l<f:
        if p[f]==p[l]:
            return True
        else:
            return False
        l+=1
        f-=1
p=(1,2,3,3,2,1)
if check(p)==True:
    print("This tuple is a flip flop")
else:
    print("This tuple is not a flip flop")