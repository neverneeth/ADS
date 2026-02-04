"""
Docstring for BTR.generate_web_assets

File to generate JSON data for web visualization of associahedrons and binary trees.
"""

import sys
sys.path.append("./")

from src.BTR.map_rotations import AssociahedronGraph
import json
import os

def generate_web_assets(n: int, output_dir: str = "./web/static/BTR"):
    """
    Generates JSON files representing the associahedron graph and binary trees
    for web visualization.
    
    :param n: Size of the binary trees.
    :param output_dir: Directory to save the generated JSON files.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    associahedron = AssociahedronGraph(n)

    # Generate graph data
    graph_data = {
        "nodes": [],
        "edges": []
    }

    for node in associahedron.graph.nodes:
        graph_data["nodes"].append({"id": node})

    for edge in associahedron.graph.edges:
        graph_data["edges"].append({"source": edge[0], "target": edge[1]})

    with open(os.path.join(output_dir, f"associahedron_n{n}.json"), "w") as f:
        json.dump(graph_data, f, indent=4)

    print(f"Generated web assets for n={n} in {output_dir}")


if __name__ == "__main__":
    n = range(3, 8)
    for i in n:
        generate_web_assets(i)
