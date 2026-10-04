import os
import time
import sys
import io 
import numpy
import printer
from Skillset import * 
from Skill import * 
from Subs.Body import * 
from Subs.Cool import * 
from Subs.Intelligence import * 
from Subs.Reflexes import * 
from Subs.Technical_Ability import * 
#from VARS import * 
#from ollama import chat as MODEL
#from ollama import ChatResponse
#import datetime
#import pyfiglet
#import random


# output_buffer = io.StringIO()
# sys.stdout = output_buffer

perk_points = 13
attribute_points = 5
import random
import time
from colorama import Fore, Style, init
import threading
init()


#printer.start()


from printer import print_centered, split_print_center, start




import sys
import termios
import tty
import os


def enterBody():
    os.system('clear')
    split_print_center("\033[2J\033[H", end="")
    print('\n\n\n')
    split_print_center("> SCANNING SOMATIC SYSTEMS...")
    time.sleep(0.7)
    split_print_center("> STRENGTH NEURONS: DETECTED")
    split_print_center("> SKELETAL INTEGRITY: ANALYZED")
    split_print_center("> PHYSICAL OUTPUT CAPACITY: CALCULATED")
    for level in Body_Levels:
        for body in level:
            split_print_center(body.name)
    pass

def enterCool():
    os.system('clear')
    pass

def enterIntelligence():
    os.system('clear')
    pass

def enterReflexes():
    os.system('clear')
    pass

def enterTechnicalAbility():
    os.system('clear')
    pass

def enterOverview():
    os.system('clear')
    pass




# ============================================================
# MENU
# ============================================================

options = [
    "[ B ] BODY",
    "[ C ] COOL",
    "[ I ] INTELLIGENCE",
    "[ R ] REFLEXES",
    "[ T ] TECHNICAL_ABILITY",
    "[ O ] OVERVIEW",
    "[ D ] DISCONNECT"
]

selected = 0


# ============================================================
# GET KEY FROM TERMINAL
# ============================================================

def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)

        key = sys.stdin.read(1)

        # Arrow keys begin with ESC
        if key == "\x1b":
            key += sys.stdin.read(2)

        return key

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


# ============================================================
# DRAW MENU
# ============================================================

def draw_menu():
    # Clear entire terminal and move cursor to top-left
    split_print_center("\033[2J\033[H", end="")

    print()
    print()
    #split_print_center("                 CYBERPUNK SKILL TREE")
    print()

    for i, option in enumerate(options):

        if i == selected:
            # Highlight selected option
            #print("\033[3m   italics    \033[0m")
            split_print_center(f"\033[3m\033[45m\033[97m> {option}\033[0m")

        else:
            split_print_center(f"  {option}")

    print()
    split_print_center("        ↑ ↓  Navigate       ENTER  Select")
    split_print_center(f"        PERK POINTS  {perk_points}")
    split_print_center(f"        ATTRIBUTE POINTS  {perk_points}")


# ============================================================
# MAIN LOOP
# ============================================================

start()

while True:

    draw_menu()

    key = get_key()

    # UP ARROW
    if key == "\x1b[A":
        selected -= 1

        # Wrap around
        if selected < 0:
            selected = len(options) - 1

    # DOWN ARROW
    elif key == "\x1b[B":
        selected += 1

        # Wrap around
        if selected >= len(options):
            selected = 0

    # ENTER
    elif key == "\r":
        print(selected)
        match selected: # learned that the index starts at 0 for this as well
            
            case 0:
                enterBody()   
            case 1:
                enterCool()
                
            case 2:
                enterIntelligence()
            case 3:
                enterReflexes()
            case 4:
                enterTechnicalAbility()
        # Disconnect
            case 5:
                enterOverview()
            case 6:
                split_print_center("\nDisconnecting...")
                break

        # Other options
        split_print_center(f"\nYou selected: {options[selected]}")
        input("\nPress ENTER to return to the menu...")