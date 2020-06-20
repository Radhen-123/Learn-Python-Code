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

def Calender_Module():
    import calendar
    #           Plain Calender
    Text_Calender = calendar.TextCalendar(calendar.SUNDAY)
    Text_String = Text_Calender.formatmonth(2020, 6, 0, 0)
    print(Text_String)

    #           HTML Code
    HTML_Calender = calendar.HTMLCalendar(calendar.SUNDAY)
    HTML_String = HTML_Calender.formatmonth(2020,6)
    print(HTML_String)
    print("\n\nIteration\n\n")
    for i in Text_Calender.itermonthdays(2020,6):
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

def GratestCommonDivison(a,b):
    while(b != 0):  # Make Table
        t = a       # a > b and b!= 0    20,8
        a = b       # r = a%b            4
        b = t % b   # a = b, b = r loop again a = 8 , b = 4
    return a        # Return a until b!= 0


class LinkedListNode:
    def __init__(self, value, nextNode = None): #Single Linked List
        self.value = value
        self.nextNode = nextNode
# node1 = LinkedListNode(3)
# node2 = LinkedListNode(7)
# node3 = LinkedListNode(10)
#
# node1.nextNode = node2
# node2.nextNode = node3
#
# cur  = node1
# while True:
#     print(str(cur.value)+" ->" + str(cur.nextNode))
#     if cur.nextNode is None:
#         print("None")
#         break
#     cur = cur.nextNode
#
#
# print(node1.nextNode)
# print(node2.nextNode)
# print(node3.nextNode)
class LinkedList:
    def __init__(self, Head = None):
        self.Head = Head

    def InsertAtTail(self, Data):
        NewNode = LinkedListNode(Data)
        if (self.Head == None):
            self.Head = NewNode
        else:
            LastNode = self.Head
            while LastNode.nextNode != None:
                LastNode = LastNode.nextNode
            LastNode.nextNode = NewNode

    def InsertAtHead(self, Data):
        NewNode = LinkedListNode(Data)
        NewNode.nextNode = self.Head
        self.Head = NewNode

    def Print_Data(self):
        Start_Node = self.Head
        while(Start_Node != None):
            print(Start_Node.value)
            Start_Node = Start_Node.nextNode

    def Length_Linked_List(self):
        StartNode = self.Head
        Length = 0
        while(StartNode != None):
            Length += 1
            StartNode = StartNode.nextNode
        return Length
     def DeleteAtHead(self):
        DeleteNode = self.Head
        self.Head = DeleteNode.nextNode
        del DeleteNode
        
        
ll = LinkedList()
ll.InsertAtTail(25)
ll.InsertAtTail(663)
ll.InsertAtTail(536)
ll.InsertAtTail(23)


ll.InsertAtHead(65)
ll.InsertAtHead(653)
ll.InsertAtHead(31)

ll.Print_Data()
print("Length "+str(ll.Length_Linked_List()))
