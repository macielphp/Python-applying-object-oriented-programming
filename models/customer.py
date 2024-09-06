from models.toggleable import Toggleable # Import Toggleable for managing status
from utils.print_helper import print_table  # Import print_table for displaying tables

class Customer(Toggleable):
    customers = []  # Class-level list to store all customers

    def __init__(self, name, table):
        super().__init__()  # Initialize Toggleable for _paid status management
        self._name = name
        self._table = table
        self._paid = False
        Customer.customers.append(self)  # Add the new customer to the list
    
    def __str__(self):
        return f'{self._name.ljust(25)} | {self._table.ljust(25)}'
    
    @property
    def name(self):
        return self._name #Give access to Customer's name

    @classmethod
    def list_customers(cls) -> None:
        headers = ["Customer's name", "Table's number", "Bill's paid"]
        rows = [[customer._name, customer._table, customer.active]
            for customer in cls.customers]
        print_table(headers, rows)

