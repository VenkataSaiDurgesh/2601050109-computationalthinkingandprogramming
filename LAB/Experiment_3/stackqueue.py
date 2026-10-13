from dataclasses import dataclass
from typing import Any


@dataclass
class Stack:
    items: list[Any]

    def push(self, x: Any):
        self.items.append(x)

    def pop(self):
        return self.items.pop()


@dataclass
class Queue:
    items: list[Any]

    def enqueue(self, x: Any):
        self.items.append(x)

    def dequeue(self):
        return self.items.pop(0)


# Stack
s = Stack([])
s.push(10)
s.push(20)
print("Stack:", s.items)
print("Pop:", s.pop())

# Queue
q = Queue([])
q.enqueue(10)
q.enqueue(20)
print("Queue:", q.items)
print("Dequeue:", q.dequeue())
