ADD_FOR_INDEX = 1


class MenuDisplay:
    @staticmethod
    def display(options):
        print("Todo List Application")
        for key, value in options.items():
            print(f"{key}. {value}")
        print("\n")


class AddItemMessage:
    @staticmethod
    def display(name):
        print(f"Item {name} successfully added to list!")


class EditItemMessage:
    @staticmethod
    def display(index):
        print(f"Item {index + ADD_FOR_INDEX} successfully modified!")


class DeleteItemMessage:
    @staticmethod
    def display(index):
        print(f"Item {index + ADD_FOR_INDEX} has been successfully deleted!")


class MarkItemMessage:
    @staticmethod
    def display(index):
        print(f"Item {index + ADD_FOR_INDEX} successfully marked as completed!")


class ListDisplay:
    @staticmethod
    def display(items):
        if not items:
            print("Todo List is empty!")
        else:
            for key, value in enumerate(items):
                print(key + ADD_FOR_INDEX, value.deadline if value.deadline else "", value, "(", value.description, ")")


class ItemDisplay:
    @staticmethod
    def display(index, item):
        print(index + ADD_FOR_INDEX, item.deadline if item.deadline else "", item, "(", item.description, ")")

