print("-PRICE LIST-")
print("Pepsi Medium = $2.25")
print("Coke Medium = $1.75")
print("Fanta Medium = $1.80")
print("Sprite Medium = $1.70")

print("----------------------------------------------")

cost = float(input("Input the drink cost: "))
give = float(input("Type Amount given: "))

while cost <= 0:
    cost = float(input("Drink cost should be more than 0: "))

while give <= cost or give <= 0:
    give = float(input("Amount paid should be equal or more than cost: "))

print("----------------------------------------------")

coins=[]

change = (give - cost)
change2 = change-int(change)
change2 = round(change2,2)*100
coin = [50,25,10,5,1]
for c in coin:
    while change2>=c:
        coins.append(c)
        change2 = change2-c
    
half=coins.count(50)
quarter = coins.count(25)
dime=coins.count(10)
nickel =coins.count(5)
pen=coins.count(1)

dollars = int(change)
if half !=0 or quarter != 0 or dime!=0 or nickel!=0 or pen!=0:
    print ('The change of', round(give,2), 'is:','%.2f'%change, '\n-dollars:',dollars,'\n-halfs(50):',half,'\n-quarters(25):',quarter,'\n-dime(10):',dime,'\n-nickels(5):',nickel,'\n-pennies(1):',pen)
else:
     print ('The change from', round(give,2), 'is:',change,'and no coins')


print("----------------------------------------------")


print("THANK YOU FOR ORDERING!")