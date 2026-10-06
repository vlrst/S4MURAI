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
from glitch import glitch_text
from random import randint
perk_points = 13
attribute_points = 5
import time
from colorama import Fore, Style, init
init()


#printer.start()


from printer import print_centered, split_print_center, split_print, print_right, start













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
    split_print_center(f"        ATTRIBUTE POINTS  {attribute_points}")


# ============================================================
# MAIN LOOP
# ============================================================

start()






def enterBody():

    body_options = [
        "[ O ] OVERVIEW",
        "[ S ] SKILLS",
        "[ P ] PERCENT",
        "[ B ] BACK"
    ]

    body_selected = 0

    # ========================================================
    # INITIAL SCREEN
    # ========================================================

    os.system("clear")
    split_print_center("\033[2J\033[H", end="")

    print("\n\n\n")

    # Scan
    split_print_center("> SCANNING SOMATIC SYSTEMS...")
    time.sleep(0.7)

    split_print_center("> STRENGTH NEURONS: DETECTED")
    split_print_center("> SKELETAL INTEGRITY: ANALYZED")
    split_print_center("> PHYSICAL OUTPUT CAPACITY: CALCULATED\n\n\n")

    # Body levels
    for level in Body_Levels:
        for skill in level:
            #split_print_center(body.name)
            #split_print(str([body]))
            print(f"[{skill.sub} {glitch_text(f"{skill.name}-{skill}")}]")
            glitch_text(f"{skill.name}-{skill.sub}")
            

    print("\n")

    # ========================================================
    # SAVE CURSOR POSITION
    #
    # Everything above this point will stay on scre en.
    # ========================================================

    print("\033[s", end="")

    # ========================================================
    # FUNCTION TO DRAW ONLY THE BODY MENU
    # ========================================================

    def draw_skills(levels, skills_in_level, skill_selected):
        
        os.system('clear')
        print("\n\n")
        # Return to beginning of menu
        print("\033[u", end="")
        for i, option in enumerate(levels):
            #print(f'THIS IS THE SKILL SELECTED {skill_selected} and it is at index {i}')
            print("\033[2K\r", end="")
            if i == skill_selected:
                split_print( # NOT SPLIT_PRINT_CENTER BECAUSE ITS A SKILL SO WE WANT TO SHOW THE DESCRIPTION AS WELL
                    f"\033[3m\033[45m\033[97m> Level {option}\033[0m"
                )
            else: # NOT SPLIT_PRINT_CENTER BECAUSE ITS A SKILL SO WE WANT TO SHOW THE DESCRIPTION AS WELL
                split_print(
                    f"  Level {option}"
                )

            if skill_selected == 0:
                
                    
                for level in Body_Levels:
                    for skill in level:
                        print_right(skill.name)
                
        
        # for level in [levels]:
        #         for skill in level:
        #             for i, option in enumerate(skill):
        #                 print(f'THIS IS THE SKILL SELECTED {skill_selected} and it is at index {i}')
        #                 print("\033[2K\r", end="")
        #                 if i == skill_selected:
        #                     split_print( # NOT SPLIT_PRINT_CENTER BECAUSE ITS A SKILL SO WE WANT TO SHOW THE DESCRIPTION AS WELL
        #                         f"\033[3m\033[45m\033[97m> {option.name}\033[0m"
        #                     )
        #                 else: # NOT SPLIT_PRINT_CENTER BECAUSE ITS A SKILL SO WE WANT TO SHOW THE DESCRIPTION AS WELL
        #                     split_print(
        #                         f"  {option.name}"
        #                     )
        while True:
            key = get_key()

        # --------------------------------
        # UP
        # --------------------------------

            if key == "\x1b[A":

                skill_selected -= 1

                if skill_selected < 0:
                    #skill_selected = len([i for level in Body_Levels for i in level]) - 1
                    skill_selected = len([1,2,3,4]) - 1

                draw_skills([1,2,3,4], Body_Levels, skill_selected)

            # --------------------------------
            # DOWN
            # --------------------------------

            elif key == "\x1b[B":

                skill_selected += 1

                #if skill_selected >= len([i for level in Body_Levels for i in level]):
                if skill_selected >= len([1,2,3,4]):
                    skill_selected = 0

                draw_skills([1,2,3,4], Body_Levels, skill_selected)

        

    def draw_body_menu():
        os.system('clear')
        print("\n\n")
        # Return to beginning of menu
        print("\033[u", end="")

        for i, option in enumerate(body_options):

            # Clear the current terminal line
            print("\033[2K\r", end="")

            if i == body_selected:
                split_print_center(
                    f"\033[3m\033[45m\033[97m> {option}\033[0m"
                )
            else:
                split_print_center(
                    f"  {option}"
                )

        print("\033[2K\r", end="")
        split_print_center(
            "        ↑ ↓  Navigate       ENTER  Select"
        )

        print("\033[2K\r", end="")
        split_print_center(
            f"        PERK POINTS  {perk_points}"
        )

        print("\033[2K\r", end="")
        split_print_center(
            f"        ATTRIBUTE POINTS  {attribute_points}"
        )

    # Draw menu for the first time
    draw_body_menu()

    # ========================================================
    # BODY MENU LOOP
    # ========================================================

    while True:

        key = get_key()

        # --------------------------------
        # UP
        # --------------------------------

        if key == "\x1b[A":

            body_selected -= 1

            if body_selected < 0:
                body_selected = len(body_options) - 1

            draw_body_menu()

        # --------------------------------
        # DOWN
        # --------------------------------

        elif key == "\x1b[B":

            body_selected += 1

            if body_selected >= len(body_options):
                body_selected = 0

            draw_body_menu()

        # --------------------------------
        # ENTER
        # --------------------------------

        elif key == "\r":

            if body_selected == 0:
                
                # OVERVIEW
                pass

            elif body_selected == 1:

                # SKILLS
                draw_skills([1,2,3,4], Body_Levels, skill_selected=0) # skill_selected=0 to start at the top

            elif body_selected == 2:

                # PERCENT
                pass

            elif body_selected == 3:

                # BACK
                return
            split_print_center(f"\nYou selected: {body_options[body_selected]}")
            
            

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
