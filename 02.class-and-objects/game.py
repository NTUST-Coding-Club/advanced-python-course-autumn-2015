import random
import RPG

def battle(player):
    monster_list = [ RPG.Pig, RPG.Cow ]
    monster_type = random.choice(monster_list)
    monster = monster_type()
    while monster.hp > 0:
        player.attack(monster)

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
