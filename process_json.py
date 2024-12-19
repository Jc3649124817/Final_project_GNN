
import json
import numpy as np
import os
import os.path as osp
import sys




def process_json():
    dir_path = "./json_files/"
    # file_names = []
    # for file_name in os.listdir(dir_path):
    #     file_names.append(file_name)
    
    # print(f"There are {len(file_names)} json files")
    #print(file_names[0])

    with open("match_file_list.json","r") as file:
        file_names = json.load(file)
    print(len(file_names))

    #key is the trait name, value is the max tier of the trait (current tier is from 0-max tier).
    possible_traits = {}
    #key is the unit name, value is the max tier of the unit (should be 4 for all, 1-4 as the range)
    possible_units = {}
    possible_items = []
    max_num_units = 0
    



    for file_name in file_names:
        file_path = osp.join(dir_path, file_name)
        #print(file_path)
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
        player_infos = data["info"]["participants"]
        for board in player_infos:
            traits_list = board["traits"]
            units_list = board["units"]
            if len(units_list) > 15:
                pass
                #print(units_list)
                print(len(units_list))
                print(file_name)

            max_num_units = max(max_num_units, len(units_list))
           
            for trait_dict in traits_list:
                if not (trait_dict["name"] in possible_traits):
                    possible_traits[trait_dict["name"]] = trait_dict["tier_total"]
            for unit_dict in units_list:
                if not (unit_dict["name"] in possible_units):
                    possible_units[unit_dict["character_id"]] = 4
                for item in unit_dict["itemNames"]:
                    if not (item in possible_items):
                        possible_items.append(item)

    relevant_stats = ["gold_left", "level", "puuid", "total_damage_to_players"]


    # print(possible_units)
    # print(possible_traits)
    # print(possible_items)
    print(len(possible_units.keys()))
    print(len(possible_traits.keys()))
    print(len(possible_items))


    print(max_num_units)   

    possible_list = [possible_units, possible_traits, possible_items]
    json_string = json.dumps(possible_list, indent=4)


    with open("possible_dicts.json", "w") as file:
        file.write(json_string)


    return possible_units, possible_traits, possible_items













    # player_list = data["metadata"]["participants"]
    # print(player_list)
    # print(len(player_list))
    # while:
    

    # playerinfo_dict = data["info"]["participants"]

    # for file in 

    # print(len(playerinfo_dict[0]))
    # print(playerinfo_dict[0].keys())

    # feature_array = np.zeros((0, ))
    # for board in playerinfo_dict:
    #     traits = board["traits"]
    #     units = board["units"]
    # for trait in traits:
    #     print(trait.keys())
    # for unit in units:
    #     print(unit.keys())

if __name__ == "__main__":
    process_json()