from models.rating import Rating
from models.customer import Customer
from models.toggleable import Toggleable
from utils.print_helper import print_table
from models.status import Status

class Restaurant(Toggleable): 
    restaurants = []
    valid_categories = ['Italian', 'American', 'Portuguese', 'Brazilian', 'Japanese']

    def __init__(self, name, category):
        super().__init__() # Initializes Toggleable 

        if not isinstance(name, str):  # Validation
            raise ValueError('Name must be a string.')
        if category not in self.valid_categories: # Validation
            raise ValueError(f"Category must be one of {self.valid_categories}")
        # Prevent adding duplicate customers, team members, restaurants, or cashiers
        if any(cust for cust in Customer.customers if cust.name == name): 
            raise ValueError(f"Customer with name {name} already exists.")
        self._name = name.title()
        self._category = category
        self._rating = [] #Stores Customers' names and ratings
        self._status = Status.INACTIVE
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f'{self.name} | {self.category}'
    
    @classmethod
    def list_restaurants(cls): 
        headers = ['Restaurant\'s name', 'Category', 'Rating', 'Status']
        rows = [[restaurant._name, restaurant._category, str(restaurant.average_rating), restaurant.active]
                for restaurant in cls.restaurants]
        print_table(headers, rows)
            
    @property
    def active(self):
        return self._status.value

    def toggle_status(self):
        self._status = Status.ACTIVE if self._status == Status.INACTIVE else Status.INACTIVE

    def receive_rating(self, customer_name, rating_value):
        customer = next((cust for cust in Customer.customers if cust.name == customer_name), None)  # Find the Customer object by name
        if customer is None: 
            print(f"Warning: No Customer found with name{customer_name}")
            return
        rating = Rating(customer, rating_value)
        self._rating.append(rating)


    @property
    def average_rating(self):
        if not self._rating:
            return 0
        sum_ratings = sum(rating._rating for rating in self._rating)
        rates_length = len(self._rating)
        average = round(sum_ratings / rates_length, 1) # Example: 1,2
        return average

    @classmethod 
    def add_category(cls, category): # Dinamic listing of categories
        cls.category.add(category)