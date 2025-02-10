from Hero import *
from Weapon import *
from Enemy import *
from Zombie import *
from Ogre import *

def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.healthPoints > 0 and e2.healthPoints > 0:
        print("-----------------------------------------------")

        e1.specialAttack()
        e2.specialAttack()
        
        print(f"{e1.get_typeOfEnemy()} has {e1.healthPoints} HP left.")
        print(f"{e2.get_typeOfEnemy()} has {e2.healthPoints} HP left.")

        e1.attack()
        e2.attack()
        e1.healthPoints -= e2.attackDamage
        e2.healthPoints -= e1.attackDamage

    print("--------RESULTS-----------------")
    if e1.healthPoints > 0:
        print(f"{e1.get_typeOfEnemy()} won the battle!!")
    elif e2.healthPoints > 0:
        print(f"{e2.get_typeOfEnemy()} won the battle!!")
    else:
        print("Both Die at same time!!")

def heroBattle(hero: Hero, enemy: Enemy):
    enemy.talk()

    while hero.healthPoints > 0 and enemy.healthPoints > 0:
        print("-----------------------------------------------")
        
        enemy.specialAttack()
        
        print(f"Hero has {hero.healthPoints} HP left.")
        print(f"{enemy.get_typeOfEnemy()} has {enemy.healthPoints} HP left.")
        
        hero.attack()
        enemy.attack()
        hero.healthPoints -= enemy.attackDamage
        enemy.healthPoints -= hero.attackDamage

    print("--------RESULTS-----------------")
    if hero.healthPoints > 0:
        print(f"Hero won the battle!!")
    elif enemy.healthPoints > 0:
        print(f"{enemy.get_typeOfEnemy()} won the battle!!")
    else:
        print("Both Die at same time!!")


zombie = Zombie(10, 1)
ogre = Ogre(20, 3)
hero = Hero(10, 1)
weapon = Weapon('Sword', 5)
hero.equipWeapon(weapon)

heroBattle(hero, ogre)