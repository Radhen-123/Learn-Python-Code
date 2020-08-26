import threading
import time

# WorkingC = True
# def Working_Time():
#     name = threading.current_thread().getName()
#     Working = 0
#     while WorkingC:
#         print(name + "Is Working")
#         Working += 1
#     print(name, "has Worked ", Working, " Time")
#
#
# if __name__ == '__main__':
#     threading.Thread(target=Working_Time, name="Radhen").start()
#     threading.Thread(target=Working_Time, name="Om").start()
#     time.sleep(0.2)
#     WorkingC = False



# class Om_Task(threading.Thread):
#     def __init__(self):
#         super().__init__()
#     def run(self):
#         time.sleep(1)
#         print("Om Start Working")
#         print("Om Waiting  to overcom Barrier")
#         time.sleep(5)
#         print("Om is Working")
#         time.sleep(2)
# print("Command to om")
# Om = Om_Task()
# Om.start()
# print("Radhen Continue his Work")
# time.sleep(3)
# print("Radhen Done")
# print("Waiting")
# Om.join()
# print("Work completed")

# Work = True
# def Om_Watching():
#     while Work:
#         print("Om is Watching")
#         time.sleep(1)
# Om = threading.Thread(target=Om_Watching)
# Om.daemon = True
# Om.start()
# for i in range(0, 5, 1):
#     print("Radhen is working")
#     time.sleep(2)


# ---------- Data Race ---------- One pencile to solve Overwitting
# Hours = 0
# Pencil = threading.Lock()               #Use RLock for multipal time acquire and release same number of time or dead lock
# def WorkingHour():
#     for i in range(0, 10, 1):
#         print(threading.current_thread().getName()+" is thinking")
#         global Hours
#         Pencil.acquire()                 #Comment This line
#         Hours += 1
#         time.sleep(0.5)
#         Pencil.release()                 #Comment This line
#
# Om = threading.Thread(target=WorkingHour, name="Om")
# Radhen = threading.Thread(target=WorkingHour, name="Radhen")
# Om.start()
# Radhen.start()
# Om.join()
# Radhen.join()
# print(Hours)


# ---------- Try Lock ---------- Try to acquire if unlock otherwise do remaining work
# items_on_notepad = 0
# Pencil = threading.Lock()
# def Worker():
#     global items_on_notepad
#     name = threading.current_thread().getName()
#     items_to_add = 0
#     while items_on_notepad < 20:
#         if items_to_add and Pencil.acquire(blocking=False):
#             # Pencil.acquire()                                  #uncomment This and remove second condition with blocking
#             items_on_notepad += items_to_add
#             print(name+' added '+str(items_to_add)+" item")
#             items_to_add = 0
#             time.sleep(0.3)
#             Pencil.release()
#         else:
#             time.sleep(0.1)
#             items_to_add += 1
#             print(name +" found something else to add")
# Om = threading.Thread(target=Worker, name="Om")
# Radhen = threading.Thread(target=Worker, name="Radhen")
# Start  = time.perf_counter()
# Om.start()
# Radhen.start()
# Om.join()
# Radhen.join()
# Start = time.perf_counter() - Start
# print(Start)

# ---------- Read Write Lock ----------


# ---------- Dead Lock Overcome ---------- Example Think and eat two chopstick shared by two people used in bank i.e Prority

# a_stick = threading.Lock()
# b_stick = threading.Lock()
# c_stick = threading.Lock()
# sushi = 10*50
# def Pholosopher(name, first_stick, second_stick):
#     global sushi
#     Eaten = 0
#     while sushi > 0:
#         first_stick.acquire()
#         second_stick.acquire()
#         try:
#             if sushi > 0:
#                 sushi -= 1
#                 Eaten += 1
#                 print(name, " has taken sushi and remaining ", sushi)
#             # if sushi == 10:                               # ---------- Abondund Lock ---------- Acqures and started another work so add in try
#             #     print(sushi/0)
#         finally:
#             first_stick.release()
#             second_stick.release()
#     print(name," took ", Eaten," Sushi")                    #Om will have higest number of sushi because he has b_stick so less compition
# #
# # # # threading.Thread(target=Pholosopher, args=("Radhen", a_stick, b_stick)).start()       #Dead lock migh toccure
# # # # threading.Thread(target=Pholosopher, args=("Om", b_stick, c_stick)).start()
# # # # threading.Thread(target=Pholosopher, args=("Radhen", c_stick, a_stick)).start()
# # # threading.Thread(target=Pholosopher, args=("Radhen", a_stick, b_stick)).start()         #Dead lock will not occure due to priority a to higest
# # # threading.Thread(target=Pholosopher, args=("Om", b_stick, c_stick)).start()
# # # threading.Thread(target=Pholosopher, args=("Khant", a_stick, c_stick)).start()
# # threading.Thread(target=Pholosopher, args=("Radhen", a_stick, b_stick)).start()         #Dead lock will not occure due to priority a to higest
# # threading.Thread(target=Pholosopher, args=("Om", a_stick, b_stick)).start()
# # threading.Thread(target=Pholosopher, args=("Khant", a_stick, b_stick)).start()
#
# for i in range(0,50):
#     threading.Thread(target=Pholosopher, args=(str(i), a_stick, b_stick)).start()  # Dead lock will not occure due to priority a to higest
# ----------- Live Lock -----------
