from typing import TypeVar, Generic, List

# Define a type variable for generic typing
T = TypeVar('T')

class Repository(Generic[T]):
    """
    A reusable generic repository for enterprise objects (Customer, Product, Employee, etc.).
    """
    def __init__(self) -> None:
        self.items: List[T] = []

    def add(self, item: T) -> None:
        self.items.append(item)
        print(f"Added successfully: {item}")

    def get_all(self) -> List[T]:
        return self.items

# --- Example Usage ---
if __name__ == "__main__":
    print("--- Customer Repository ---")
    customer_repo = Repository[str]()
    customer_repo.add("Alice Smith (Customer ID: C001)")
    customer_repo.add("Bob Jones (Customer ID: C002)")
    print("All Customers:", customer_repo.get_all())

    print("\n--- Product Repository ---")
    product_repo = Repository[dict]()
    product_repo.add({"id": 101, "name": "Laptop", "price": 1200.00})
    product_repo.add({"id": 102, "name": "Mouse", "price": 25.50})
    print("All Products:", product_repo.get_all())
