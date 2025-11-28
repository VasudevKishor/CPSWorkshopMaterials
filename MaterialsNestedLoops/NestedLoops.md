# Comprehensive Guide: Nested Loops

## 1. Theory & Mechanics

### Introduction
A **Nested Loop** is a programming construct where a loop exists entirely within the body of another loop. This structure is fundamental in computer science for handling multi-dimensional data structures (like matrices, tables, or images) and complex algorithmic patterns.

In computational terms, a nested loop represents a **hierarchical iteration**: for every single step of the parent process, the child process must complete its entire execution cycle.

### The Mental Models

#### The "Clock" Analogy
Think of a standard analog clock:
* **The Outer Loop** is the **Hour Hand**.
* **The Inner Loop** is the **Minute Hand**.

For the Hour Hand to move just **one step** (e.g., from 1 PM to 2 PM), the Minute Hand must complete a **full revolution** (0 to 60).

#### The "Odometer" Analogy
Think of a car mileage counter:
* The rightmost digit (inner loop) spins fast (0-9).
* Only when it completes a full cycle (9 -> 0) does the digit to its left (outer loop) increment by one.

### Syntax & Structure (Python)

```python
# The "Outer" Loop
for i in range(outer_limit):
    # Pre-processing for the row (Optional)
    
    # The "Inner" Loop
    for j in range(inner_limit):
        # The Core Logic
        # This block runs (outer_limit * inner_limit) times
        process(i, j)
        
    # Post-processing for the row (Optional)
    # e.g., print a new line
