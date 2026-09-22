from dataclasses import dataclass

@dataclass
class InventoryItem:
    """
    Models an inventory item efficiently using Python's @dataclass.
    Automatically generates __init__, __repr__, and comparison methods.
    """
    product_id: str
    product_name: str
    quantity: int
    price: float

# --- Example Usage ---
if __name__ == "__main__":
    # Instantiating inventory items without writing a custom __init__ method
    item1 = InventoryItem(product_id="P1001", product_name="Wireless Mouse", quantity=50, price=29.99)
    item2 = InventoryItem(product_id="P1002", product_name="Mechanical Keyboard", quantity=25, price=89.50)
    
    # Printing objects (leveraging the automatic __repr__)
    print(item1)
    print(item2)
    
    # Calculating total stock value for item1
    total_value = item1.quantity * item1.price
    print(f"Total stock value for {item1.product_name}: ${total_value:.2f}")
