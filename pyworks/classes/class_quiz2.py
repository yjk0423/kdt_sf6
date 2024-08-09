class Supermarket:
    def __init__(self,location,name,product,customer):
        self.location = location
        self.name = name
        self.product = product
        self.customer = customer
    def print_location(self):
        print(self.location)
    def change_category(self,prduct):
        self.product = prduct
    def show_list(self):
        print(self.product)
    def enter_customer(self):
       self.customer += 1
    def show_info(self):
        print(f"Location: {self.location}, Name: {self.name}, Product: {self.product}, Customer: {self.customer}")



super_market = Supermarket("마포구염리동", "마켓온", "음료",12)

super_market.print_location()
super_market.change_category("과자")
super_market.show_list()
super_market.enter_customer()
super_market.show_info()

