from utils.print_helper import print_table
from models.toggleable import Toggleable

class Team(Toggleable):  # Inherit from Toggleable to manage active status
    team = []

    def __init__(self, name, tables):
        super().__init__() # Initialize Toggleable for the _active status
        self._name = name.title()
        self._tables = tables #It is a list
        Team.team.append(self)

    def __str__(self):
        tables_str = ', '.join(map(str, self._tables)) #Convert list to a comma-separated string
        return(f'{self._name.ljust(10)} | {tables_str.ljust(10)}')

    @classmethod
    def list_members(cls):
        headers = ["Member's name", "Responsible for table", "Working"]
        rows = [[member._name, member._tables, member.active]
            for member in cls.team]
        print_table(headers, rows)  # Use print_table for clean output

