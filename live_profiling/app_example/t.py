


# import psutil
# proc_iter = psutil.process_iter(attrs=["pid", "name", "cmdline"])
# # print(list(proc_iter))
# other_script_running = any("loop.py" in p.info["cmdline"] for p in list(proc_iter))

# for p in psutil.process_iter(attrs=["pid", "name", "cmdline"]):
#      print(p)


# def find_procs_by_name(name):
#     "Return a list of processes matching 'name'."
#     is_running = False
#     for p in psutil.process_iter(attrs=["name", "exe", "cmdline"]):
#          if p.info["cmdline"] == ["python","loop.py"]:
#              is_running = True

#     return is_running


# # print(find_procs_by_name("Music"))

# import os
# import psutil
# import sched, time
# import threading
# s = sched.scheduler(time.time, time.sleep)
# count = 0

# def do_something(sc): 
#     global count
#     print("Doing stuff...")
#     # do your stuff
#     count += 1
#     print(find_procs_by_name("Music"))
#     sc.enter(2, 1, do_something, (sc,))
    

# e1 = s.enter(2, 0, do_something, (s,))
# # s.run()



# def find_procs_by_name(name):
#     "Return a list of processes matching 'name'."
#     for p in psutil.process_iter(attrs=["name", "exe", "cmdline"]):
#          print(p.info)

# #     return ls
# print(find_procs_by_name("Music"))

# import schedule
# from schedule import every, repeat, run_pending
# import time

# count = 0

# @repeat(every(3).seconds,count)
# def job(count):
#      global count += 1
#      print("I am a scheduled job")

# while True:
#     run_pending()
#     print(count)
#     time.sleep(1)



import schedule
import time


count = 0

d = []
def greet(d):
    d.append(1)
    print('Hello', d)

job = schedule.every(2).seconds.do(greet, d)
# schedule.every(4).seconds.do(greet, name='Bob')

while True:
    schedule.run_pending()
    count += 1
    print(count)
    if count == 10:
         schedule.cancel_job(job)
         break
    time.sleep(1)
    

# from schedule import every, repeat

# @repeat(every().second, "World")
# @repeat(every().day, "Mars")
# def hello(planet):
#     print("Hello", planet)

