class Customer:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
    # using dunder method _str_ to return customer information
    def __str__(self):
        return f'Customer Info.: \nName: {self.name}\nAddress: {self.address}'


if __name__ == '__main__':
    # Creating customer class object
    customer1 = Customer('MBABAZI', 'KIRA')
    # Printing customer information
    print(customer1)