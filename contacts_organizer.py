"""
# Author: Richard Lu
# Project name: Contacts Organizer
# Date Started: October 2020
# Contact: richardlu0928@gmail.com
# Total Time used: 5 hours
# Last Updated: 2020/12/29
# Version: 1.0
"""

# This program can add contacts, delete contacts, search contacts and list
# out all contacts stored locally.
# Run the program with IDLE to edit contacts locally.

import os
from typing import List, Tuple, Dict, TextIO
from time import sleep


def add() -> None:
    name = input("Please input new contact's name: ")
    number = input("Please input new contact's number: ")
    address = input("Please input new contact's address. Simply press Enter "
                    "if not applicable: ")
    birth_date = input("Please input new contact's birth date. Simply press "
                       "Enter if not applicable: ")
    if address == '':
        address = '@!'
    if birth_date == '':
        birth_date = 'Birthday Unknown'
    concatenated = name + '\n' + number + '\n' + address + '\n' + birth_date
    file_contacts = 'contacts.txt'
    openfile = open(file_contacts, 'a')
    openfile.write(concatenated + '\n\n')
    openfile.close()
    print("New contact successfully added.")
    run()


def search() -> None:
    mode_1 = input("Type 1 to search by name, type 2 to search by phone "
                   "number, type 3 to search by address, type anything "
                   "else to exit the program: ")
    data = open('contacts.txt', 'r').read()
    data_array = data.split("\n\n")
    if data_array == ['']:
        print('File is empty with no contacts, please add one first.')
        run()
    del data_array[-1]
    if mode_1 == "1":
        name = []
        for i in data_array:
            listed = i.split('\n')
            name.append(listed[0])
        _search(name, data_array, "name")
    elif mode_1 == "2":
        number = []
        for i in data_array:
            listed = i.split('\n')
            number.append(listed[1])
        _search(number, data_array, "number")
    elif mode_1 == "3":
        print("Input @! to search all contacts without address inputted.")
        address = []
        for i in data_array:
            listed = i.split('\n')
            address.append(listed[2])
        _search(address, data_array, "address")
    else:
        print("Program exited. Thanks for using.")


def _search(search_spec: list, main_list: list, which: str) -> None:
    msg = input("Please input the " + which + ": ")
    print()
    if any(msg.lower().replace(" ", "") in i.lower().replace(" ", "")
           for i in search_spec):
        counted = 0
        counter = 1
        for j in search_spec:
            if msg.lower().replace(" ", "") in j.lower().replace(" ", ""):
                print("Contact Number " + str(counter) + ": ")
                print(main_list[counted])
                print()
                counter += 1
            counted += 1
        print("All data has been printed out.")
        run()
    else:
        print("Sorry, can't find this contact. Please restart the program.")


def list() -> None:
    data = open('contacts.txt', 'r').read()
    data_array = data.split("\n\n")
    _list(data_array)
    run()


def _list(data_array) -> None:
    if data_array == ['']:
        print('File is empty with no contacts, please add a contact first.')
        run()
    else:
        counter = 1
        for i in data_array[:-1]:
            print("Contact number " + str(counter) + ":")
            print(i + '\n')
            counter += 1
        print("All data has been printed out.")


def delete() -> None:
    data = open('contacts.txt', 'r').read()
    data_array = data.split("\n\n")
    _list(data_array)
    numb = input("Which contact number do you wish to delete: ")
    decision = input("This action cannot be undone, type 1 to confirm, "
                     "type anything else to undo: ")
    if decision == "1":
        numb = int(numb) - 1
        del data_array[numb]
        del data_array[-1]
        with open("contacts.txt", "w") as f:
            for i in data_array:
                f.write(i + '\n\n')
        print("Contact number " + str(numb + 1) + " has been deleted "
                                                  "successfully.")
        run()
    else:
        run()


def run() -> None:
    mode = input("Type 1 to add a contact, type 2 search a contact, type 3 to "
                 "list all contacts stored, type 4 to delete a contact, type "
                 "anything else to exit the program. "
                 "Press Enter after inputted: ")
    if mode == '1':
        print("Received. You want to add a contact. \n")
        add()
    elif mode == '2':
        print("Received. You want to search a contact. \n")
        search()
    elif mode == '3':
        print("Received. You want to list all contacts stored. \n")
        list()
    elif mode == '4':
        print("Received. You want to delete a stored contact. \n")
        delete()
    else:
        print("Program exited. Thanks for using.")
        exit()


if __name__ == '__main__':
    print("Welcome to Contacts Organizer, a program made by Richard Lu.")
    if not os.path.exists('contacts.txt'):
        with open('contacts.txt', 'w'):  # Create a new local file if not exist
            pass
    sleep(0.5)
    run()
