from Weapon import *

class Hero:

    def __init__(self, healthPoints, attackDamage):
        self.healthPoints = healthPoints
        self.attackDamage = attackDamage
        self.weapon: Weapon = None
        self.isWeaponEquipped = False
    
    def equipWeapon(self, weapon: Weapon):
        if self.weapon is None and not self.isWeaponEquipped:
            self.attackDamage += weapon.attackIncrease
            self.isWeaponEquipped = True
            self.weapon = weapon.get_weaponType()
    
    def attack(self):
        print(f"Hero attack for {self.attackDamage} damage.")