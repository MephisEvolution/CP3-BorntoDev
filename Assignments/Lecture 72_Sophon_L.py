menulist = []
def showbill ():
    print("--- My Food ---")
    for number in range(len(menulist)):
        print(menulist[number])
    total = sum(item [1] for item in menulist)
    print("Total: ", total, "Baht")
while True:
    menuname = str(input("Please enter selected menu: "))
    if (menuname.lower() == "exit"):
        break
    else:
      menuprice = float(input("Price: "))
      menulist.append([menuname,menuprice])
showbill()