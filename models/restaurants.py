class Restaurant: 
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.active = False
        

restaurant_park = Restaurant('Park', 'Gormet')
restaurant_pizza = Restaurant('Pizza Mix', 'Brazilian')
restaurant_dutto = Restaurant('Dutto', 'Italian')


restaurants = [restaurant_park, restaurant_pizza, restaurant_dutto]

print(vars(restaurant_park))
print(vars(restaurant_dutto))
print(vars(restaurant_pizza))
