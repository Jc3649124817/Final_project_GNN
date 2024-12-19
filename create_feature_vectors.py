
import json
import numpy as np
import os
import os.path as osp
import process_json
from sklearn.preprocessing import StandardScaler








if __name__ == "__main__":

    with open("possible_dicts.json","r") as file:
        possible_strings = json.load(file)
    possible_units = possible_strings[0]
    possible_traits = possible_strings[1]
    possible_items = possible_strings[2]
    

    #print(possible_units)
    units_list = list(possible_units.keys())
    traits_list = list(possible_traits.keys())
    items_list = possible_items

    relevant_stats = ["gold_left", "level", "players_eliminated", "total_damage_to_players"]

    #possible_units, possible_traits, possible_items = process_json.process_json()
    feature_vector_length = len(relevant_stats) + len(units_list) + len(traits_list) + len(items_list)
    unit_start_index = len(relevant_stats)
    trait_start_index = len(relevant_stats) + len(units_list)
    item_start_index = len(relevant_stats) + len(units_list) + len(traits_list)
    print(feature_vector_length)

    
    

    with open("match_file_list.json","r") as file:
        file_names = json.load(file)

    print(len(file_names))

    all_features = np.zeros((len(file_names) *8, feature_vector_length))
    labels = np.zeros((len(file_names) *8), dtype=np.int64)

    dir_path = "./json_files/"

    current_row = 0
    for file_name in file_names:
        #print("apple")

        file_path = osp.join(dir_path, file_name)
        #print(file_path)
        with open(file_path, "r") as json_file:
            data = json.load(json_file)

        #represents the feature vector of 1 node in one outer loop.
        for board in data["info"]["participants"]:
            if len(data["info"]["participants"]) != 8:
                print(len(data["info"]["participants"]))
            labels[current_row] = board["placement"]  - 1
            #print("appple")
            #player_row = np.zeros((1, feature_vector_length))
        
            #fill in the relevent stats
            for state, i in zip(relevant_stats, range(4)):
                all_features[current_row, i] = board[relevant_stats[i]]
            
            #fill in the possible units section
            
            for unit in board["units"]:
                
                unit_name = unit["character_id"]
                unit_tier = unit["tier"]
                partition_index = units_list.index(unit_name)
                all_features[current_row, unit_start_index + partition_index] =  unit_tier
                
                for item in unit["itemNames"]:
                    partition_index = items_list.index(item)
                    all_features[current_row, item_start_index + partition_index] = 1
            
            
            for trait in board["traits"]:
                #print(trait, current_row)
                trait_name = trait["name"]
                tier_current = trait["tier_current"]
                tier_total = trait["tier_total"]
                partition_index = traits_list.index(trait_name)
                actual_index = trait_start_index + partition_index
                #print(current_row, (trait_start_index + partition_index))
                all_features[current_row, actual_index] =  (float(tier_current) / float(tier_total))


            current_row+=1
    
    
    for i in range(0, 40):
        print(f'{i}: {all_features[18993, i]}')
    # print(all_features[0,3])
    # print(all_features[0,4])
    # print(all_features[0,5])

    print(unit_start_index)
    print(trait_start_index)
    print(item_start_index)

    np.save('original_feature_vector.npy', all_features)


    #normalize the features vectors:
    scalar = StandardScaler()
    scalar.fit(all_features)

    standarized_features = scalar.transform(all_features)

    for i in range(0, 40):
        print(f'{i}: {standarized_features[1131, i]}')

    
    np.save('standardized_feature_vectors.npy', all_features)
    print(labels[-8:])
    
    # for i in range(18993, len(labels)):
    #     if labels[i] != 0:
    #         print(i)
    #         break
    
    np.save("labels.npy", labels)
    




