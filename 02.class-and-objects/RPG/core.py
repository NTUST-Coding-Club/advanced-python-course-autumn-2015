from .common import *
from .player import Player
from .utils import *
from .monster import *

def battle(player):
    monster_list = [ Pig, Cow, Cow, Cow, Cow ] #, SlanderMan ]
    monster_type = choice(monster_list)
    monster = monster_type()

    while True:
        show_status(player)
        show_status(monster)
        print('''
0) 逃跑
1) 喝藥水
2) 攻擊
''')
        act_number = input('要做什麼呢？')
        try: act_number = int(act_number)
        except ValueError: continue

        if act_number == 0:
            print('%s %s逃跑了%s' % (player, Fore.YELLOW, Fore.RESET))
            return
        elif act_number == 2:
            player.attack(monster)

        if monster.hp <= 0:
            print('%s 戰勝了' % player)
            return

def inspect_bag(player):
    for item in player.bag:
        print('你有 %s' % item)

def start(name):
    player = Player(name)

    menu = [ exit, battle, inspect_bag ]
    while True:
        print('''
0) 離開遊戲
1) 找怪打
2) 看看背包有什麼
''')
        act_number = input('要做什麼呢？')
        try:
            act_number = int(act_number)
        except ValueError:
            continue
        except IndexError:
            continue
        if act_number == 0:
            return
        action = menu[act_number]
        action(player)
