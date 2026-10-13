from multiprocessing import Process, Queue, Lock
import threading

def producer(q, lock):
    def work():
        for i in range(1, 6):
            q.put(i)
            with lock:
                print("Produced:", i)

    t = threading.Thread(target=work)
    t.start()
    t.join()


def consumer(q, lock):
    def work():
        for i in range(1, 6):
            item = q.get()
            with lock:
                print("Consumed:", item)

    t = threading.Thread(target=work)
    t.start()
    t.join()


if __name__ == "__main__":

    q = Queue()
    lock = Lock()

    p1 = Process(target=producer, args=(q, lock))
    p2 = Process(target=consumer, args=(q, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Completed")
