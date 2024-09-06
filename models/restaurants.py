from models.rating import Rating

class Restaurant: 
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category
        self._active = False #_active is a private attribuite.
        self._rating = [] #Stores Customers' names and ratings
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f'{self.name} | {self.category}'
    
    @classmethod
    def list_restaurants(cls): 
        print(f'{"Restaurant's name".ljust(25)} | {"Category".ljust(25)} | {"Status"}')
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {restaurant.active}') 
            
    @property
    def active(self):
        return '✅' if self._active else '❌'

    def alter_status(self):
        self._active = not self._active

    def receive_rating(self, customer, rating):
        rating = Rating(customer, rating)
        self._rating.append(rating)
