import time
import tracemalloc


def create_dummy_log(filename, num_lines=50000):
    with open(filename, "w") as file:
        for i in range(num_lines):
            if i % 10 == 0:
                file.write(f"{i} - ERROR - Database connection lost\n")
            elif i % 5 == 0:
                file.write(f"{i} - WARNING - Slow response time\n")
            else:
                file.write(f"{i} - INFO - Request processed successfully\n")



def read_errors_list(filename):
    errors = []

    with open(filename, "r") as file:
        for line in file:
            if "ERROR" in line:
                errors.append(line.strip())

    return errors


def read_errors_generator(filename):
    with open(filename, "r") as file:
        for line in file:
            if "ERROR" in line:
                yield line.strip()



def test_list(filename):
    tracemalloc.start()

    start = time.perf_counter()

    errors = read_errors_list(filename)

    end = time.perf_counter()

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return len(errors), end - start, peak / (1024 * 1024)


def test_generator(filename):
    tracemalloc.start()

    start = time.perf_counter()

    count = 0

    for error in read_errors_generator(filename):
        count += 1

    end = time.perf_counter()

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return count, end - start, peak / (1024 * 1024)


filename = "server.log"


create_dummy_log(filename, 50000)

print("server.log created successfully!")


list_count, list_time, list_memory = test_list(filename)
gen_count, gen_time, gen_memory = test_generator(filename)


print("\n===== LIST-BASED =====")
print("ERROR records:", list_count)
print("Execution time:", list_time, "seconds")
print("Peak memory:", list_memory, "MB")

print("\n===== GENERATOR-BASED =====")
print("ERROR records:", gen_count)
print("Execution time:", gen_time, "seconds")
print("Peak memory:", gen_memory, "MB")



print("\n===== COMPARISON =====")

if list_time < gen_time:
    print("List-based solution was faster.")
else:
    print("Generator-based solution was faster.")

if list_memory < gen_memory:
    print("List-based solution used less memory.")
else:
    print("Generator-based solution used less memory.")

##OUTPUT:-
---------------
server.log created successfully!

===== LIST-BASED =====
ERROR records: 5000
Execution time: 0.048529401999985566 seconds
Peak memory: 1.0352439880371094 MB

===== GENERATOR-BASED =====
ERROR records: 5000
Execution time: 0.04941391099998782 seconds
Peak memory: 0.020921707153320312 MB

===== COMPARISON =====
List-based solution was faster.
Generator-based solution used less memory.
