class FirstClass:
    """
    FirstClass('myname')
    FirstClass('your name', 'M')  # or 'F'
    """
    def __init__(self, name, gender=''):
        self.name = name
        self.gender = gender
        print('Hello, %s' % name)

    def say_hi(self):
        print('Hi, I am %s' % self.name)

    def intro(self):
        name = self.name_with_prefix()
        print('This is %s' % name)

    def name_with_prefix(self):
        if self.gender == 'M':
            return 'Mr. %s' % self.name
        elif self.gender == 'F':
            return 'Ms. %s' % self.name
        else:
            return self.name

# obj = FirstClass('Inndy', 'M')
obj = FirstClass('AAABCD')
obj.a = "This is obj.a"
# obj.name = 'AAAAAAA'
obj.intro()

print(obj.a)
# print(obj)
print('Name is %s' % obj.name)
obj.say_hi()

for i in range(10): print()
