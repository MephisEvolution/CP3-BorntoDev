class Customer:
    name =""
    lastName =""
    age = 0

    def addCart(self):
        print("Added to ",self.name,self.lastName,"'s cart")

customer1 = Customer()
customer1.name = "James"
customer1.lastName = "Mayers"
customer1.addCart()

customer2 = Customer()
customer2.name = "John"
customer2.lastName = "Dole"
customer2.addCart()

customer3 = Customer()
customer3.name = "Michael"
customer3.lastName = "Smith"
customer3.addCart()