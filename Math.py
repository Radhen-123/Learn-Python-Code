def Time_Module():
    import datetime

    #       All Functions for Today
    Today = datetime.datetime.today()
    print("Todays Date And Time: ", Today)
    Date = Today.date()
    Time = Today.time()
    Month = Today.month
    Year = Today.year
    Day = Today.day
    Time_Parts = Today.time()
    WeekdayList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    Weekday = Today.weekday()
    print("Date: ", Date)
    print("Time: ", Time)
    print("Year: ", Year)
    print("Month: ", Month)
    print("Day: ", Day)
    print("Weekday: ", WeekdayList[Weekday])
    print("Time Hour:", Time_Parts.hour, " Minute: ", Time_Parts.minute, " Seconds: ", Time_Parts.second,
          " Microsecond: ", Time_Parts.microsecond)
    # Another Way
    Another_Now = datetime.datetime.now()
    print("By Different way: ", Another_Now)
    Time_Another = datetime.datetime.time(datetime.datetime.now())
    print("Time by another way: ", Time_Another)
    #       Today Functoin Gets Over

    #           Formatting DateTime

    print("Formate with % operation: ", Today.strftime("%a WeekDays %A, %d Date %D, %b Months %B, %y Year %Y"))
    #           Formate for specific Location
    print(Today.strftime("Local Date and Time: %c"))
    print(Today.strftime("Local Date: %x "))
    print(Today.strftime("Local time: %X "))
    #           Formate Time
    print(Today.strftime("Current time 12 Hour formate: %I:%M:%S %p"))
    print(Today.strftime("24 Hour Formate time: %H:%M"))

    #           Perform Math
    print(datetime.timedelta(days=365, hours=5,minutes=60))
    AfterYear = Today + datetime.timedelta(days=365)
    print(AfterYear.strftime("One Year From Now: %A,%d,%B,%Y"))
    Calculate = Today + datetime.timedelta(days=2, weeks=3, hours=4, minutes=35, seconds=55, milliseconds= 55)
    print(Calculate.strftime("Future Calculation: %A,%d,%B,%Y"))

    #               Past Calculation
    LastYear = Today - datetime.timedelta(days=365)
    print(LastYear.strftime("Last Year From Now was: %A,%d,%B,%Y"))
    CalculatePast = Today - datetime.timedelta(days=2, weeks=3, hours=4, minutes=35, seconds=55, milliseconds=55)
    print(CalculatePast.strftime("Past Calculation :%A,%d,%B,%Y"))
    #       Assign Date
    DateOfBirth = datetime.date(day=6, month=12, year=2020)
    print(DateOfBirth.strftime("%A,%d,%B,%Y"))

def Calendar_Module():
    import calendar
    #           Plain Calender
    Text_Calendar = calendar.TextCalendar(calendar.SUNDAY)
    Text_String = Text_Calendar.formatmonth(2020, 6, 0, 0)
    print(Text_String)

    #           HTML Code
    HTML_Calendar = calendar.HTMLCalendar(calendar.SUNDAY)
    HTML_String = HTML_Calendar.formatmonth(2020,6)
    print(HTML_String)
    print("\n\nIteration\n\n")
    for i in Text_Calendar.itermonthdays(2020,6):
        print(i)
    print("List in calendar library")
    print(calendar.day_name[:])
    print(calendar.month_name[:])
    cal = calendar.monthcalendar(2020,7)
    print(cal[:])
    print(cal[0][3])
    print(calendar.MONDAY)
    print("Team Meeting")
    for m in range(1,13):
        calen = calendar.monthcalendar(2020, m)
        weekone = calen[0]
        weektwo = calen[1]
        if weekone[calendar.SUNDAY] != 0:
            meetday = weekone[calendar.SUNDAY]
        else:
            meetday = weektwo[calendar.SUNDAY]
        print("%10s %2d"%(calendar.month_name[m],meetday))

def GreatestCommonDivison(a,b):
    while(b != 0):  # Make Table
        t = a       # a > b and b!= 0    20,8
        a = b       # r = a%b            4
        b = t % b   # a = b, b = r loop again a = 8 , b = 4
    return a        # Return a until b!= 0



