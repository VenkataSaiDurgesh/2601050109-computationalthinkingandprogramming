import time
import sys

n = 1000000

# List processing
start = time.time()

data = [x * 2 for x in range(n)]

list_time = time.time() - start
list_memory = sys.getsizeof(data)


# Generator processing
start = time.time()

data = (x * 2 for x in range(n))

for x in data:
    pass

generator_time = time.time() - start
generator_memory = sys.getsizeof(data)


print("List time:", list_time)
print("List memory:", list_memory)

print("Generator time:", generator_time)
print("Generator memory:", generator_memory)
