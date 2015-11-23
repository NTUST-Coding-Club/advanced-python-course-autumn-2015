from colorama import Fore

# c9.io 中執行：sudo pip3 install colorama

class Test:
    def __init__(self):
        self.a = 'a'
        self.b = 'b'

print(list(Test().__dict__)) # ['a', 'b']

print(list(Fore.__dict__)) # 兩個底線
print(Fore.RED + '紅色文字')
print(Fore.LIGHTBLUE_EX + '淺藍色文字' + Fore.RESET)
print(Fore.MAGENTA + 'MAGENTA' + Fore.RESET)

for color in Fore.__dict__: # Fore.__dict__ 是個 dict 物件
    # 裡面有所有的色彩名稱

    # getattr(a, "b") 等同 a.b
    print(getattr(Fore, color) + 'a', end='')
print(Fore.RESET)
