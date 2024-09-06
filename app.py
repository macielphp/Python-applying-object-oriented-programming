from models.restaurants import Restaurant
from models.customer import Customer
from models.team import Team
from models.cashier import Cashier

# Create instances of Customer for customer's name and table
customer_maciel = Customer('Maciel', "3")
customer_julian = Customer('Julian', "5")
customer_manu = Customer("Manu", "8")

# Create instace Restaurant for restaurant's name and Category
pizza_mix = Restaurant('Pizza Mix', 'Italian')
dittos_res = Restaurant('Dittos Res', 'American')
fips = Restaurant('Fips', 'Japanese')

# Insert values to the receive_rating method class of Restaurant
fips.receive_rating('Maciel', 5)
fips.receive_rating('Julian', 1)
fips.receive_rating('Manu', 4)

# Alter the status of the Restaurant's private parameter _paid to True.
fips.toggle_status()

# Creating instances for Team
team_member_marcos = Team('Marcos', [3, 5])
team_member_bruno = Team('Bruno', [6, 7, 8])
team_member_pedro = Team('Pedro', [10, 11, 12])

# Create instances of Cashier
cashier_1 = Cashier('Bruno', 'Julian', '5', 1299)
cashier_2 = Cashier('Marcos', 'Maciel', '3', 5999)

def main():
    print('List of restaurants')
    Restaurant.list_restaurants()

    print('-' * 80)
    print('List of customers')
    Customer.list_customers()

    print("-" * 80)
    print("List of Team's member")
    Team.list_members()

    print("-" * 80)
    print("List of cashiers")
    Cashier.list_cashiers()

if __name__ == "__main__":
    main()