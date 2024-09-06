class Customer:
    customers = []  # Class-level list to store all customers

    def __init__(self, name, table):
        self._name = name
        self._table = table
        self._paid = False
        Customer.customers.append(self)  # Add the new customer to the list
    
    def __str__(self):
        return f'{self._name.ljust(25)} | {self._table.ljust(25)}'
    
    @classmethod
    def list_customers(cls):
        print(f'{"Customer\'s name".ljust(25)} | {"Table\'s number".ljust(25)} | {"Bill\'s paid"}')
        for customer in cls.customers:
            # Use the property `paid` to display '✅' or '☐'
            print(f'{customer._name.ljust(25)} | {customer._table.ljust(25)} | {customer.paid}')

    @property
    def paid(self):
        return '✅' if self._paid else '☐'

    def alter_paid(self):
        self._paid = not self._paid  # Toggles the payment status

# Create instances of Customer
customer_maciel = Customer('Maciel', "3")
customer_julian = Customer('Julian', "5")

# Change the payment status of customer Julian
customer_julian.alter_paid()

# List all customers
Customer.list_customers()  # This will now show '✅' or '☐' for the paid status
