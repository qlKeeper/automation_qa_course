from dataclasses import dataclass

@dataclass
class Person:
    full_name: str
    firstname: str
    lastname: str
    age: int
    salary: int
    department: str
    email: str
    current_address: str
    permament_address: str