from .common import *

def hp_bar(hp_now, hp_max, bar_size = 20):
    percentage = hp_now * 100 // hp_max

    color = Fore.GREEN
    if percentage < 70:
        color = Fore.YELLOW
    if percentage < 50:
        color = Fore.MAGENTA
    if percentage < 10:
        color = Fore.RED

    block_count = int(percentage / (100 / bar_size))
    bar = '%s[%s]%s' % (color, ("=" * block_count).ljust(bar_size), Fore.RESET)
    bar += " (%d%% %d/%d)" % (percentage, hp_now, hp_max)
    print(bar)

def show_status(who):
    print('%s' % who)
    hp_bar(who.hp, who.max_hp)

def test_hp_bar():
    hp_bar(9, 100)
    hp_bar(33, 100)
    hp_bar(66, 100)
    hp_bar(99, 100)
