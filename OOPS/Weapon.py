class Weapon:

    def __init__(self, weaponType, attackIncrease):
        self.__weaponType = weaponType
        self.attackIncrease = attackIncrease
    
    def get_weaponType(self):
        return self.__weaponType