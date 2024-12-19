The na1_api.py, euw1_api.py and asia_api.py were used to simultaneously request tft game data from the Riot Games API. They require no inputs and store the 
resulting json files in the folder ./json_files

delete_outliers.py and process_json.py gets rid of the games that are either non-standard or contain mistakes/formatting differnces
 (mostly the Korean games) from the list of match file names that the rest of the scripts use to create the graph structure. It also does some list creation to mistakes
 creating node_features easier in the next step.

create_feature_vectors.py takes the list of match file names, and creates  a (num_nodes, num_features) array, standardizes it and stores it in 
standardized_feature_vectors.npy. It also creates labels.npy which stores the ground truth for each node.


create_edges.py creates the edges between the most similar nodes using the euclidian distance between them and a threshold limit of 8.


At some point my laptop/VScode refused to recognize certain imports so I used final_project_gcn.ipynb to implement the GCN, using the base code
made by the instructors for colab 2. If you follow the cells, they show how I got the results. I copied final_project_gcn.ipynb but I have no idea 
if it will be able to reproduce the results or if it will crash whereas the ipynb should work as long as you have standardized_feature_vectors.npy,
edge_lists.npy, and labels.npy in its scope.


