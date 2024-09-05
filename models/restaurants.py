class Restaurant: 
    name = ''
    category = ''
    active = False

restaurant_park = Restaurant()
restaurant_park.name = 'Park'
restaurant_park.category = 'Gourmet'
restaurant_pizza = Restaurant()

restaurants = [restaurant_park, restaurant_pizza]
print(restaurant_park.name)
