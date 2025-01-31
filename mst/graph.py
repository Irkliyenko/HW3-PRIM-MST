import numpy as np
import heapq
from typing import Union
from collections import defaultdict

class Graph:

    def __init__(self, adjacency_mat: Union[np.ndarray, str]):
        """
    
        Unlike the BFS assignment, this Graph class takes an adjacency matrix as input. `adjacency_mat` 
        can either be a 2D numpy array of floats or a path to a CSV file containing a 2D numpy array of floats.

        In this project, we will assume `adjacency_mat` corresponds to the adjacency matrix of an undirected graph.
    
        """
        if type(adjacency_mat) == str:
            self.adj_mat = self._load_adjacency_matrix_from_csv(adjacency_mat)
        elif type(adjacency_mat) == np.ndarray:
            self.adj_mat = adjacency_mat
        else: 
            raise TypeError('Input must be a valid path or an adjacency matrix')

        self.adjList = defaultdict(list)
        self.mst = np.zeros_like(self.adj_mat)

    def _load_adjacency_matrix_from_csv(self, path: str) -> np.ndarray:
        with open(path) as f:
            return np.loadtxt(f, delimiter=',')

    def construct_mst(self):
        """
        Constructs the Minimum Spanning Tree (MST) using Prim's Algorithm.
        Stores the MST as an adjacency matrix in `self.mst`.
        """

        # Initialize MST structures
        visited = set()
        heap = []
        start_node = 0 
        visited.add(start_node)

        # Convert adjacency matrix to adjacency list
        for i in range(len(self.adj_mat)):
            for j in range(len(self.adj_mat[i])):
                if self.adj_mat[i][j] > 0:  # If an edge exists
                    self.adjList[i].append((j, self.adj_mat[i][j]))  # (neighbor, weight)

        # Push all edges from start_node into the heap
        for neighbor, weight in self.adjList[start_node]:
            heapq.heappush(heap, (weight, start_node, neighbor))  # Store (weight, src, dest)

        while len(visited) < len(self.adj_mat) and heap:
            weight, src, dest = heapq.heappop(heap)  # Extract the smallest edge
            
            if dest not in visited:
                # Add edge to MST
                visited.add(dest)
                self.mst[src][dest] = weight
                self.mst[dest][src] = weight  

                # Push all edges of the new node into the heap
                for neighbor, edge_weight in self.adjList[dest]:
                    if neighbor not in visited:
                        heapq.heappush(heap, (edge_weight, dest, neighbor))

        

