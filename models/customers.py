class Customer:
    customers = []  # Class-level list to store all customers
    def __init__ (self, name, table):
        self.name = name
        self.table = table
        Customer.customers.append(self)  # Add the new customer to the list
    
    def __str__(self):  
        return f'{self.name} | {self.table}' # String representation of a customer
    
    def list_customers(self):
        for customer in Customer.customers:
            print(f'{customer.name} | {customer.table}')  # Print each customer's name and table

# Create instances of Customer
customer_maciel = Customer('Maciel', 3)
customer_julian = Customer('Julian', 5)

# List all customers
customer_maciel.list_customers() # This will print all customers

# Print a specific customer
print(f'Details of {customer_julian.name}:\n{customer_julian}')  # Using __str__ to print the details of customer_julian