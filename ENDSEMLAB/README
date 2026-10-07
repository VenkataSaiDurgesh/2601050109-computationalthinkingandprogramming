# Server Log ERROR Extraction: List vs Generator

## 1. Problem Statement

A software company has a large server log file containing millions of records. 
The system needs to extract all `ERROR` messages.

The task is to implement two approaches:

1. A **list-based solution** that reads and stores all matching ERROR records.
2. A **generator-based solution** that yields matching ERROR records one at a time.

The two approaches are compared based on:

- Execution time
- Memory consumption

The goal is to understand why generator-based processing is suitable when the complete dataset does not need to be stored in memory.

---

## 2. Objective

The objectives of this experiment are:

- Extract ERROR messages from a server log.
- Implement the solution using a Python list.
- Implement the solution using a Python generator.
- Measure execution time.
- Measure peak memory consumption.
- Compare both approaches.
- Understand the advantages of lazy evaluation.

---

## 3. Technologies Used

- Python 3
- `time` module
- `tracemalloc` module
- Google Colab / Jupyter Notebook

---

## 4. Approach 1: List-Based Solution

The list-based solution reads the log file line by line.

If a line contains the word `ERROR`, it is added to a list.

```python
def read_errors_list(filename):
    errors = []

    with open(filename, "r") as file:
        for line in file:
            if "ERROR" in line:
                errors.append(line.strip())

    return errors

Working
1. Open the log file.
2. Read each line.
3. Check whether "ERROR" is present.
4. Store matching records in a list.
5. Return the complete list.
Advantage
All ERROR records are available after processing.
Disadvantage
All matching records must be stored in memory.
5. Approach 2: Generator-Based Solution
The generator-based solution uses the yield keyword.
def read_errors_generator(filename):    with open(filename, "r") as file:        for line in file:            if "ERROR" in line:                yield line.strip()


Working
1. Open the log file.
2. Read one line at a time.
3. Check whether "ERROR" is present.
4. Yield the matching record.
5. Continue with the next record.
The generator does not store all ERROR records in memory.
6. Dummy Log File
For testing, a dummy log file containing 50,000 records is generated.
The records contain:
- ERROR messages
- WARNING messages
- INFO messages
Every 10th record is an ERROR.
Therefore:
50,000 / 10 = 5,000 ERROR records

7. Performance Measurement
Execution Time
The time.perf_counter() function is used to measure execution time.
start = time.perf_counter()# Code executionend = time.perf_counter()execution_time = end - start


Memory Consumption
The tracemalloc module is used to measure memory usage.
tracemalloc.start()# Code executioncurrent, peak = tracemalloc.get_traced_memory()tracemalloc.stop()


The peak memory value is converted from bytes to megabytes.
8. Complexity Analysis
Let:
- N = total number of records in the log file
- K = number of ERROR records
List-Based Approach
Time Complexity:
O(N)

Every log record is checked once.
Space Complexity:
O(K)

All ERROR records are stored in the list.
Generator-Based Approach
Time Complexity:
O(N)

Every log record is checked once.
Extra Space Complexity:
O(1)

The generator processes matching records one at a time instead of storing them all.
9. Expected Result
The program produces output similar to:
server.log created successfully!

===== LIST-BASED =====
ERROR records: 5000
Execution time: 0.15 seconds
Peak memory: 0.40 MB

===== GENERATOR-BASED =====
ERROR records: 5000
Execution time: 0.12 seconds
Peak memory: 0.02 MB

===== COMPARISON =====
Generator-based solution was faster.
Generator-based solution used less memory.

Note: Actual execution time and memory values depend on the computer and Python environment.

10. Comparison
Feature	List-Based	Generator-Based
Processing	Stores all matching records	Processes one record at a time
Time Complexity	O(N)	O(N)
Space Complexity	O(K)	O(1) extra space
Memory Usage	Higher	Lower
Uses yield	No	Yes
Suitable for huge files	Less suitable	Highly suitable


11. Analysis / Inference
The experiment shows that both approaches have the same time complexity, O(N), because both need to scan the entire log file.
However, their memory requirements are different.
The list-based approach stores every ERROR message in memory. Therefore, memory consumption increases as the number of ERROR records increases.
The generator-based approach uses lazy evaluation. It produces one ERROR message at a time and does not store the complete set of matching records.
Therefore, the generator approach is more memory-efficient and scalable for very large log files.
12. Why Use a Generator?
Generator-based processing is suitable when the complete dataset does not need to be held in memory.
For example, a server may contain millions of log records. Storing all ERROR messages in a list could consume a large amount of memory.
A generator can process the data like this:
Read record
     ↓
Check for ERROR
     ↓
Yield ERROR record
     ↓
Process record
     ↓
Read next record

This makes generators useful for:
- Large server logs
- Streaming data
- Large files
- Database records
- Real-time data processing
13. Conclusion
The list-based and generator-based solutions successfully extract ERROR messages from the server log.
Both solutions have O(N) time complexity.
However, the generator-based solution uses significantly less memory because it processes records one at a time rather than storing all matching records.
Therefore:
Generator-based processing is the preferred approach for large datasets when all matching records do not need to be stored in memory simultaneously.

14. Viva Questions
Q1. What is a generator?
A generator is a Python function that produces values one at a time using the yield keyword.
Q2. What is the main difference between a list and a generator?
A list stores all values in memory, while a generator produces values one at a time.
Q3. What is the time complexity of this program?
The time complexity of both approaches is O(N).
Q4. Which approach uses less memory?
The generator-based approach uses less memory.
Q5. Why is a generator useful for large files?
Because it does not store the complete dataset in memory and processes records one at a time.
15. How to Run
Step 1: Open Google Colab
Open:
https://colab.research.google.com/
Step 2: Create a New Notebook
Select:
File → New notebook

Step 3: Paste the Python Code
Paste the complete Python implementation into a code cell.
Step 4: Run the Program
Press:
Shift + Enter

Step 5: Observe the Results
Compare:
- Number of ERROR records
- Execution time
- Peak memory consumption
16. Project Structure
server-log-error-extraction/
│
├── server.log
├── main.py
└── README.md

