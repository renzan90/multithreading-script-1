import time
import threading

start=time.perf_counter()

def do_something():                                     #The main function that works in the code
    print('Sleeping 5 seconds')
    time.sleep(5)
    print('Done Sleeping')

t1=threading.Thread(target=do_something)                #Function subjected to threading twice
t2=threading.Thread(target=do_something)

t1.start()                                              #Functions executed
t2.start()

finish=time.perf_counter()                              

print(f'Finished in {finish-start} second(s)')

#Output

# Sleeping 1 second
# Sleeping 1 second
# Finished in (round0.00044659700006377534) second(s)
# Done Sleeping
# Done Sleeping

#In the above output the threading process begins with t1 printing the initial message 'sleeping 1 second' and does the same with t2.
#Then both t1 and t2 go to sleep and while they are sleeping, the 'finish' variable executes and prints the result.
#And after this has been done, the sleep time is over and then both t1 and t2 will print the 'done sleeping' messages