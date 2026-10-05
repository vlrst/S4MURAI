from Skillset import Body_Levels
from printer import split_print

skill_selected =0
counter =1
for level in Body_Levels:
        # for skill in level:    
        #     for i, option in enumerate(skill):
        #         #split_print("\033[2K\r", end="")
        #         print(str(option.name))
        #         print(str(i) + "\n")

        print(counter)
        counter+=1





         # if i == skill_selected:
                #     print( # NOT SPLIT_PRINT_CENTER BECAUSE ITS A SKILL SO WE WANT TO SHOW THE DESCRIPTION AS WELL
                #         f"\033[3m\033[45m\033[97m> {option.name}\033[0m"
                #     )
                # else: # NOT SPLIT_PRINT_CENTER BECAUSE ITS A SKILL SO WE WANT TO SHOW THE DESCRIPTION AS WELL
                #     print(
                #         f"  {option.name}")