def MergeShort(List):
    if len(List) > 1:
        Middle = len(List)//2
        Left = List[:Middle]
        Right = List[Middle:]
        MergeShort(Left)
        MergeShort(Right)
        RightIndex = 0
        LeftIndex = 0
        FinalListIndex = 0
        while RightIndex < len(Right) and LeftIndex < len(Left):
            if Left[LeftIndex] > Right[RightIndex]:
                List[FinalListIndex] = Right[RightIndex]
                RightIndex +=1
            else:
                List[FinalListIndex] = Left[LeftIndex]
                LeftIndex += 1
            FinalListIndex += 1

        while RightIndex < len(Right):
            List[FinalListIndex] = Right[RightIndex]
            RightIndex += 1
            FinalListIndex += 1

        while LeftIndex < len(Left):
            List[FinalListIndex] = Left[LeftIndex]
            LeftIndex += 1
            FinalListIndex += 1
# l = [1,6,8,4,1,5,8,9,6,2,5,45]
# MergeShort(l)


class LinkedListNode:
    def __init__(self, Data, NextNode = None):
        self.Data = Data
        self.NextNode = NextNode

class LinkedList:
    def __init__(self, Start = None):
        self.Start = Start


    def Insert_At_Start(self, Data):
        NewNode = LinkedListNode(Data)
        NewNode.NextNode = self.Start
        self.Start = NewNode


    def Insert_At_End(self, Data):
        NewNode = LinkedListNode(Data)
        Pointer = self.Start
        if  Pointer == None:
            self.Insert_At_Start(Data)
        else:
            while Pointer.NextNode != None:
                Pointer = Pointer.NextNode
            Pointer.NextNode = NewNode

    def Insert_At_Index(self, Index, Data):
        NewNode = LinkedListNode(Data)
        FindPointer = 1
        if(Index <= 0):
            print("Insertion at Invalid Index")
        elif(Index == 1):
            self.Insert_At_Start(Data)
        elif (Index <= self.Length()):
            Pointer = self.Start
            while FindPointer != Index:
                PrePointer = Pointer
                Pointer = Pointer.NextNode
                FindPointer += 1
            PrePointer.NextNode = NewNode
            NewNode.NextNode = Pointer
        elif (Index == self.Length() + 1):
            self.Insert_At_End(Data)
        else:
            print("Insertion Out of Range")

    def Insert_Before_Number(self, Number, Data):
        Pointer = self.Start
        NewNode = LinkedListNode(Data)
        Count = 0
        if Number ==   Pointer.Data:
            self.Insert_At_Start(Data)
        else:
            while Pointer.Data != Number and Pointer.NextNode != None:
                PrePointer = Pointer
                Pointer = Pointer.NextNode
                Count += 1
            PrePointer.NextNode = NewNode
            NewNode.NextNode = Pointer


    def Insert_After_Number(self, Number, Data):
        Pointer = self.Start
        PastPointer = Pointer.NextNode
        NewNode = LinkedListNode(Data)
        while Pointer.Data != Number and Pointer.NextNode != None:
            Pointer = Pointer.NextNode
            PastPointer =PastPointer.NextNode
        Pointer.NextNode = NewNode
        NewNode.NextNode = PastPointer

    def Delete_At_Start(self):
        Pointer = self.Start
        if Pointer == None:
            print("List is Empty")
            return None
        else:
            self.Start = Pointer.NextNode
            del Pointer


    def Delete_At_End(self):
        Pointer = self.Start
        if Pointer == None:
            print("List is Empty")
            return None
        else:
            while Pointer.NextNode != None:
                PrePointer = Pointer
                Pointer = Pointer.NextNode
            PrePointer.NextNode = None
            del Pointer

    def Delete_At_Index(self, Index):
        FindIndex = 1
        Pointer = self.Start
        if Pointer == None:
            print("List is Empty")
            return None
        elif Index <= 0:
            print("Deletion Invalid Index")
        elif (Index == 1):
            self.Delete_At_Start()
        elif(Index == self.Length()):
            self.Delete_At_End()
        elif Index <= self.Length() :
            while FindIndex != Index:
                PrePointer = Pointer
                Pointer = Pointer.NextNode
                FindIndex += 1
            PrePointer.NextNode = Pointer.NextNode
            del Pointer
        else:
            print("Deletion Out of Range")

    def Delete_Number(self, Number):
        Pointer = self.Start
        if Pointer == None:
            print("List is Empty")
        else:
            while Pointer.Data != Number:
                PrePointer = Pointer
                Pointer = Pointer.NextNode
            PrePointer.NextNode = Pointer.NextNode
            del Pointer

    def Print_Linked_List(self):
        Begin = self.Start
        Count = 0
        if Begin == None:
            print("No Data To print")
        else:
            while Begin != None:
                Count += 1
                print("Index:" + str(Count) + " Data: " + str(Begin.Data))
                Begin = Begin.NextNode

    def Length(self):
        Count = 0
        StartPointer = self.Start
        while StartPointer != None:
            StartPointer = StartPointer.NextNode
            Count += 1
        return Count

