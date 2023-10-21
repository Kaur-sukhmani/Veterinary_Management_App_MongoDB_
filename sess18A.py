import datetime


class Customer:

    def __init__(self):
        self.name = ""
        self.phone = ""
        self.email = ""
        self.age = 0
        self.gender = ""
        self.address = ""
        self.createdon = ""

    def read_customer_data(self):
        # self.cid = 0
        self.name = input("enter customer name: ")
        self.phone = input("enter customer phone: ")
        self.email = input("enter customer email: ")
        self.age = int(input("Enter customer age"))
        self.gender = input("enter customer gender(male/female):").lower()
        self.address = input("enter customer address: ")

        self.createdon = datetime.datetime.today()

    # datetime -> program, class, today ka function
