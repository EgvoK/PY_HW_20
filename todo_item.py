class Item:
    def __init__(self, name, description, deadline=None, completed=None):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.completed = completed

    def is_completed(self):
        self.completed = True
        self.deadline = None

    def __str__(self):
        mark = "V" if self.completed else " "
        return f"[{mark}] {self.name}"
