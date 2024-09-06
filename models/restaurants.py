class Restaurant: 
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category
        self._active = False #_active is a private attribuite.
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

restaurant_park = Restaurant('Park', 'Gormet')
restaurant_pizza = Restaurant('Pizza Mix', 'Brazilian')
restaurant_dutto = Restaurant('Dutto', 'Italian')

restaurant_park.alter_status()
restaurant_pizza.alter_status()

Restaurant.list_restaurants()
 