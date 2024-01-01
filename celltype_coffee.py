import pandas as pd
import os
import numpy as np
import sys
import shutil
directory = sys.argv[1]
threshold = sys.argv[2]
output_dir = sys.argv[3]
priority_alg = sys.argv[4]


def borda(ranked_lists):
    # Create a dictionary to store the scores for each candidate
    edge_scores = {}
    # Count the number of candidates
    num_edges = len(ranked_lists[0])
    #print("Length of edges:", num_edges)
    # Initialize scores for each candidate to zero
    for alg in ranked_lists:
        for i, edge in enumerate(alg):
            if edge not in edge_scores:
                edge_scores[edge] = 0
    
    # Calculate the Borda scores
    for alg in ranked_lists:
        #print("Length of algorithm:", len(alg))
        counter = 0
        for i, edge in enumerate(alg):
            #print("i", i)
            #print("edge", edge)
            #print("Adding edge to edge_scores", edge, "with score", num_edges - i - 1)
            edge_scores[edge] += num_edges - i - 1
    
    # Normalize the scores
    #total_points = num_edges * len(ranked_lists)
    #normalized_scores = {edge: score / total_points for edge, score in edge_scores.items()}
    for i in range(len(edge_scores.keys()) - num_edges):
        min_key = min(edge_scores.keys(), key=lambda k: edge_scores[k])
        del edge_scores[min_key]
    sorted_scores = dict(sorted(edge_scores.items(), key=lambda x:x[1], reverse=True))
    #print("Length of keys", len(sorted_scores.keys()))
    return sorted_scores

def make_ranked_list(directory):

    file_list = []
    counter = 0
    line_count = 0
    for filename in os.listdir(directory):
            print("Going through filename", filename)
            lct_file = os.path.join(directory, filename)
            lct_test_csv = pd.read_csv(lct_file, sep = "\t")
            lct_test_csv.columns = ['Gene1', 'Gene2', 'EdgeWeight']
            lct_test_csv = lct_test_csv[lct_test_csv['Gene1'] != lct_test_csv['Gene2']]
            if priority_alg in filename:
                line_count = len(lct_test_csv.index)
    for filename in os.listdir(directory):
            threshold = line_count
            #print("USING MIN THRESHOLD OF", threshold)
            f = os.path.join(directory, filename)
            test_csv = pd.read_csv(f, sep = "\t")
            test_csv.columns = ['Gene1', 'Gene2', 'EdgeWeight']
            test_csv = test_csv[test_csv['Gene1'] != test_csv['Gene2']]
            #print(test_csv)
            edges_1 = test_csv['Gene1'].tolist()[0:threshold]
            edges_2 = test_csv['Gene2'].tolist()[0:threshold]
            #weights = test_csv['EdgeWeight'].tolist()[0:threshold]
            edge_tuple = []

            for edge in range(len(edges_1)):
                edge_tuple.append((edges_1[edge], edges_2[edge]))

            file_list.append(edge_tuple)
            counter += 1
    return(file_list)


def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))



ranked_list = make_ranked_list(directory)


to_normalize = [i for i in range(len(ranked_list[0]))]
norm_list = list(NormalizeData(to_normalize))
norm_list.reverse()

result = borda(ranked_list)

edge_1 = []
edge_2 = []
scores = norm_list
for key in result.keys():
    edge_1.append(key[0])
    edge_2.append(key[1])

out_dict = {
    "Edge1" : edge_1,
    "Edge2" : edge_2, 
    "Scores" : scores
}

out_df = pd.DataFrame(out_dict)

# Write to csv
out_df = out_df[out_df.iloc[:, 2] >= float(threshold)]

os.chdir(output_dir)
threshold_path = str(threshold) + "_consensus_net"
if os.path.exists(threshold_path) and os.path.isdir(threshold_path):
        shutil.rmtree(threshold_path)
os.mkdir(threshold_path)
print("Created threshold_path of", threshold_path)
out_df.columns = ['Gene1', 'Gene2', 'EdgeWeight']
out_df.to_csv(threshold_path + "/consensus_network.tsv", sep = "\t", index = False)
print("Wrote final outfile")



