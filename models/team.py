class Team:
    team = []
    def __init__(self, name, tables, active=False):
        self.name = name
        self.tables = tables
        self.active = active
        Team.team.append(self)

    def __str__(self):
        print(f'Name: {self.name} | Table(s): {self.tables}')

    def list_active_members():
        for member in Team.team:
            if member.active == True:
                print(f"Member's name: {member.name}\nResponsible for table(s) number: {member.tables}\nActive: {member.active}\n-----------------------------")

team_member_marcos = Team('Marcos', [3, 5], True)
team_member_bruno = Team('Bruno', [6, 7, 8], True)
team_member_pedro = Team('Pedro', [10, 11, 12], False)

Team.list_active_members()
