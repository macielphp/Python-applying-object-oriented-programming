class Restaurant: 
    restaurants = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._active = False #_active is a private attribuite.
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f'{self.name} | {self.category}'
    
    def list_restaurants(): 
        print(f'{"Restaurant's name".ljust(25)} | {"Category".ljust(25)} | {"Status"}')
        for restaurant in Restaurant.restaurants:
            print(f'{restaurant.name.ljust(25)} | {restaurant.category.ljust(25)} | {restaurant.active}') 
    @property
    def active(self):
        return '✅' if self._active else '❌'

restaurant_park = Restaurant('Park', 'Gormet')
restaurant_pizza = Restaurant('Pizza Mix', 'Brazilian')
restaurant_dutto = Restaurant('Dutto', 'Italian')

Restaurant.list_restaurants()
 