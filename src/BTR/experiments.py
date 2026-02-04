"""
Docstring for BTR.experiments

This experiment aims to:
    - Generate all trees of size n
    - Create there corresponding associahedrons
    - Plots the associahedrons using matplotlib
    - Save the plots as images in the 'results' folder
    - Record the runtime of each step and save it to csv file in 'results' folder
    - Record storage and memory usage and save it to csv file in 'results' folder
"""

import sys
sys.path.append("./")

from src.BTR.generate_all_rotations import generate_all_rotations
from src.BTR.map_rotations import AssociahedronGraph
from src.BTR.rotation_distance import compute_rotation_distance_matrix as compute_all_distances

import time
import os
import csv
import pandas as pd
import argparse


def run_experiments(mix_n: int, max_n: int, results_dir: str = "./results"):
    """
    Docstring for run_experiments
    
    :param mix_n: Lower bound for size of binary trees
    :type mix_n: int
    :param max_n: Upper bound for size of binary trees
    :type max_n: int
    :param results_dir: Directory to save results
    :type results_dir: str
    """
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    runtime_rows = []
    storage_rows = []

    for n in range(mix_n, max_n + 1):
        print(f"Running experiments for n={n}")

        start_time = time.time()
        trees, adjacency = generate_all_rotations(n)
        gen_time = time.time() - start_time

        start_time = time.time()
        associahedron = AssociahedronGraph(n)
        graph_time = time.time() - start_time

        associahedron.visualize(path = results_dir + "/plots")

        start_time = time.time()
        distances = compute_all_distances(n)
        dist_time = time.time() - start_time

        runtime_rows.append({
            'n': n,
            'generate_rotations_time': gen_time,
            'create_associahedron_time': graph_time,
            'compute_distances_time': dist_time
        })

        storage_rows.append({
            'n': n,
            'num_trees': len(trees),
            'num_edges': associahedron.graph.number_of_edges(),
            'tree_size': sys.getsizeof(trees),
            'associahedron_size': sys.getsizeof(associahedron.graph),
            'distance_matrix_size': distances[0].nbytes
        })


    runtime_df = pd.DataFrame(runtime_rows)
    runtime_df.to_csv(os.path.join(results_dir, 'runtime_data.csv'), index=False)

    storage_df = pd.DataFrame(storage_rows)
    storage_df.to_csv(os.path.join(results_dir, 'storage_data.csv'), index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run experiments on binary tree rotations and associahedrons.")
    parser.add_argument('--min_n', type=int, default=3, help='Minimum size of binary trees (default: 3)')
    parser.add_argument('--max_n', type=int, default=7, help='Maximum size of binary trees (default: 7)')
    parser.add_argument('--results_dir', type=str, default='./results/BTR', help='Directory to save results (default: ./results)')
    args = parser.parse_args()
    run_experiments(mix_n=args.min_n, max_n=args.max_n, results_dir=args.results_dir)