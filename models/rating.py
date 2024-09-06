from models.customer import Customer

class Rating:
    def __init__(self, customer: Customer, rating):
        if not isinstance(rating,(int, float)) or not (0 <= rating <= 5):
            raise ValueError('Rating must be a number between 0 and 5.')
        self._customer = customer.name # Access customer's name from the Customer object
        self._rating = rating

    def __str__(self):
        return f"Customer: {self._customer}, Rating: {self._rating}"

    @property
    def customer(self):
        return self._customer
    
    @property
    def rating(self):
        return self._rating
