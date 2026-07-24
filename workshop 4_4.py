print("Show Menu\n============")
print("1. Menu 1\n2. Menu 2\n3. Menu 3\n4. Exit")
chioce = input("Enter Choice : ")
match chioce:
    case "1":
        print("Choice 1")
    case "2":
        print("Choice 2")
    case "3":
        print("Choice 3")
    case "4":
        print("Choice Exit ")
    case _:
        print("Eror no Choice")
