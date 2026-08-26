# Online Shopping Cart System

## What is this program?
A basic version of an online store's cart — the kind of thing running behind the scenes every time you shop on Amazon or Flipkart, just stripped down to a text menu.

## Description
There's a small catalog of 5 products (Laptop, Mobile, Headphones, Keyboard, Mouse) with fixed prices. The user can browse the catalog, add items to their cart (with a quantity), remove items, view the cart, and finally generate a bill. The bill isn't just "add it all up" — it applies a discount the user enters, then adds 18% GST on top of the discounted amount, giving a realistic final total.

## Input
- Menu choice (1–6).
- Product name and quantity, when adding or removing items.
- Discount percentage, when generating the final bill.

## Output
- The product catalog with prices.
- The current cart contents (product, price, quantity, line total).
- The final bill: subtotal → discount → amount after discount → GST → grand total.

## Time Complexity
- Displaying products: **O(p)**, p = number of products (5, but written generally).
- Adding/removing an item: essentially **O(1)** dictionary access, since product lookups are hash-based.
- Generating the bill: **O(c)**, c = number of distinct items sitting in the cart.

## Space Complexity
**O(c)** — the cart only stores what's actually been added, so memory use grows with the number of *distinct* products in the cart, not the whole catalog.

## Problem Decomposition
1. Catalog and cart are two separate dictionaries — one static, one dynamic.
2. Each user action (add, remove, view, bill) gets its own dedicated function.
3. Subtotal calculation is pulled out into its own reusable function.
4. The billing function builds on top of the subtotal, layering discount then GST.
5. A menu loop ties it all together based on user input.

## Pattern Recognition
Two patterns stacked together here:
- **Dictionary/hash-map lookup pattern** for fast product and cart access.
- **Layered calculation pattern** — subtotal → discount → tax → total — which is basically how every real billing or invoicing system works, whether it's a shop, a restaurant POS, or an e-commerce checkout.
