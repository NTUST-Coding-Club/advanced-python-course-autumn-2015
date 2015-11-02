class Human(object):
    NAME = 'human'
    def __init__(self, name):
        print('A %s named %s' % (self.__class__.NAME, name))
        self.name = name

    def eat(self, food):
        print('%s eat %s' % (self.name, food))

    def sleep(self, time):
        print('%s sleep for %s' % (self.name, time))

class Engineer(Human):
    NAME = 'engineer'
    def __init__(self, name):
        super().__init__(name)

class Coder(Engineer):
    NAME = 'coder'
    def __init__(self, name):
        super().__init__(name)

    def sleep(self, time):
        print('No, coder are debugging')
        print('Coder never sleep')

print('-- Here is a teacher --')
teacher = Human('Teacher')
teacher.eat('Apple')
teacher.sleep('an hour')


print('-- Here is a engineer --')
rock = Engineer('Rock')
rock.sleep('8 hours')

print('-- Here is Inndy --')
inndy = Coder('Inndy')
inndy.sleep('1 day')
