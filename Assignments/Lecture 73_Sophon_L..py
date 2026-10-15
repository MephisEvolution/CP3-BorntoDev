systemmenu = {"บะหมี่หมูแดง" : 45, "บะหมี่เกี๊ยวกุ้งหมูแดง":40,"เกี๊ยวกุ้งน้ำ":50,"ข้าวหมูแดง":45}
menulist = []
def showbill ():
    print("--- My Food ---")
    for number in range(len(menulist)):
        print(menulist[number][0], menulist[number][1])
    total = sum(item [1] for item in menulist)
    print("Total: ", total, "Baht")
while True:
    menuname = str(input("Please enter selected menu: "))
    if (menuname.lower() == "exit"):
        break
    else:
      menulist.append([menuname,systemmenu[menuname]])
showbill()