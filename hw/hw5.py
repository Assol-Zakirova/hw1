# commands_by_role = {
#    "admin": ["start", "ban", "stop"],
#    "user": ["start", "message"]
# }
# commands = ['start', 'ban', 'stop', 'message']
#
# def check_access(func):
#     def wrapper(*args, **kwargs):
#         user = args[0]
#         command = func.__name__
#
#         if command not in commands:
#             raise ValueError('Command does not exists')
#
#         if command not in commands_by_role[user.role]:
#             raise ValueError('Command is not available')
#
#         return func(*args, **kwargs)
#     return wrapper
#
# class User:
#     def __init__(self, username, role):
#         self.username = username
#         self.role = role
#
# class CommandHandler:
#     @staticmethod
#     @check_access
#     def start(user: User):
#         return f'{user.username} запустил программу '
#
#     @staticmethod
#     @check_access
#     def stop(user: User):
#         return f'{user.username} становил программу'
#
#     @staticmethod
#     @check_access
#     def ban(user: User, target: User):
#         return f'{user.username} забанил {target.username}'
#
#     @staticmethod
#     @check_access
#     def message(user: User, target: User, text: str):
#         return f'{user.username} отправил сообщение {target.username} с содержанием {text}'
#
# alice = User("Alice", "admin")
# bob = User("Bob", "user")
#
# handler = CommandHandler()
# print(handler.start(alice))
# print(handler.ban(alice, bob))
# print(handler.message(bob, alice, "Hello alice"))

#2
class BankAccount:
    default_name = "guest"
    def __init__(self, name,  bill = 0):
        self.name = name
        self.__bill = bill
    @staticmethod
    def start():
        return 'Welcome to the program'
    @classmethod
    def create_from_name(cls, bill):
        return cls(cls.default_name, 200)
    @property
    def money(self):
        return self.__bill
a = BankAccount('Assol', 10000)
print(a.start())
b  = BankAccount.create_from_name(1000)
print(b.name)
print(a.money)
