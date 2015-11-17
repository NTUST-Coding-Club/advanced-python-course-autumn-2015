from .common import *

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.mp = 100
        self.power = 100
        self.bag = []

    def eat(self, food):
        print('%s ate %s' % (self, food))

    def attack(self, target):
        print('%s attacked %s' % (self, target))
        target.be_attacked(self)
        if target.hp <= 0:
            print('%s is dead' % target)
        else:
            print('* %s [ %d ]' % (target, target.hp))

    def be_attacked(self, from_):
        if randint(1, 2) == 1:
            print('%s 閃過了攻擊' % self)
        else:
            self.hp -= from_.power
            print('%s 被 %s 攻擊，損傷 %d' % (self, from_, from_.power))

    def recv_item(self, item):
        print('%s get %s' % (self, item))
        self.bag.append(item)

    def __str__(self):
        return Fore.GREEN + 'Player %s' % self.name + Fore.RESET
