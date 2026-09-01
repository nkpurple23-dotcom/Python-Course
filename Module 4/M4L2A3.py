weather=(1,0,0,0,1,1,0)
sunny=0
rainy=0
for i in weather:
    if i==1:
        rainy+=1
    else:
        sunny+=1
if sunny>rainy:
    print("Today has good weather")
else:
    print("Today has bad weather")