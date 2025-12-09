#1
class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
    def action(self):
        return f'{self.name} готов к бою!'
#2
class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp
    def action(self):
        return f'Маг {self.name} кастует заклинание! MP: {self.mp}'
class WarriorHero(MageHero):
    def action(self):
        return f'Воин {self.name} рубит мечом! Уровень: {self.lvl}'
#3
class BankAccount:
    def __init__(self, hero, bank_name, balance, password):
        self.hero = hero
        self.bank_name = bank_name
        self._balance = balance
        self.__password = password
    def login(self, password):
        if password == self.__password:
            return True
        return 'You entered the wrong password, try again'
    def full_info(self):
        return f'{self.hero.name} has {self._balance} on the bank account'
    def get_bank_name(self):
        return self.bank_name
    def bonus_for_level(self):
        return f'Your bonus for level is {self.hero.lvl * 10}'
#4
    def __str__(self):
        return f'{self.hero.name} | Баланс: {self._balance} SOM'

    def __add__(self, other):
        if type(self.hero) == type(other.hero):
            return self._balance + other._balance
        return False


    def __eq__(self, other):
        if self.hero.name == other.hero.name and self.hero.lvl == other.hero.lvl:
            return True
        return False

#5
from abc import ABC, abstractmethod
class SmsService(ABC):
    @abstractmethod
    def send_otp(self,phone):
        pass
class KGSms(SmsService):
    def send_otp(self,phone):
        return f'<text>Код: 1234</text><phone>{phone}</phone>'
class RUSms(SmsService):
    def send_otp(self,phone):
        return f'{"text": "Код: 1234", "phone": "{phone}"}'

mage1 = MageHero("Merlin", 80, 500, 150)
mage2 = MageHero("Merlin", 80, 500, 200)
warrior = WarriorHero("Conan", 50, 900, 20)

acc1 = BankAccount(mage1, 'mbank', 5000, "1234")
acc2 = BankAccount(mage2, 'mbank',3000, "0000")
acc3 = BankAccount(warrior,'mbank', 2500, "1111")

print(mage1.action())
print(warrior.action())

print(acc1)
print(acc2)

# --- Классовые и статические методы ---
print("Банк:", acc1.get_bank_name())
print("Бонус зауровень:", acc1.bonus_for_level(), "SOM")

# --- Магические методы: __add__ ---
print("\n=== Проверка __add__ ===")
print("Сумма счетов двух магов:", acc1 + acc2)

print("Сумма мага и воина:", acc1 + acc3)

# --- Магический метод: __eq__ ---
print("\n=== Проверка __eq__ ===")
print("Mage1 == Mage2 ?", acc1 == acc2)  # True — одинаковое имя и уровень
print("Mage1 == Warrior ?", acc1 == acc3)  # False

# --- SMS ---
sms = KGSms()
print(sms.send_otp("+996777123456"))






