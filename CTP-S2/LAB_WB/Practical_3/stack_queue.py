from dataclasses import dataclass, field
from typing import Generic, List, TypeVar

T = TypeVar("T")


@dataclass
class Stack(Generic[T]):
  items: List[T] = field(default_factory=list)

  def push(self, item: T) -> None:
    self.items.append(item)

  def pop(self) -> T:
    return self.items.pop()


@dataclass
class Queue(Generic[T]):
  items: List[T] = field(default_factory=list)

  def enqueue(self, item: T) -> None:
    self.items.append(item)

  def dequeue(self) -> T:
    return self.items.pop(0)


# Test Code
s = Stack()
s.push(10)
s.push(20)
print("Stack Popped:", s.pop())

q = Queue()
q.enqueue("A")
q.enqueue("B")
print("Queue Dequeued:", q.dequeue())
