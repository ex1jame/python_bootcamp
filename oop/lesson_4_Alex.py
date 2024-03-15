from random import randint,choice
from enum import Enum


class SuperAbility(Enum):
    HEAL = 1
    CRITICAL_DAMAGE = 2
    BOOST = 3
    SAVE_DAMAGE_AND_REVERT = 4





class GameEntity:

    def __init__(self,name,health,damage) -> None:
        self.__health = health
        self.__name = name
        self.__damage = damage
    
    @property
    def name(self):
        return self.__name
    
    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self,value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value
        
    
    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self,value):
        self.__damage = value
    
    def __str__(self) -> str:
        return f'{self.name} health: {self.health} damage: {self.damage}'

class Boss(GameEntity):
    
    def __init__(self, name, health, damage) -> None:
        super(Boss,self).__init__(name, health, damage)
        self.__defense = None

    @property
    def defense(self):
        return self.__defense
    
    def choose_defense(self,heroes):
        random_hero = choice(heroes)
        self.__defense = random_hero.super_ability

    def attack(self,heroes):
        for hero in heroes:
            if hero.health > 0:
                
                hero.health = hero.health - self.damage

    def __str__(self) -> str:
        return "BOSS" + super(Boss,self).__str__() + f' defence: {self.defense}'
    

class Hero(GameEntity):
    def __init__(self, name, health, damage,super_ability) -> None:
        super(Hero,self).__init__(name, health, damage)
        self.__super_ability = super_ability

    
    @property
    def super_ability(self):
        return self.__super_ability

    def attack(self,boss):
        boss.health -= self.damage
    
    def apply_super_power(self,boss,heroes):
        pass

class Warrior(Hero):
    def __init__(self, name, health, damage) -> None:
        super(Warrior,self).__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self,boss,heroes):
        coeficent = randint(2,5)
        boss.health = boss.health - coeficent * self.damage
        print(f'warrior {coeficent * self.damage}')

class Magic(Hero):
    def __init__(self, name, health, damage) -> None:
        super(Magic,self).__init__(name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self,boss,heroes):
        coeficent = randint(2,3)
        boss.health = boss.health - coeficent * self.damage
        print(f'magic {coeficent * self.damage}')

class Medic(Hero):
    def __init__(self, name, health, damage,heal_points) -> None:
        super(Medic,self).__init__(name, health, damage,SuperAbility.HEAL)
        self.__heal_points =  heal_points

    @property
    def healing_capacity(self):
        return self.__heal_points

    def apply_super_power(self,boss,heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points

class Berserk(Hero):
    def __init__(self, name, health, damage) -> None:
        super(Berserk,self).__init__(name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__saved_damage = 0

    @property
    def saved_damage(self):
        return self.__saved_damage
    
    def apply_super_power(self,boss,heroes):
        if  self.saved_damage == 0:
            self.__saved_damage = boss.damage
            boss.health -= boss.damage
        else:
            boss.health -= self.saved_damage
            self.__saved_damage =  0
        return print(f'berserk {self.saved_damage}')
        

round_number = 0


def is_game_finished(boss,heroes):
    if boss.health <= 0:
        print('Heroes Won')
        return True
    
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print("Boss Won")
    return all_heroes_dead


def start_game():
    boss_azerot = Boss(' Azerot', 1000,50)
    warrior_gandolf = Warrior('Gandolf', 280, 40)
    magic_morgana = Magic('Morgana', 280, 50)
    medic_eliana = Medic('Eliana', 150, 7,30)
    medic_ela = Medic('Ela', 250, 7,14)
    berserk_nathryl = Berserk('Nathryl', 500, 15)

    heroes = [warrior_gandolf,magic_morgana,medic_eliana,medic_ela,berserk_nathryl]
    
    print_statistics(boss_azerot, heroes)
    while (not is_game_finished(boss_azerot, heroes)):
        play_round(boss_azerot,heroes)
            



def print_statistics(boss,heroes):
    print(f'ROUND ' + str(round_number) + ' ------------------')
    print(f"{boss}")
    for hero in heroes:
        print(f"{hero}")

def  play_round(boss,heroes):
    global round_number
    round_number += 1
    if boss.health > 0:
        boss.choose_defense(heroes)
        boss.attack(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 and boss.defense != hero.super_ability: 
            hero.attack(boss)
            hero.apply_super_power(boss,heroes)
    print_statistics(boss,heroes)

start_game()