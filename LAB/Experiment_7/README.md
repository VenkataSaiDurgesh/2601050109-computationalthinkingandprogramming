Producer–Consumer Using Threading, Multiprocessing and Primitives
1. Algorithm / Procedure
Create a shared queue.
Create a lock to safely print messages.
Create a producer process and a consumer process.
Inside each process, create one thread.
Producer adds numbers to the queue.
Consumer removes numbers from the queue.
Use the lock while printing.
Stop after all items are processed.
2. Simple Python Program
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
3. Data & Result
Data:

Items = 1, 2, 3, 4, 5
Result:

Produced: 1
Produced: 2
Consumed: 1
Produced: 3
Consumed: 2
Produced: 4
Consumed: 3
Produced: 5
Consumed: 4
Consumed: 5
Completed
The order can change because both processes run concurrently.

4. Inference
The program shows how threading, multiprocessing, and primitives can work together.

Process → creates separate processes.
Thread → creates threads.
Queue → transfers data.
Lock → prevents simultaneous printing.
5. Analysis
Time Complexity: O(n)
Space Complexity: O(n)
Conclusion: The producer creates items and puts them into the queue, while the consumer takes the items from the queue concurrently.
