from printer import * 
from Subs.Body import * 
from get_key import get_key
from points import * 


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
            glitch_text(f"{skill.name}{skill}")
            print(f"[V//{skill.sub}]")# {glitch_text(f"{skill.name}{skill}")}]")
            
            

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

            # if skill_selected == 0:
                
                    
            #     for level in Body_Levels:
            #         for skill in level:
            #             print_right(skill.name)
                
        
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
            
            
