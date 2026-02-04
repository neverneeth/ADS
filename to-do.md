# Empirical Analysis

- [x] Construct the Rotation Graph using the networkx package
    - [x] each vertex represents a binary tree with n nodes
    - [x] two trees are connected by an edge if one can be turned into the other by a single
rotation
- [ ] Visualize the graph using matplotlib
    - [ ] Presently nodes are labelled as post order traversals; find alternative. 
- [x] Compute rotation distance using BFS on the graph
- [x] Represent the rotation distance as a matrix

# Runtime Benchmarking

- [ ] For a fixed n, measure the execution time for 
    - [ ] generating all trees of size n
    - [ ] constructing the rotation graph
    - [ ] computing the distance matrix
- [ ] Create a csv file for recording the execution times, also include columns for number of trees in the file

# Memory Usage Profiling

- [ ] For each n record the memory usage for
    - [ ] storing the trees
    - [ ] storing the rotation graph
    - [ ] storing the distance matrix
- [ ] Create a csv file for these stats

