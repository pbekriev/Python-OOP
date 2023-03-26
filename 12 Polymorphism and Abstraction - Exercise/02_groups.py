from typing import List


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        new_person = Person(self.name, other.surname)
        return new_person


class Group:
    def __init__(self, name: str, people: List[Person]):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        new_group = Group(f"{self.name} {other.name}", self.people + other.people)
        return new_group

    def __getitem__(self, index):
        return f"Person {index}: {self.people[index]}"

    def __repr__(self):
        return f"Group {self.name} with members {', '.join([str(p) for p in self.people])}"
