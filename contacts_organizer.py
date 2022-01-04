"""
# Author: Richard Lu
# Project name: Contacts Organizer
# Date Started: October 2020
# Contact: admin@richardlu.ca
# Repo: https://github.com/Sprit-Fun/Contacts_Organizer
# Total Time used: 6 hours
# Last Updated: 2022/01/03
# Version: 1.01
"""

# This program can add contacts, delete contacts, search contacts and list
# out all contacts stored locally, encrypted with base64 for extra security.
# Run the program with any Python interpreter to edit contacts locally.

import base64
import os
from time import sleep
from typing import Dict, List, TextIO, Tuple


def encoding(info: str) -> str:
    info_bytes = info.encode("ascii")
    base64_bytes = base64.b64encode(info_bytes)
    encrypted = base64_bytes.decode("ascii")
    return encrypted


def decoding(info: str) -> str:
    base64_bytes = info.encode("ascii")
    info_bytes = base64.b64decode(base64_bytes)
    decrypted = info_bytes.decode("ascii")
    return decrypted


def print_i(chunk: str) -> None:
    dataed = chunk.split("\n")
    for i in dataed:
        print(decoding(i))
    print()


def add() -> None:
    name = input("Please input new contact's name: ")
    number = input("Please input new contact's number: ")
    address = input("Please input new contact's address. Simply hit Enter "
                    "if not applicable: ")
    birth_date = input("Please input new contact's birth date. Simply hit "
                       "Enter if not applicable: ")
    if address == '':
        address = '@!'
    if birth_date == '':
        birth_date = 'No birthday added'
    concatenated = encoding(name) + '\n' + encoding(number) + '\n' + \
                   encoding(address) + '\n' + encoding(birth_date)
    openfile = open('contacts', 'a')
    openfile.write(concatenated + '\n\n')
    openfile.close()
    print("New contact successfully added. \n")
    run()


def search() -> None:
    data = open('contacts', 'r').read()
    data_array = data.split("\n\n")
    if data_array == ['']:
        print('File is empty with no contacts, please add one first. \n')
        run()
    del data_array[-1]
    mode_1 = input("Type 1 to search by name, type 2 to search by phone "
                   "number, type 3 to search by address, type anything "
                   "else to exit the program: ")
    if mode_1 == "1":
        name = []
        for i in data_array:
            listed = i.split('\n')
            name.append(decoding(listed[0]))
        _search(name, data_array, "name")
    elif mode_1 == "2":
        number = []
        for i in data_array:
            listed = i.split('\n')
            number.append(decoding(listed[1]))
        _search(number, data_array, "number")
    elif mode_1 == "3":
        print("Input @! to search all contacts without address inputted.")
        address = []
        for i in data_array:
            listed = i.split('\n')
            address.append(decoding(listed[2]))
        _search(address, data_array, "address")
    else:
        print("Program exited. Thanks for using. \n")


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
                print_i(main_list[counted])
                counter += 1
            counted += 1
        print("All contacts have been printed out. \n")
        run()
    else:
        print("Sorry, can't find this contact. \n")
        run()


def list() -> None:
    data = open('contacts', 'r').read()
    data_array = data.split("\n\n")
    _list(data_array)
    run()


def _list(data_array) -> None:
    if data_array == ['']:
        print('File is empty with no contacts, please add a contact first. \n')
        run()
    else:
        counter = 1
        for i in data_array[:-1]:
            print("Contact number " + str(counter) + ":")
            print_i(i)
            counter += 1
        print("All data has been printed out. \n")


def delete() -> None:
    data = open('contacts', 'r').read()
    data_array = data.split("\n\n")
    _list(data_array)
    numb = input("Which contact number do you wish to delete: ")
    decision = input("This action cannot be undone, type 1 to confirm, "
                     "type anything else to undo: ")
    if decision == "1":
        numb = int(numb) - 1
        del data_array[numb]
        del data_array[-1]
        with open("contacts", "w") as f:
            for i in data_array:
                f.write(i + '\n\n')
        print("Contact number " + str(numb + 1) + " has been deleted "
                                                  "successfully. \n")
        run()
    else:
        print()
        run()


def run() -> None:
    mode = input("Input 1 to add a contact, 2 search a contact, 3 to "
                 "list all contacts stored, 4 to delete a contact, "
                 "anything else to exit the program. "
                 "Press Enter after input: ")
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
        print("Exiting now. Thank you for using!")
        exit()


if __name__ == '__main__':
    print("Welcome to Contacts Organizer V1.01 written by Richard Lu.")
    if not os.path.exists('contacts'):
        with open('contacts', 'w'):  # Create a new local file if not exist
            pass
    run()  # Start running
