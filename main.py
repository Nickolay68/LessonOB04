from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass
class Sword(Weapon):
    def attack(self):
        return "наносит удары мечом!"

class Bow(Weapon):
    def attack(self):
        return "выпускает стрелу из лука!"
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} оборудовал {type(weapon).__name__}.")

    def attack(self):
        if self.weapon:
            print(f"{self.name} {self.weapon.attack()}")
        else:
            print(f"{self.name} пытается напасть, но у него нет оружия!")
class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            print(f"{self.name} имеет {self.health} здоровье ушло.")
        else:
            print(f"{self.name} потерпел поражение!")

def battle(fighter: Fighter, monster: Monster):
    print(f"\nДикий {monster.name} появляется!")
    while monster.health > 0:
        fighter.attack()
        monster.take_damage(10)  # Урон фиксированный для простоты
        if monster.health > 0:
            print(f"The {monster.name} атакует в ответ!")
        else:
            print(f"{fighter.name} победил  {monster.name}!")

# Пример использования

# Создаем бойца и монстра
hero = Fighter("Наш герой Ваня")
goblin = Monster("Goblin", 30)

# Выбираем оружие
sword = Sword()
bow = Bow()

# Меняем оружие и начинаем бой
hero.change_weapon(sword)
battle(hero, goblin)

# Сменим оружие и снова начнем бой
hero.change_weapon(bow)
goblin = Monster("Goblin", 30)  # Новый монстр
battle(hero, goblin)

