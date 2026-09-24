## Exercise 6: Student Data Model (`student_model.py`)

* **Objective:** Implement a Student/Employee data model using dataclasses and compare it with a traditional class implementation[cite: 1].

* **Input:** Student attributes (name, student_id, gpa).

* **Output:** Formatted string representations (`__repr__`) demonstrating automatic boilerplate code generation.

* **Algorithm:**
  1. Define a modern Python `@dataclass` for the student model.
  2. Define a traditional Python class with an explicit `__init__` and `__repr__` method for comparison.
  3. Instantiate both and print their outputs to showcase syntax reduction.

* **Time Complexity:** O(1) for object instantiation.

* **Space Complexity:** O(1) per object instance.
