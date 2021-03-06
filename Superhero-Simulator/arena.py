from ability import *
from weapon import *
from armor import *
from hero import *
from team import *

class Arena:

    def __init__(self):
        self.team_one = None
        self.team_two = None

    def __repr__(self) -> str:
        return f"Battle Simulator Arena"

    def create_ability(self, num):
     
        name = input(f"\nWhat is ability {num + 1}'s name?:  ")
        max_damage = input(f"What is the max damage of {name}?:  ")

        return Ability(name, int(max_damage))

    def create_weapon(self, num):
        ''' Prompt user for Weapon information. return Weapon with values from user input. This method will allow a user to create a weapon. Prompt the user for the necessary information to create a new weapon object.
        '''

        name = input(f"\nWhat is weapon {num + 1}'s name?:  ")
        max_damage = input(f"What is the max damage of {name}?:  ")

        return Weapon(name, int(max_damage))

    def create_armor(self, num):
        ''' Prompt user for Armor information return Armor with values from user input. This method will allow a user to create armor. Prompt the user for the necessary information to create a new armor object. 
        '''

        name = input(f"\nWhat is the name of armor piece #{num + 1}?:  ")
        max_defense = input(f"What is the max defense of {name}?:  ")

        return Armor(name, int(max_defense))

    def create_hero(self, num):
        

        hero_name = input(f"\nHero #{num + 1}'s name:  ")
        hero_health = input(f"{hero_name}'s health (Enter a number, try 1000 for a default value):  ")

        hero = Hero(hero_name, int(hero_health))

        add_item = None

        while add_item != "4":
            add_item = input(f"\nPress any of the following numbers to perform the corresponding action:\n[1] Give {hero.name} an ability\n[2] Give {hero.name} a weapon\n[3] Give {hero.name} armor\n[4] Done adding items\n\nYour choice:  ")
            
            if add_item == "1":
                number = int(input(f"How many abilities do you want to give {hero.name}?:  "))

                for num in range(number):
                    ability = self.create_ability(num)
                    hero.add_abilities(ability)

            elif add_item == "2":
                number = int(input(f"How many weapons will {hero.name} have?:  "))

                for num in range(number):
                    weapon = self.create_weapon(num)
                    hero.add_weapons(weapon)

            elif add_item == "3":
                number = int(input(f"How many pieces of armor will {hero.name} have?:  "))

                for num in range(number):
                    armor = self.create_armor(num)
                    hero.add_armors(armor)

        return hero

    def build_team_one(self):
        ''' Prompt the user to build team_one. This method should allow a user to create team one. Prompt the user for the number of Heroes on team one, call self.create_hero() for every hero that the user wants to add to team one. 
        '''
        
        name_of_team = input("\nWhat is team one's name?:\n")
        self.team_one = Team(name_of_team)

        number_on_team = int(input(f"\nHow many members would you like on {name_of_team}?:\n"))

        for i in range(number_on_team):
            hero = self.create_hero(i)
            self.team_one.add_hero(hero)

        message = f"Team One: {name_of_team} has been created!"

        print(message)
        return message

    def build_team_two(self):
        ''' Prompt the user to build team_two. This method should allow a user to create team two. Prompt the user for the number of Heroes on team two, call self.create_hero() for every hero that the user wants to add to team two. 
        '''
        
        name_of_team = input("\nWhat is team two's name?:\n")
        self.team_two = Team(name_of_team)

        number_on_team = int(input(f"\nHow many members would you like on {name_of_team}?:\n"))

        for i in range(number_on_team):
            hero = self.create_hero(i)
            self.team_two.add_hero(hero)

        message = f"Team Two: {name_of_team} has been created!"

        print(message)
        return message

    def team_battle(self):
        ''' Battle team_one and team_two together.'''
        self.team_one.attack(self.team_two)

    def show_stats(self):
        ''' Prints team statistics to terminal. This method should print out battle statistics including each team's average kill/death ratio. Required Stats: Show surviving heroes,Declare winning team, Show both teams average kill/death ratio.
        '''
        print(f"\n\n\nBattle Stats:\n\n\n")

        # based on the number of alive heroes on each team we can declare which team is winning

        team1_alive = 0
        team2_alive = 0

        for hero in self.team_one.living_members:
            team1_alive += 1
            print(f"{hero.name} on {self.team_one.name} is still alive.")
        
        print("\n")
        
        for hero in self.team_two.living_members:
            team2_alive += 1
            print(f"{hero.name} on {self.team_two.name} is still alive.")

        if team1_alive > team2_alive:
            current_winner = self.team_one.name
        else:
            current_winner = self.team_two.name

        
        print(f"\n{self.team_one.name}'s remaining heroes: {team1_alive}")
        print(f"{self.team_two.name}'s remaining heroes: {team2_alive}\n")
        print(f"Currently Winning: {current_winner}\n")

        # displaying individual hero stats from each team
        print(f"\n{self.team_one.name}'s Heroes' Stats:\n")

        total_kills = 0
        total_deaths = 0

        for hero in self.team_one.members:

            total_kills += hero.kills
            total_deaths += hero.deaths

            print(f"{hero.name} has won {hero.kills} battles and has lost {hero.deaths} battles.")

        
        print(f"\n{self.team_one.name}'s Victories: {total_kills}")
        print(f"{self.team_one.name}'s Defeats: {total_deaths}")

       
        if self.team_one.team_deaths == 0:

            print(f"{self.team_one.name}'s Average Kill/Death Ratio: {(self.team_one.team_kills // 1)}\n")
        else:
            print(f"{self.team_one.name}'s Average Kill/Death Ratio: {(self.team_one.team_kills // self.team_one.team_deaths)}\n")

        
        print(f"\n{self.team_two.name}'s Heroes' Stats:\n")

        total_kills2 = 0
        total_deaths2 = 0

        for hero in self.team_two.members:

            total_kills2 += hero.kills
            total_deaths2 += hero.deaths

            print(f"{hero.name} has won {hero.kills} battles and has lost {hero.deaths} battles.")

        print(f"\n{self.team_two.name}'s Victories: {total_kills2}")
        print(f"{self.team_two.name}'s Defeats: {total_deaths2}")

        if self.team_two.team_deaths == 0:

            print(f"{self.team_two.name}'s Average Kill/Death Ratio: {(self.team_two.team_kills // 1)}\n")
        else:
            print(f"{self.team_two.name}'s Average Kill/Death Ratio: {(self.team_two.team_kills // self.team_two.team_deaths)}\n")


game_is_running = True

arena = Arena()


print("\nWelcome to the Superhero Battle Simulator! Here you can create and fully customize your own warriors with custom abilities, weapons, and armor! You can then put your heroes on teams and have them do battle against each other! Follow the prompts and have fun! May you be victorious!\n\n\n")


arena.build_team_one()
arena.build_team_two()


while game_is_running:


    arena.team_battle()


    arena.show_stats()

    play_again = input("\nPlay Again? Y or N:  ")

    
    if play_again.lower() == "n":
        game_is_running = False

    else:
       
        arena.team_one.revive_team()
        arena.team_two.revive_team()
