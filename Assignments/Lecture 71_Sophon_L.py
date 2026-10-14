menulist = []
pricelist = []
def showbill ():
    print("--- My Food ---")
    for number in range(len(menulist)):
        print(menulist[number], pricelist[number])
    total = sum(pricelist)
    print("Total: ", total, "Baht")
while True:
    menuname = input("Please enter selected menu: ")
    if (menuname.lower() == "exit"):
        break
    else:
      menuprice = float(input("Price: "))
      menulist.append(menuname)
      pricelist.append(menuprice)
showbill()

