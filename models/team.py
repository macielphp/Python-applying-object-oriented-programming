class Team:
    team = []

    def __init__(self, name, tables):
        self._name = name.title()
        self._tables = tables
        self._active = False
        Team.team.append(self)

    def __str__(self):
        tables_str = ', '.join(map(str, self._tables)) #Convert list to a comma-separated string
        return(f'{self._name.ljust(10)} | {tables_str.ljust(10)}')

    @classmethod
    def list_members(cls):
        print(f'{"Member\'s name".ljust(20)} | {"Responsible for table(s) number".ljust(35)} | {"Status"}')
        for member in cls.team:
            tables_str = ', '.join(map(str, member._tables)) #Convert list to a string for proper display  
            print(f"{member._name.ljust(20)} | {tables_str.ljust(35)} | {member.active}")

    @property
    def active(self):
        return '✅' if self._active else '❌'

    def alter_status(self):
        self._active = not self._active

# Creating team members
team_member_marcos = Team('Marcos', [3, 5])
team_member_bruno = Team('Bruno', [6, 7, 8])
team_member_pedro = Team('Pedro', [10, 11, 12])

# Alter status of one member
team_member_pedro.alter_status()

# List all members
Team.list_members()

