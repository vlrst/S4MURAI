import os
import time
import sys
import tty
import termios
import shutil
from tqdm import tqdm
from Skillset import * 
from Skill import * 
from Subs.Body import * 
from Subs.Cool import * 
from Subs.Intelligence import * 
from Subs.Reflexes import * 
from Subs.Technical_Ability import * 
from random import randint
from get_key import get_key
from points import * 


from enterX.enterCool import *
from enterX.enterBody import *

import time
from colorama import Fore, Style, init
init()


#printer.start()


from printer import print_centered, split_print_center, split_print, print_right, start, glitch_text













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
    split_print_center(f"        ATTRIBUTE POINTS  {attribute_points}")


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
        #print(selected)
        match selected: # learned that the index starts at 0 for this as well
            
            case 0: # enter body
                enterBody()
            case 1:
                enterCool()
            case 6:
                os.system('clear')
                split_print_center("\n\n> DISCONNECT ")
                time.sleep(.1)
                split_print_center("\nTERMINATING NEURAL LINK...\n")
                for i in tqdm(range(100)):
                    time.sleep(randint(1,10)/100)
                split_print_center("\n[CONNECTION LOST]")
                time.sleep(.5)
                split_print_center("STAY SAFE V...")
                break
   
            

        # Other options
        split_print_center(f"\nYou selected: {options[selected]}")
        # input("\nPress ENTER to return to the menu...")
