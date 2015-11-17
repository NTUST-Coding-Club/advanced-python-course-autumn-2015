from .common import *

class Monster(object):
    def __init__(self, name):
        self.name = name
        self.hp = 10
        self.power = 1

    def be_attacked(self, from_):
        self.hp -= from_.power
        if randint(1, 1) == 1:
            self.fight_back(from_)

    def fight_back(self, target):
        target.be_attacked(self)

    def __str__(self):
        return Fore.RED + 'Monster %s' % self.name + Fore.RESET

class Pig(Monster):
    def __init__(self):
        super().__init__('Pig')
        self.hp = 3
        self.power = 1

    def be_attacked(self, from_):
        super().be_attacked(from_)
        if self.hp <= 0:
            if randint(1, 3) == 1:
                from_.recv_item(Fore.BLUE + '豬肉' + Fore.RESET)

class Cow(Monster):
    def __init__(self):
        super().__init__('Cow')
        self.hp = 6
        self.power = 2

    def be_attacked(self, from_):
        super().be_attacked(from_)
        if self.hp <= 0:
            if randint(1, 6) == 1:
                from_.recv_item(Fore.YELLOW + '神裝 (+9999)' + Fore.RESET)
            if randint(1, 3) == 1:
                from_.recv_item(Fore.BLUE + '生牛排' + Fore.RESET)
