# Student Attendance Report

## What is this program?
A little tool that a teacher could actually use — it takes attendance numbers for a class and spits out a clean report: who's below the safe attendance line, who's leading the class, and what the class average looks like.

## Description
For every student, the program asks for their name, how many classes were held, and how many they attended. From that it works out each student's attendance percentage, flags anyone under 75%, picks out the student with the best attendance, and calculates the overall class average — then prints it all in a readable report.

## Input
- Number of students.
- For each student: name, total classes conducted, classes attended.

## Output
- Each student's attendance percentage.
- A list of students who fell below 75%.
- The student with the highest attendance (and their %).
- The class's average attendance.

## Time Complexity
**O(n)** overall, where n is the number of students. Every step — collecting data, calculating percentages, filtering the low-attendance students, finding the top student, averaging — is just one straightforward pass through the list of students. Nothing nested, nothing expensive.

## Space Complexity
**O(n)** — two dictionaries are kept in memory (raw student data, and calculated percentages), each with one entry per student.

## Problem Decomposition
1. Collect raw data first, and only that (`get_student_data`).
2. Turn raw numbers into percentages as a separate step (`calculate_percentage`).
3. Everything after that — filtering by threshold, finding the max, averaging — is its own small, focused function.
4. Display logic is kept completely separate from the number-crunching.
5. `main()` just wires all these pieces together in order.

## Pattern Recognition
This is a **data pipeline pattern**: collect → transform → analyze → report. It's a very common shape for any kind of "reporting" tool — grades, sales figures, survey results — the steps stay the same, only the data changes.
