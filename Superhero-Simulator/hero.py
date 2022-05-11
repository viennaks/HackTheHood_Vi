
import random

class Hero:
   

  def __init__(self, name= "Raven", starting_health = 100):

    '''Instance properties:
      name: String
      starting_health: Integer
      current_health: Integer
    '''
    
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health


  def battle(self, opponent):
    ''' Current Hero will take turns fighting the opponent hero passed in.
    '''
    heroes =[]
    heroes.append(self.name)
    heroes.append(opponent.name)

    winner = random.choice(heroes)
    for hero in heroes:
      if not hero != winner:
        loser = hero

    print(f'{winner} has defected {loser}')
    
    return winner 
  
 
hero1 = Hero("Nitro Storm")
hero2 = Hero("Dexter Speed")
hero1.battle(hero2)

     
   
