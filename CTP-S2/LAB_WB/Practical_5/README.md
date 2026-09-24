## Exercise 5: Banking Management System (`banking_system.py`)

* **Objective:** Develop a Banking Management System demonstrating inheritance and abstraction with full type hints[cite: 1].  

* **Input:** Account details (Account Number, Initial Balance) and transaction amounts for deposit/withdrawal.

* **Output:** Updated account balance or raised `ValueError` on insufficient funds.

* **Algorithm:**
  1. Define an abstract base class `Account` with abstract methods `deposit` and `withdraw`.
  2. Implement a derived class `SavingsAccount` inheriting from `Account`.
  3. Provide concrete implementations for balance modification and validation checks.

* **Time Complexity:** O(1) for basic deposit/withdrawal operations.

* **Space Complexity:** O(1) per account instance.
