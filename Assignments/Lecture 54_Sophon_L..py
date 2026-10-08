def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username == "admin" and password == "1234":
        return True
    else:
        return False
def showmenu():
    print("--- iShop ---")
    print("1. Vat calculator")
    print("2. Price calculator")
def menuselect():
    userselect = int(input("Enter your choice: "))
    return userselect
def vatcalculate(totalprice):
    vat = 7
    result = totalprice + (totalprice * vat / 100)
    return result
def pricecalculate():
    price1 = int(input("price of first product (THB) : "))
    price2 = int(input("price of second product (THB) : "))
    return vatcalculate(price1+price2)
print(login())
print(showmenu())
print(pricecalculate())