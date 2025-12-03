class Animal:
    def __init__(self, name: str, age: int, health: int):
        self.name = name
        self.age = age
        self.health = health
    def info(self) -> str:
        return f"{self.name}, {self.age} лет, здоровье {self.health}"
    def use_ability(self) -> str:
        return f"{self.name} использует базовую способность."
class Flyable:
    def use_ability(self):
        ability = super().use_ability()
        return f"{ability} летает."

class Swimmable:
    def use_ability(self):
        ability = super().use_ability()
        return f'{ability} плавает.'
class Invisible:
    def use_ability(self):
        ability = super().use_ability()
        return f'{ability} становится невидимым'
class Duck(Flyable, Swimmable, Animal):
    def conclusion(self):
        return f'{self.use_ability()} '
a = Duck('donald', 2, 90)
print(a.conclusion())