def Function_Of_Linked_List():
    print("*********Index Menu**********")
    print("---------Insertion-----------")
    print("1 For insert Data at Start")
    print("2 For insert Data at End")
    print("3 For insert Data at Index")
    print("4 For insert Data Before Number")
    print("5 For insert Data after Number")
    print("---------Deletion-----------")
    print("6 For Delete Element at Start")
    print("7 For Delete Element at End")
    print("8 For Delete Element at Index")
    print("9 For Delete given Number")
    print("--------Other---------------")
    print("10 Print Length of list")
    print("11 for exit")
    Linked_List = LinkedList()
    Start = 0
    while Start != 11:
        Number = int(input("Enter your Selection: "))
        if Number == 1:
            Data = int(input("Enter Data to insert: "))
            Linked_List.Insert_At_Start(Data)
            Linked_List.Print_Linked_List()
        elif Number == 2:
            Data = int(input("Enter Data to insert: "))
            Linked_List.Insert_At_End(Data)
            Linked_List.Print_Linked_List()
        elif Number == 3:
            Data = int(input("Enter Data to insert: "))
            Index = int(input("Enter Index: "))
            Linked_List.Insert_At_Index(Index, Data)
            Linked_List.Print_Linked_List()
        elif Number == 4:
            Data = int(input("Enter Data to insert: "))
            BeforeNumber = int(input("Before which Number: "))
            Linked_List.Insert_Before_Number(BeforeNumber, Data)
            Linked_List.Print_Linked_List()
        elif Number == 5:
            Data = int(input("Enter Data to insert: "))
            AfterNumber = int(input("After which Number: "))
            Linked_List.Insert_After_Number(AfterNumber, Data)
            Linked_List.Print_Linked_List()
        elif Number == 6:
            Linked_List.Delete_At_Start()
            Linked_List.Print_Linked_List()
        elif Number == 7:
            Linked_List.Delete_At_End()
            Linked_List.Print_Linked_List()
        elif Number == 8:
            Index = int(input("Enter Index: "))
            Linked_List.Delete_At_Index(Index)
            Linked_List.Print_Linked_List()
        elif Number == 9:
            Number = int(input("Enter Number To Delete: "))
            Linked_List.Delete_Number(Number)
            Linked_List.Print_Linked_List()
        elif Number == 10:
            print(Linked_List.Length())
        Start = Number
# Function_Of_Linked_List()

def Generat_Unordard_List(From, To, Length):
    import random
    List = random.sample(range(From, To),Length)
    return List



def Find_Max_Sum_in_sequence(List):
    Sum_Till_Now = 0
    Max_Till_Now = 0
    for i in range(0, len(List),1):
        Sum_Till_Now = Sum_Till_Now + List[i]
        if Sum_Till_Now < 0:
            Sum_Till_Now = 0
        if Sum_Till_Now > Max_Till_Now:
            Max_Till_Now = Sum_Till_Now
    return Max_Till_Now


# List = [[0,0,1,0,1],
#         [0,0,1,0,0],
#         [1,1,1,0,0],
#         [1,1,1,1,0],
#         [0,0,0,1,0],
#         [0,0,1,1,1]]
# print(List[2][0])
# print(len(List[0]))
# print(len(List))
# Num = 0
def Colour(Matrix, Row, Column, Replace, WhichNumber):
    global Num
    if (Row < 0 or Column < 0 or Row > len(Matrix)-1 or Column > len(Matrix[0])-1):
        return
    if (Matrix[Row][Column] != WhichNumber):
        return
    Matrix[Row][Column] = Replace
    Num += 1
    Colour(Matrix, Row-1, Column, Replace, WhichNumber)
    Colour(Matrix, Row+1, Column, Replace, WhichNumber)
    Colour(Matrix, Row, Column-1, Replace, WhichNumber)
    Colour(Matrix, Row, Column+1, Replace, WhichNumber)

# Colour(List, 2, 0, 3, 1)
# print(List[0][:])
# print(List[1][:])
# print(List[2][:])
# print(List[3][:])
# print(List[4][:])
# print(List[5][:])
# print("Length = "+str(Num))

x = 0
def FastPower(Base, Power):                    #a^b
    global x
    x += 1
    if (Power == 0 or Base == 1):
        return 1
    elif Power < 0:
        if (Power % 2 == 0):
            return FastPower(1 / (Base * Base), Power / 2)
        else:
            return FastPower(Base, Power + 1) / Base
    elif (Power%2 == 0):
        return FastPower(Base*Base, Power/2)
    else:
        return Base*FastPower(Base, Power-1)
