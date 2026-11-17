
import threading

balance = 1000

lock = threading.Lock()

def withdraw():
    global balance

    lock.acquire()

    if balance >= 500:
        balance -= 500
        print("Withdrawal successful")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance")

    lock.release()

t1 = threading.Thread(target=withdraw)
t2 = threading.Thread(target=withdraw)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final balance:", balance)
