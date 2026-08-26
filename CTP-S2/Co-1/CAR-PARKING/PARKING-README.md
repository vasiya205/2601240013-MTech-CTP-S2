# Parking Management System

## What is this program?
A simple command-line tool that runs a parking lot — think of it as the digital version of the guy in the booth with a clipboard, except this one does the math for you.

## Description
The lot has 100 slots. When a car pulls in, the system finds the first free slot and assigns it, noting the vehicle number and entry time. When the car leaves, it calculates how long it was parked and generates a bill (₹50/hour). You can also check how many slots are free at any time, and see a full list of who's currently parked. Everything runs through a repeating menu (1 to 5) until the user chooses to exit.

## Input
- A menu number (1–5) to pick an action.
- Vehicle number (text) when parking a car.
- Entry time and exit time (in hours).
- Slot number when releasing a car.

## Output
- A live count of total/occupied/available slots, plus which exact slots are free.
- A confirmation when a vehicle is parked, showing which slot it got.
- A bill breakdown when a vehicle leaves (duration × rate).
- A table of everyone currently parked.

## Time Complexity
- Checking availability: **O(n)** — it loops through all 100 slots.
- Allocating a slot: **O(n)** worst case — it scans for the first empty slot, and separately checks all existing entries to make sure the vehicle isn't already parked.
- Releasing a slot: **O(1)** — direct lookup by slot number.
- Showing parked vehicles: **O(k)**, where k is however many cars are currently parked.

## Space Complexity
**O(k)** — only occupied slots are stored in memory (in a dictionary), so it scales with how full the lot actually is, not the fixed capacity of 100.

## Problem Decomposition
1. Keep one dictionary as the single source of truth: `slot number → [vehicle, entry time]`.
2. Write one function per real-world action: check availability, park a car, release a car, list parked cars.
3. Wrap it all in a loop that just reads the user's menu choice and calls the right function.

## Pattern Recognition
This is a classic **menu-driven CRUD system** (Create/Read/Update/Delete) built on top of a **dictionary as a lookup table**. You'll see this same shape in almost any "management system" style project — inventory systems, booking systems, library systems — swap the entities and the logic barely changes.
