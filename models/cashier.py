from typing import List
from models.toggleable import Toggleable  # Import the Toggleable class
from utils.print_helper import print_table  # Import the print_table function


class Cashier(Toggleable):  # Inherit from Toggleable for status management
    cashiers: List['Cashier'] = []  # Type hint for cashiers as a list of Cashier objects

    def __init__(self, team_member: str, customer_name: str, table: str, amount: int):
        super().__init__()  # Initialize Toggleable to manage the _paid status
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
        Cashier.cashiers.append(self)

    def __str__(self) -> str:
        return f'{self._team_member.ljust(15)} | {self._customer_name.ljust(15)} | {self._table.ljust(10)} | {self._amount:,.2f}'

    @property
    def amount(self) -> int:
        return self._amount

    @classmethod
    def list_cashiers(cls) -> None:
        headers = ['Atendent', 'Customer\'s name', 'Table', 'Amount', 'Paid']
        rows = [[cashier._team_member, cashier._customer_name, cashier._table, f"${cashier._amount:,.2f}", cashier.active] 
                for cashier in cls.cashiers]
        print_table(headers, rows)  # Use the print_table function for cleaner output

    @classmethod
    def remove_cashier(cls, cashier_to_remove: 'Cashier') -> None:
        cls.cashiers = [cashier for cashier in cls.cashiers if cashier != cashier_to_remove]

    # The toggle_paid method is no longer needed, as it's inherited from Toggleable.