# print(FastPower(4, -4))

def Find_All_Possible_Path(Rows, Columns):          #Find all possible number of path in m x n Matrix
    if(Rows == 1 or Columns == 1):                  #base condition
        return 1
    else:
        return Find_All_Possible_Path(Rows-1, Columns) + Find_All_Possible_Path(Rows, Columns-1)

# print(Find_All_Possible_Path(4, 4))


def Game_Of_Coin(Array, First, Last):
    if (First + 1 == Last):
        return max(Array[First], Array[Last])
    return max(Array[First] + min(Game_Of_Coin(Array, First+2, Last), Game_Of_Coin(Array,First+1, Last-1)), Array[Last] + min(Game_Of_Coin(Array, First+1, Last-1), Game_Of_Coin(Array, First, Last-2)))

# a =[1, 5, 700, 2]
# print(Game_Of_Coin(a, 0, len(a)-1))

def Sum(Number):
    if (Number == 1):
        return 1
    return Number + Sum(Number-1)



def Factorial(Number):
    global Sum
    if Number <= 1:
        return 1
    else:
        Number = Number * Factorial(Number - 1)
    return Number
# print(Factorial(6))

def Fibonacci_Sequence(AtLocation):
    if AtLocation<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif AtLocation==0:
        return 0
    # Second Fibonacci number is 1
    elif AtLocation==1:
        return 1
    else:
        return Fibonacci_Sequence(AtLocation-1)+Fibonacci_Sequence(AtLocation-2)


def Fibonacci(NumberOfTerms):
    n = 0
    List = [0, 1]
    while NumberOfTerms-2 != 0:
        List.append(List[n]+List[n+1])
        n += 1
        NumberOfTerms -= 1
    print(List)
# Fibonacci(8)
# print(Fibonacci_Sequence(7))
Ten = 1
def Sum_of_First_Nterms(NumberOfTerm):
    if NumberOfTerm <= 1:
        return 1
    elif NumberOfTerm == 2:
        return 3
    elif NumberOfTerm%2 == 0:
        return (3*Sum_of_First_Nterms((NumberOfTerm - 1) / 2) + Sum_of_First_Nterms((NumberOfTerm + 1) / 2))
    else:
        return (3*Sum_of_First_Nterms(NumberOfTerm / 2) + Sum_of_First_Nterms(NumberOfTerm / 2 -1))
# print(Sum_of_First_Nterms(3))

Step = 1
def Tower_Of_Hnoi(NumberOfPices, From_Source, Destination_Rode, Extra_Rode):
    global Step
    if NumberOfPices == 1:
        print("Step:",Step," Move disk 1 from", From_Source, " Rode to", Destination_Rode, " Rode")
        Step +=1
    else:
        Tower_Of_Hnoi(NumberOfPices - 1, From_Source, Extra_Rode, Destination_Rode)
        print("Step:",Step," Move disk", NumberOfPices,  "from", From_Source, " Rode to", Destination_Rode, " Rode")
        Step += 1
        Tower_Of_Hnoi(NumberOfPices-1, Extra_Rode, Destination_Rode, From_Source)
# Tower_Of_Hnoi(3, "A", "C", "B")
# print("-------------------------------------------------------")
def Tower_Hnoi(NumberOfPeg, Source, Destination, Spare):
    if NumberOfPeg == 1:
        print("Move From ",Source," To ",Destination )
    else:
        Tower_Hnoi(NumberOfPeg-1, Source, Spare, Destination)
        Tower_Hnoi(1, Source, Destination, Spare)
        Tower_Hnoi(NumberOfPeg-1, Spare, Destination,Source)
# Tower_Hnoi(3, 'A', 'C', 'B')


def Decimal_To_Any_Base(Decimal, Base):
    if Decimal < Base:
        return Decimal
    else:
        return  10 * (Decimal_To_Any_Base(Decimal // Base, Base)) + Decimal % Base

# print(Decimal_To_Any_Base(11, 8))

def Reverse_String(Name):
    if Name == "":
        return ""
    else:
        return Reverse_String(Name[1:]) + Name[0]
def Palindrome(Name):
    Name = Name.lower()
    Length = len(Name)
    if Length == 1:
        return True
    else:
        return (Name[0] == Name[Length - 1] and Palindrome(Name[1:Length - 1]))
# print(Palindrome("Radar"))


