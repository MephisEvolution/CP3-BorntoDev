totalprice = int(input("Enter your product price: "))
def vatcalculate (totalprice):
    result = totalprice+(totalprice*7/100)
    return result
print(vatcalculate(totalprice))