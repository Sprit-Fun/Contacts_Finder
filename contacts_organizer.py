"""
# Author: Richard Lu
# Project name: Contacts Organizer
# Date Started: December 2020
# Contact: richardlu0928@gmail.com
# Total Time used: 3 hours
# Last Updated: 2020/12/29
# Version: 0.2
"""

# This program can add contacts, search contacts and list out all contacts
# stored locally. Run the program with IDLE to edit contacts locally.

import os
from typing import List, Tuple, Dict, TextIO
from time import sleep


def add():
    file_contacts = 'contacts.txt'
    openfile = open(file_contacts, 'w')
    listed = ['ok', 'something not right', 'just practicing']
    for i in listed:
        openfile.write(i)
    openfile.close()

    file_contacts = 'example.txt'
    openfile = open(file_contacts, 'r')
    openfile.readline()
    openfile.close()


def search():
    mode_1 = input("Type 1 to search by name, type 2 to search by phone "
                   "number, type 3 to search by address.")
    data = open('contacts.txt', 'r').read()
    data_array = data.split("\n\n")
    if data_array == ['']:
        print('File is empty with no contacts, please restart the program.')
        exit()
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
        print("Sorry, input failed. Please restart the program.")


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
        print("All data has been printed out. Thanks for using the program.")
    else:
        print("Sorry, can't find this contact. Please restart the program.")


def list():
    counter = 1
    data = open('contacts.txt', 'r').read()
    data_array = data.split("\n\n")
    if data_array == ['']:
        print('File is empty with no contacts, please restart the program.')
    else:
        for i in data_array:
            print("Contact number " + str(counter) + ":")
            print(i)
            counter += 1
            print()
        print("All data has been printed out. Thanks for using the program.")


if __name__ == '__main__':
    print("Welcome to Contacts Organizer, a program made by Richard Lu.")
    sleep(0.5)
    if not os.path.exists('contacts.txt'):
        with open('contacts.txt', 'w'):  # Create a new local file if not exist
            pass
    mode = input("Type 1 to add a contact, type 2 search a contact, type 3 to "
                 "list all contacts stored, press Enter after inputted.")
    if mode == '1':
        print("Received. You want to add a contact. \n")
        add()
    elif mode == '2':
        print("Received. You want to search a contact. \n")
        search()
    elif mode == '3':
        print("Received. You want to list all contacts stored. \n")
        list()
    else:
        print("Input invalid, unable to receive. Please restart the program.")
