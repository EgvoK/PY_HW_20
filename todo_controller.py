import datetime
import os
import sys


from todo_view import *
from todo_model import Model

ADD_FOR_INDEX = 1


def cls():
    os.system("cls" if os.name == "nt" else "clear")


class Controller:
    OPTIONS = {"1": "Display Items",
               "2": "Display Item",
               "3": "Add Item",
               "4": "Edit Item",
               "5": "Delete Item",
               "6": "Mark Item",
               "0": "Exit"}

    def __init__(self):
        self.model = Model()

    def menu(self):
        cls()
        self.show_menu()

        while True:
            option = input("Enter option number: ")
            cls()
            self.show_menu()
            if option == "1":
                self.show_items()
            elif option == "2":
                self.show_item()
            elif option == "3":
                self.add_item()
            elif option == "4":
                self.edit_item()
            elif option == "5":
                self.delete_item()
            elif option == "6":
                self.mark_as_complete()
            elif option == "0":
                sys.exit()

    def show_menu(self):
        MenuDisplay.display(self.OPTIONS)

    def show_items(self):
        ListDisplay.display(self.model.get_items())

    def show_item(self):
        index = self.index_input()
        try:
            item = self.model.get_item(index)
            ItemDisplay.display(index, item)
        except IndexError:
            self.error_index()

    def add_item(self):
        name = self.name_input()
        description = self.description_input()
        deadline = self.deadline_input()
        self.model.add_item(name, description, deadline)
        AddItemMessage.display(name)

    def edit_item(self):
        index = self.index_input()
        name = self.name_input()
        description = self.description_input()
        deadline = self.deadline_input()
        try:
            self.model.edit_item(index, name, description, deadline)
            EditItemMessage.display(index)
        except IndexError:
            self.error_index()

    def delete_item(self):
        index = self.index_input()
        try:
            self.model.delete_item(index)
            DeleteItemMessage.display(index)
        except IndexError:
            self.error_index()

    def mark_as_complete(self):
        index = self.index_input()
        try:
            self.model.mark_as_completed(index)
            MarkItemMessage.display(index)
        except IndexError:
            self.error_index()

    @staticmethod
    def index_input():
        while True:
            try:
                index = int(input("Enter item index: "))
                return index - ADD_FOR_INDEX
            except ValueError:
                print("Error! Please enter a number!")

    @staticmethod
    def name_input():
        while True:
            return input("Enter item name: ").strip()

    @staticmethod
    def description_input():
        while True:
            return input("Enter item description: ").strip()

    @staticmethod
    def deadline_input():
        year_index = 0
        month_index = 1
        day_index = 2
        while True:
            try:
                date = input("Enter date of deadline (YYYY/MM/DD): ")
                if not date:
                    return None
                date = date.split("/")
                deadline = datetime.date(int(date[year_index]), int(date[month_index]), int(date[day_index]))
                return deadline
            except:
                print("Error! Incorrect date!")

    @staticmethod
    def error_index():
        print("Error! Incorrect index!")

