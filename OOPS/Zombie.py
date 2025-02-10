import random
from Enemy import *

class Zombie(Enemy):

    def __init__(self, healthPoints, attackDamage):
        super().__init__(typeOfEnemy='Zombie', healthPoints=healthPoints, attackDamage=attackDamage)

    def talk(self):
        print("Zomibe is *..Grumbling..*")
    
    def spreadDisease(self):
        print("The Zombie is trying to spread infection")
    
    def specialAttack(self):
        didSpecialAttackWork = random.random() < 0.50
        if didSpecialAttackWork:
            self.healthPoints += 2
            print("Zombie regenerated 2 HP!")