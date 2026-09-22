# PEP 695 Type Parameter Syntax (Python 3.12+)
class DataStore[T]:
    """
    A reusable generic container using modern PEP 695 syntax.
    """
    def __init__(self) -> None:
        self.items: list[T] = []

    def add(self, item: T) -> None:
        self.items.append(item)
        print(f"Stored item: {item}")

    def get_all(self) -> list[T]:
        return self.items

# --- Example Usage ---
if __name__ == "__main__":
    print("--- String Data Store ---")
    string_store = DataStore[str]()
    string_store.add("ItemA")
    string_store.add("ItemB")
    print("All Strings:", string_store.get_all())

    print("\n--- Integer Data Store ---")
    int_store = DataStore[int]()
    int_store.add(500)
    int_store.add(1000)
    print("All Integers:", int_store.get_all())
