while True:
    username = input("กรุณาระบุ Username ของท่าน: ")
    password = input("กรุณาระบุรหัสผ่านของท่าน: ")
    if username == "admin" and password == "1234" :
        print("================================")
        print("        ร้าน My Shop ยินดีต้อนรับ")
        break
    else:
        print("Username หรือ Password ไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง")
print("================================")
print("รายการสินค้าของเรามีดังนี้: ")
print("หมายเลขสินค้า           รายการสินค้า               ราคา(บาท/ชิ้น)")
print("   1                    CD                      150")
print("   2                เทป Cassette                80")
print("   3                เครื่องเล่นเพลงMP3แบบพกพา       2000")
print("   4                เครื่องเล่นเทป Cassette         1000")
print("==================================================")
total_price = 0
while True:
 selected_item = str(input("กรุณาระบุหมายเลขสินค้าที่ท่านต้องการ หรือ พิมพ์'ครบ'เพื่อชำระเงิน: "))
 if selected_item == "1":
    quantity = int(input("กรุณาระบุจำนวนของสินค้า: "))
    total_price += 150 * quantity
 if selected_item == "2":
    quantity = int(input("กรุณาระบุจำนวนของสินค้า: "))
    total_price += 80 * quantity
 if selected_item == "3":
    quantity = int(input("กรุณาระบุจำนวนของสินค้า: "))
    total_price += 2000 * quantity
 if selected_item == "4":
    quantity = int(input("กรุณาระบุจำนวนของสินค้า: "))
    total_price += 1000 * quantity
 if selected_item == "ครบ":
        break
 else:
     print("ไม่มีหมายเลขสินค้าที่ท่านเลือก กรุณาระบุใหม่อีกครั้ง")
print("=======================================")
print("ยอดที่ท่านต้องชำระทั้งหมด: " + str(total_price) +" "+"บาท")
print("=======================================")