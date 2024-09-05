class Restaurant: 
    restaurants = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.active = False
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f'{self.name} | {self.category}'
    
    def list_restaurants():
        for restaurant in Restaurant.restaurants:
            print(f'{restaurant.name} | {restaurant.category} | {restaurant.active}') 

restaurant_park = Restaurant('Park', 'Gormet')
restaurant_pizza = Restaurant('Pizza Mix', 'Brazilian')
restaurant_dutto = Restaurant('Dutto', 'Italian')

Restaurant.list_restaurants()
 