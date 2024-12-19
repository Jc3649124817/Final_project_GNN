import numpy as np
from sklearn.metrics import pairwise_distances
from scipy.sparse import lil_matrix
import time

if __name__ == "__main__":
    
    feature_vector = np.load("standardized_feature_vectors.npy")
    num_nodes = feature_vector.shape[0]
    euclidian_distance_matrix = pairwise_distances(feature_vector)
    print(type(euclidian_distance_matrix))
    print(euclidian_distance_matrix.shape)


    adj_matrix = np.empty((num_nodes, num_nodes))

    time1 = time.time()

    for i in range(num_nodes):
        for j in range(num_nodes):
            if euclidian_distance_matrix[i,j] < 5 and i != j:
                adj_matrix[i,j] = 1
    
    num_edges = np.sum(adj_matrix)


    edge_list = np.zeros((2, int(num_edges)))

    edge_list_index = 0
    for i in range(num_nodes):
        for j in range(num_nodes):
            if adj_matrix[i,j] == 1:
                edge_list[0, edge_list_index] = i
                edge_list[1, edge_list_index] = j
                edge_list_index+=1



    print(edge_list)
    #np.save("edge_list.npy", edge_list)

    print(time.time() - time1)

    print(f"number of edges: {np.sum(adj_matrix)}") 
            


 




