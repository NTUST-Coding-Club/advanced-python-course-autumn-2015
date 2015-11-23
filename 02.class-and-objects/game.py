import random
import RPG
from colorama import Fore


def hp_bar(hp_now, hp_max):
    BAR_SIZE = 20
    """ [=====        ] (44% 44/100) """
    percentage = hp_now * 100 // hp_max

    color = Fore.GREEN
    if percentage < 70:
        color = Fore.YELLOW
    if percentage < 50:
        color = Fore.MAGENTA
    if percentage < 10:
        color = Fore.RED

    block_count = int(percentage / (100 / BAR_SIZE))
    bar = '%s[%s]%s' % (color, ("=" * block_count).ljust(BAR_SIZE), Fore.RESET)
    bar += " (%d%% %d/%d)" % (percentage, hp_now, hp_max)
    print(bar)

# hp_bar(9, 100)
# hp_bar(33, 100)
# hp_bar(66, 100)
# hp_bar(99, 100)
# exit()

def show_status(who):
    print('%s' % who)
    hp_bar(who.hp, who.max_hp)

def battle(player):
    monster_list = [ RPG.Pig, RPG.Cow, RPG.Cow, RPG.Cow, RPG.Cow ] #, RPG.SlanderMan ]
    monster_type = random.choice(monster_list)
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

def play_game():
    name = input('取個名字吧，勇者：')
    player = RPG.Player(name)

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
        action = menu[act_number]
        action(player)

play_game()
