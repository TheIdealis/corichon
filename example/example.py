from cornichon import load_all, save_all

class SubSubClass:
    def __init__(self):
        self.value = 1

    save_all = save_all
    load_all = load_all

class SubClass:
    def __init__(self):
        self.value = 1
        self.ssc = SubSubClass()

    save_all = save_all
    load_all = load_all

class SubClass2:
    def __init__(self):
        self.value = 1
        self.ssc = SubSubClass()

    save_all = save_all
    load_all = load_all

class TestClass:
    def __init__(self):
        self.d = SubClass()
        self.d2 = SubClass2()

        self.a = [1, 2, 3]
        self.b = 'Alex ist ein toller Hecht'
        self.c = 1

    def print_all(self):
        print(self.__dict__)

    save_all = save_all
    load_all = load_all


if __name__=="__main__":
    filename = 'data/pickle'

    tc = TestClass()
    tc.print_all()
    tc.save_all(filename)
    tc.__dict__ = {}
    tc.print_all()
    tc.load_all(filename)
    tc.print_all()
