store_item_names=["pencil", "eraser", "pen", "notebook", "stapler"]
matching_stock=[5,1,10,0,2]
stock={}
stock=dict(zip(store_item_names,matching_stock))
print(stock)
in_stock={item:count for item,count in stock.items() if count>0}
shop=input("What item would you like to buy? ")
if shop not in in_stock:
    exit()
prices=[10,60,3,7,9]
markup=int(input("Enter markup price to add: "))
markuped=list(map(lambda p:p+markup,prices))
print("Mark uped prices:",markuped)