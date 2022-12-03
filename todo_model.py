from todo_item import Item


class Model:
    def __init__(self):
        self.todo_items = []

    def add_item(self, name, description, deadline):
        self.todo_items.append(Item(name, description, deadline))

    def edit_item(self, index, name, description, deadline):
        self.todo_items[index] = Item(name, description, deadline)

    def delete_item(self, index):
        self.todo_items.pop(index)

    def mark_as_completed(self, index):
        self.todo_items[index].is_completed()

    def get_items(self):
        return self.todo_items

    def get_item(self, index):
        return self.todo_items[index]
