# def Even_int(n):
#     for i in range(n):
#         if i % 2 == 0:
#             yield i
#
#
# def Fibonacci(n):
#     tail, lead = 0, 1
#     for i in range(n):
#         yield tail
#         tail, lead = lead, lead + tail


# --------------------------     For Zip And Enumerate  --------------------------#

dayEng = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
dayGujarati = ["Somvar", "Mungarvar", "Buddth", "guruvar", "sukravar", "sunneyvar", "ravevar"]

for index, day in enumerate(zip(dayGujarati, dayEng), start=1):
    print(index, day[0] + " = " + day[1] + " in English")


# --------------------------     For Filter And Map  --------------------------#
def OddFunc(x):
    if x % 2 == 0:
        return False
    return True


def LowerFunc(x):
    if x.isupper():
        return False
    return True


def SquareFunction(x):
    return pow(x, 2)


def GradFunction(x):
    if x >= 90:
        return "A"
    elif 80 <= x < 90:
        return "B"
    elif 70 <= x < 80:
        return "C"
    elif 60 <= x < 70:
        return "D"
    else:
        return "F"

List = [95, 88, 47, 75, 65, 79, 35, 49, 65, 98, 58]
char = "ABcdEFghijKLMNopQRSTuvw"
odd = list(filter(OddFunc, List))
print(odd)
lower = list(filter(LowerFunc, char))
print(lower)
square = list(map(SquareFunction, List))
print(square)
Grad = list(map(GradFunction, sorted(List)))
print(Grad)

# --------------------------     For iteration Tools  -------------------------- #
import itertools

List = ["Radhen", "Khant", "Om", "Doramon", "Tom", "Jerry"]
cycle = itertools.cycle(List)
for i in range(8):
    print(next(cycle))

count = itertools.count(100, 3)
for i in range(10):
    print(next(count))

accum = itertools.accumulate(List)
print(list(accum))
accumf = itertools.accumulate(List, max)
print(list(accumf))

x = "ABCD"
y = "1234"

chain = itertools.chain(x, y)
print(list(chain))

def Function(x):
    return x < 30

List = [10, 20, 50, 90, 30, 56]
Ans = itertools.dropwhile(Function, List)
print(list(Ans))
Ans2 = itertools.takewhile(Function, List)
print(list(Ans2))

# --------------------------     Multiple Parameter   -------------------------- #

def Addition(*args):
    result = 0
    for arg in args:
        result += arg
    print(result)
Addition(10, 20, 30, 56)
MyNum = [10, 20, 30, 56]
Addition(*MyNum)

List = [12, 56, 7, 5, 21]
SquareRoot = map(lambda num: pow(num, 1/2), List)

# --------------------------     Collection   -------------------------- #

import collections
Point = collections.namedtuple("Point", "X, Y")
P1 = Point(20, 30)
P2 = Point(50, 60)
print(P1, P2)
P1 = P1._replace(X=50)
print(P1)

p1 = (20, 30)
p2 = (50, 60)
print(type(p1), p2)

Fruits = ["Pineapple", "Orange", "Banana", "Pineapple", "Apple", "Banana", "Pineapple"]
CounterDict = {}
for Fruit in Fruits:
    if Fruit in CounterDict.keys():
        CounterDict[Fruit] += 1
    else:
        CounterDict[Fruit] = 1

print(CounterDict)

DefaultDict = collections.defaultdict(int)
for Fruit in Fruits:
    DefaultDict[Fruit] += 1

for key, values in CounterDict.items():
    print(key, values)

Class1 = ["Radhen", "Khant", "Chiman", "Varsa", "Varsa", "Makadiya", "College", "Nitesh", "Khant", "Om", "College"]
Class2 = ["Om", "Khant", "Chiman", "Varsa", "Yogi", "Shailesh", "School", "Khant", "Vageda", "Radhen", "College"]
c1 = collections.Counter(Class1)
c2 = collections.Counter(Class2)
print(c1)
print(c2)
print(sum(c1.values()))
c1.update(Class2)
print(sum(c1.values()))
print(c1.most_common(5))
print(c1 & c2)

sportTeams = [("Royals", (18, 12)), ("Rockets", (24, 6)), ("Cardinals", (20, 10)), ("Dragons", (22, 8)), ("Kings", (15, 15)), ("Chargers", (20, 10)), ("Jets", (16, 14)), ("Warriors", (25, 5))]
sortedTeams = sorted(sportTeams, key = lambda t: t[1][0], reverse=True)
print(sportTeams)
print(sortedTeams)
team = collections.OrderedDict(sportTeams)
print(team)
trying = sortedTeams.pop()
print(trying)
Dictionary = collections.OrderedDict({"a" : 1, "b" : 2, "c" : 3})
Dictionary2 = collections.OrderedDict({"a" : 1, "c" : 3, "b" : 2})
print(Dictionary == Dictionary2)  # Will return True in simple Dictionary

