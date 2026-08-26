# Library Book Finder — Binary Search

## What is this program?
It's a simple book-finder for a huge library. Imagine a library with exactly 1,000,000 books, numbered 1 to 1,000,000 and arranged in order on the shelf. You tell it which book number you're looking for, and it tells you exactly where it sits.

## Description
Instead of checking book 1, then book 2, then book 3... (which would take forever), the program uses binary search. It jumps straight to the middle of the shelf, checks if that's the book you want, and if not, it figures out whether your book is to the left or right — then throws away the half it doesn't need. It keeps doing this, cutting the search area in half every time, until it either finds the book or runs out of shelf to search.

## Input
- A number typed in by the user — the book they want to find (somewhere between 1 and 1,000,000).

## Output
- The position of the book on the shelf, if it exists.
- A "book not found" message if it doesn't.

## Time Complexity
**O(log n)** — this is the whole point of binary search. Even with a million books, it only takes about 20 comparisons max to find any book, because each check cuts the remaining pile in half.

## Space Complexity
**O(n)** — a bit of a hidden cost here. The program actually builds the full list of 1,000,000 numbers in memory before searching it. The search itself doesn't need extra memory (that part is O(1)), but creating the array upfront does.

## Problem Decomposition
1. Build the sorted shelf (array of 1 to 1,000,000).
2. Keep two pointers — one at the start (`low`) and one at the end (`high`).
3. Check the middle book between them.
4. If it's a match, done. If the target is bigger, move `low` up. If smaller, move `high` down.
5. Repeat until found or the pointers cross.

## Pattern Recognition
This is the textbook **Divide and Conquer / Binary Search** pattern — you'll see this exact idea reused anywhere you're searching through *sorted* data efficiently: sorted arrays, sorted files, even guessing games ("higher or lower").
