class Enemy:

    def __init__(self, typeOfEnemy, healthPoints, attackDamage):
        self.__typeOfEnemy = typeOfEnemy
        self.healthPoints = healthPoints
        self.attackDamage = attackDamage

    def get_typeOfEnemy(self):
        return self.__typeOfEnemy
    
    def talk(self):
        print(f"I am a {self.__typeOfEnemy}. Be prepared to fight!")
    
    def walk(self):
        print(f"{self.__typeOfEnemy} moves closer to you.")
    
    def attack(self):
        print(f"{self.__typeOfEnemy} attack for {self.attackDamage} damage.")

    def specialAttack(self):
        print("Enemy do not have any special attack.")