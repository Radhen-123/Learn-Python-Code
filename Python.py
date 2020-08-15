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
