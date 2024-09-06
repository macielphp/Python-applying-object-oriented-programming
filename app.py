from models.restaurants import Restaurant

pizza_mix = Restaurant('Pizza Mix', 'Italian')
dittos_res = Restaurant('Dittos Res', 'American')
fips = Restaurant('Fips', 'Japanese')

fips.alter_status()

def main():
    Restaurant.list_restaurants()

if __name__ == "__main__":
    main()