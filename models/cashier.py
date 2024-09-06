from typing import List

class Cashier:
    cashiers: List['Cashier'] = []  # Specify the type hint for cashiers as a list of Cashier objects

    def __init__(self, team_member: str, customer_name: str, table: str, amount: int):
        # Validate inputs
        if not isinstance(team_member, str):
            raise ValueError("team_member must be a string.")
        if not isinstance(customer_name, str):
            raise ValueError("customer_name must be a string.")
        if not isinstance(table, str):
            raise ValueError("table must be a string.")
        if not isinstance(amount, int) or amount < 0:
            raise ValueError("amount must be a positive integer.")

        self._team_member = team_member
        self._customer_name = customer_name
        self._table = table
        self._amount = amount
        self._paid = False
        Cashier.cashiers.append(self)

    def __str__(self) -> str:
        return f'{self._team_member.ljust(15)} | {self._customer_name.ljust(15)} | {self._table.ljust(10)} | {self._amount:,.2f}'

    @property
    def paid(self) -> str:
        return '✅' if self._paid else '☐'

    @property
    def amount(self) -> int:
        return self._amount

    @classmethod
    def list_cashiers(cls) -> None:
        print(f'{"Atendent".ljust(15)} | {"Customer\'s name".ljust(15)} | {"Table".ljust(10)} | {"Amount".ljust(10)} | {"Paid"}')
        for cashier in cls.cashiers:
            print(f'{cashier._team_member.ljust(15)} | {cashier._customer_name.ljust(15)} | {cashier._table.ljust(10)} | {f"${cashier._amount:,.2f}".ljust(10)} | {cashier.paid}')

    @classmethod
    def remove_cashier(cls, cashier_to_remove: 'Cashier') -> None:
        cls.cashiers = [cashier for cashier in cls.cashiers if cashier != cashier_to_remove]

    def toggle_paid(self) -> None:
        # Toggle the paid status
        self._paid = not self._paid

# Create instances of Cashier
cashier_1 = Cashier('Bruno', 'Julian', '5', 1299)
cashier_2 = Cashier('Marcos', 'Maciel', '3', 5999)

# Toggle payment status for cashiers
cashier_1.toggle_paid()
cashier_2.toggle_paid()

# List all cashiers
Cashier.list_cashiers()

# Remove a cashier and re-list
Cashier.remove_cashier(cashier_1)
print("\nAfter removing Bruno (cashier_1):")
Cashier.list_cashiers()
