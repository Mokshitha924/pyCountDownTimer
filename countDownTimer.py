import time
def test():
    val=0
    while val<10:
        val+=1
        time.sleep(1)
        print(val)
def countDown(t):
    while t:
        min=t//60
        secs=t%60
        output="your time left is {:02d}:{:02d}".format(min,secs)
        print(output)
        time.sleep(1)
        t-=1
    print("Time is up!!")
    start()
def start():
    t=input("Enter the number of seconds:")
    if t.isnumeric():
        countDown(int(t))
    else:
        print("Was not a number")
        start()
start()