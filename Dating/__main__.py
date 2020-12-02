import sys, os
from create_profile import create_profile
from find_match import find_match

actions = {
    '1' : create_profile,
    '2' : find_match,
    '3' : sys.exit
    }

while True:
    menu = str(input('\nWhat would you like to do?\n1) Create a profile\n2) Find a match\n3) Close the program\n'))
    if menu in actions:
        actions[menu]()
