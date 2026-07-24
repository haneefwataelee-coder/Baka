numstr = ""
while numstr != "0":
    numstr = input("Enter integer number (0-exit) :")
    if numstr == "0" :
        break
    else: # !=0
        pass
    for c in numstr:
        print(c)

print("Exit Program")
