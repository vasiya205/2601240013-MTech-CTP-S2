from dataclasses import dataclass


@dataclass
class StudentDataclass:
  name: str
  student_id: int
  gpa: float


class StudentTraditional:

  def __init__(self, name: str, student_id: int, gpa: float):
    self.name = name
    self.student_id = student_id
    self.gpa = gpa

  def __repr__(self):
    return (
        f"StudentTraditional(name='{self.name}',"
        f" student_id={self.student_id}, gpa={self.gpa})"
    )


# Test Code
s_dc = StudentDataclass("Alice", 101, 3.8)
s_tr = StudentTraditional("Bob", 102, 3.6)

print("Dataclass Output:", s_dc)
print("Traditional Class Output:", s_tr)
