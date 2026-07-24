money = int (input("Enter number money wihtdraw : ")) #1800
cash1 = money // 1000
cash2 = (money % 1000) // 500 
cash3 = (money%500) // 100

print("Cash B1000 : ",cash1 )
print("Cash B500  : ",cash2 )
print("Cash B100  : ",cash3 )