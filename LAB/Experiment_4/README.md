List-Based vs Generator-Based Processing
1. Algorithm / Procedure
Create a large dataset.
Process it using a list.
Process the same data using a generator.
Compare their execution time and memory usage.
Display the results.
2. Very Simple Python Code
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
3. Input
Dataset size: 1,000,000
4. Output
Example output:

List time: 0.08
List memory: 8448728

Generator time: 0.09
Generator memory: 200
The exact execution time may vary depending on the computer.

5. Inference
A list uses more memory because it stores all elements. A generator uses very little memory because it produces elements one at a time.

6. Analysis
Method	Memory	Execution
List	High	Usually faster
Generator	Very low	May be slightly slower
For large datasets, generators are more memory efficient because they process data one item at a time.
