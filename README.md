# Advanced Data Structures(PECST495)

A collection of source code associated with learnings/assignments of the **Advanced Data Structures** Elective offered by the APJAKTU as taught at the College of Engineering Trivandrum

## Repository Structure
- `src/`: Contains the main source code for various data structures and algorithms.
- `src/structs/`: Contains implementations of specific data structures.
- `src/BTR/`: Contains code related to Binary Tree Rotations
- `results/`: Directory to store results generated from experiments.
- `web/`: Contains code and assets for the web interface.

## Getting Started
1. **Clone the Repository**:
    ```bash
        git clone https://github.com/neverneeth/ADS
        cd ADS 
    ```
2. **Set Up Virtual Environment**:
    ```bash
        python -m venv venv
        source venv/bin/activate
    ```
3. **Install Dependencies**:
    ```bash
        pip install -r requirements.txt
    ```

4. **Running Code**:
    - Run all code from the root directory(`./ADS`) to ensure correct module imports.
    eg.
    ```python
        python -m src.BTR.map_rotations
    ``` 

## Binary Tree Rotations
The `src/BTR/` directory contains code related to binary tree rotations and their applications. It includes:
- `map_rotations.py`: Code to construct rotation graphs and compute rotation distances.
- `experiments.py`: Code to run empirical analysis and benchmarking experiments.
### Experiments
The `src/BTR/experiments.py` script allows you to run empirical analysis and benchmarking experiments on binary tree rotations. You can specify the range of binary tree sizes and the directory to save results.

To run the experiments, use the following command:
```bash
python -m src.BTR.experiments --min_n <min_size> --max_n <max_size> --results_dir <results_directory>
```
- `--min_n`: Minimum size of binary trees (default: 3)
- `--max_n`: Maximum size of binary trees (default: 7)
- `--results_dir`: Directory to save results (default: `./results/BTR`)
### Results
Results from experiments are saved in the `results/BTR/` directory by default. You can specify a different directory when running the experiments script.