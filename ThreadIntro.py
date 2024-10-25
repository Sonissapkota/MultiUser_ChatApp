import threading

#Threading allows us to speed up program by executing multiple task at the same time.
#Each task will run on its own thread
#Each thread can run simultaneously and share data with each other

def function1():
    for i in range(10):
        print("one")

def function2():
    for i in range(10):
        print("two")

def function3():
    for i in range(10):
        print("three")

# function1()
# function2()
# function3()

#We can execute these function concurrently using threads! We must have a target for a thread
t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)
t3 = threading.Thread(target=function3)

t1.start()
t2.start()
t3.start()