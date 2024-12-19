import json
import numpy as np
import os
import os.path as osp

if __name__ == "__main__":
    dir_path = "./json_files/"
    file_names = []
    for file_name in os.listdir(dir_path):
        file_names.append(file_name)
    
    print(f"There are {len(file_names)} json files")
    
    final_file_names = file_names.copy()
    for file_name in file_names:
        break_file = False

        file_path = osp.join(dir_path, file_name)
        #print(file_path)
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
        set_num = data["info"]["tft_set_number"]
        game_type =  data["info"]["tft_game_type"]
        #print(set_num, game_type)

        if set_num != 13 or game_type != "standard":
            final_file_names.remove(file_name)
        elif len(data["info"]["participants"]) != 8:
            final_file_names.remove(file_name)
    
    


        # player_infos  = data["info"]["participants"]
        
        # for board in player_infos:

        #     num_units = len(board["units"])
        #     if num_units > 12 or num_units < 4:
        #         file_names.remove(file_name) 
        #         break

        #     for unit_name in board["units"]:
        #         if not ("TFT13" in unit_name) and not("tft13" in unit_name):
        #             file_names.remove(file_name)
        #             break_file = True
        #             break
        #     if break_file == True:
        #         break

    file_names = final_file_names.copy()
    
    for file_name in file_names:
        if "KR_" in file_name:
            final_file_names.remove(file_name)

    print(f"There now are {len(final_file_names)} json files")


    files_string = json.dumps(final_file_names, indent=4)

    with open("match_file_list.json", "w") as file:
        file.write(files_string)
