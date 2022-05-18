import random
from hero import *

class Team:

    def __init__(self, name="Hero Team"):
        self.name = name
        self.members = []
        self.living_members = []
        self.team_deaths = 0
        self.team_kills = 0

    def __repr__(self):
        return f"Team({self.name}, {self.members})"

    def add_death(self):
        self.team_deaths += 1
        message = f'A member of {self.name} has died!'

        print(message)
        return message

    def add_kill(self):
       
        self.team_kills += 1
        message = f'A member of {self.name} has defeated an opponent!'

        print(message)
        return message


    def add_hero(self, *args):
        new_heroes = 0

        for hero in args:

            if hero not in self.members:
                new_heroes += 1
                self.members.append(hero)
                self.living_members.append(hero)
    

    def view_all_heroes(self):
        

        if not self.members:
            message = "There are no members on this team."

            print(message)
            return message
        
        else:

            for hero in self.members:
                message = f'{hero.name} is on team {self.name}'
                print(message)

            return self.members

    
    def attack(self, team):
        
        battling = True

        while battling:

            if not self.living_members or not team.living_members:
                message = "One or more teams do not have any members."
                
                print(message)
                battling = False

            team_member = random.choice(self.living_members)
            opponent = random.choice(team.living_members)

            print(f"\n\n\n{self.name}'s {team_member.name} will now battle {team.name}'s {opponent.name}!\n\n\n")

            winner = team_member.battle(opponent)

            if winner == team_member:
                self.add_kill()
                team.add_death()
                team.living_members.remove(opponent)

            elif winner == opponent:
                self.add_death()
                self.living_members.remove(team_member)
                team.add_kill()

            if self.living_members and not team.living_members:
                message = f'{self.name} has defeated {team.name}!'

                print(message)
                battling = False

            elif not self.living_members and team.living_members:
                message = f'{team.name} has defeated {self.name}!'

                print(message)
                battling = False


