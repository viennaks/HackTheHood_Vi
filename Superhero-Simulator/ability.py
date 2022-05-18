import random


class Ability:
    def __init__(self, name='Ability/Weapon', max_damage=100):
        self.name = name
        self.max_damage = max_damage

def __repr__(self):
        return f"Ability({self.name}, {self.max_damage})"
    
def attack(self):
            attack_value = random.randrange(0,self.max_damage)
            message = f'{self.name}: attack is {attack_value}'
            
            print(attack_value)
            return attack_value