Alpha = collections.deque("abcdefghijklmnopqrstuvwxyz")
print(Alpha)
Alpha.pop()
Alpha.popleft()
Alpha.append("Radhen")
Alpha.appendleft("Khant")
print(Alpha)
Alpha.rotate(10)
print(Alpha)
Alpha.rotate(-5)
print(Alpha)

# --------------------------     Advanced Classes   -------------------------- #

from enum import Enum, unique, auto


class Fruit(Enum):
    Apple = 1
    Banana = 2
    Orange = 3
    Tomato = 4
    Pear = auto()
print(Fruit.Apple)
print(type(Fruit.Apple))
print(repr(Fruit.Apple))
print(Fruit.Apple.name, Fruit.Apple.value)  #Key must Unique
print(Fruit.Pear.name, Fruit.Pear.value)
myFruit = {}
myFruit[Fruit.Banana] = "Core"
print(myFruit)

class Person():
    def __init__(self):
        self.fname = "Radhen"
        self.lname = "Khant"
        self.age = 20
    def __repr__(self):
        return "<Person Class - fname:{0}, lname:{1}, age:{2} >".format(self.fname, self.lname, self.age)
    def __str__(self):
        return "Person {0} {1} is {2} years old ".format(self.fname, self.lname, self.age)
    def __format__(self, format_spec):
        return "Person ({0} {1} is {2})".format(self.fname, self.lname, self.age)
    def __bytes__(self):
        val = "Person:{0}:{1}:{2}".format(self.fname, self.lname, self.age)
        return bytes(val.encode("utf-8"))
cls1 = Person()
print(repr(cls1))
print(str(cls1))
print("Formatted: {0}".format(cls1))
print(bytes(cls1))


class MyColour():
    def __init__(self):
        self.Red = 50
        self.Green = 75
        self.Blue = 100
    def __getattr__(self, item):
        if item == "RGBcolor":
            return (self.Red, self.Green, self.Blue)
        elif item == "Hexcolor":
            return ("#{0:02x}{1:02x}{2:02x}".format(self.Red, self.Green, self.Blue))
        else:
            raise AttributeError
    def __setattr__(self, attr, value):
        if attr == "RGBcolor":
            self.Red = value[0]
            self.Green = value[1]
            self.Blue = value[2]
        else:
            super().__setattr__(attr, value)
    def __dir__(self):
        return ("Red", "Green", "Blue", "RGBcolor", "Hexcolor")


Class = MyColour()
print(Class.RGBcolor)
print(Class.Hexcolor)
Class.RGBcolor = (125, 200, 86)
print(Class.RGBcolor)
print(Class.Hexcolor)
print(dir(Class))


class Point():
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def __repr__(self):
        return "Point({0}, {1})".format(self.X, self.Y)

    def __add__(self, other):
        return Point(self.X + other.X, self.Y + other.Y)

    def __sub__(self, other):
        return Point(self.X - other.X, self.Y - other.Y)

    def __iadd__(self, other):
        self.X += other.X
        self.Y += other.Y
        return Point(self.X, self.Y)

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

#  We can also use grater than less then || equal to  and then sorted function will become enable


P1 = Point(20, 30)
P2 = Point(10, 20)
print(P1)
print(P2)
print(P1 - P2)
print(P1 + P2)
P1 += P2
print(P1)


# --------------------------     Logging   -------------------------- #
import logging
fmtstr = "%(asctime)s: %(levelnumber)s: %(funcName)s Line:%(;ineno)d %(message)s"
logging.basicConfig(level=logging.INFO, filename='output.log', filemode='w')

logging.warning("This is Warning Message")
logging.info("This is Information Message")
logging.debug("This is Debug Message")
logging.error("This is Error Message")
logging.critical("This is Critical Message")


# --------------------------     Comprehension   -------------------------- #

odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
even = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# evenSquare = list(map(lambda e: pow(e, 2), list(filter(lambda e: 4 < e < 16, even))))
# print(evenSquare)
evenSquare = [e**2 for e in even]
print(evenSquare)
oddSquare = [e ** 2 for e in odd if 3 < e < 16]
print(oddSquare)

cTemp = [0, 12, 34, 100]
fDict = {t: (t*9/5) + 32 for t in cTemp if t < 100}
print(fDict)
Strin = "The quick brown fox jump over the lazy dog"
charsSet = {c.upper() for c in Strin if not c.isspace()}
