# HW 3: Prim's algorithm

---

## Description

The `mst/graph.py` script contains the `Graph` class, which takes the adjcency matrix or .csv files as an input. This class includes the implementation of the **Prim's** algorithm, defined in the `construct_mst` method, and `_load_adjacency_matrix_from_csv` method that loads .csv file as a adjency matrix.

## Class Methods and Attributes

### 1. **Initialization (`__init__`)**
**Description:**  
Initializes the graph using an adjacency matrix or a CSV file.

**Attributes:**
- `self.adj_mat` → Stores the adjacency matrix.
- `self.adjList` → Dictionary for adjacency list representation.
- `self.mst` → Stores the MST.

**Parameters:**
- `adjacency_mat` *(Union[np.ndarray, str])*:  
  A NumPy adjacency matrix or path to a CSV file.

---

### 2. **Loading from CSV (`_load_adjacency_matrix_from_csv`)**
**Description:**  
Reads an adjacency matrix from a CSV file.

**Parameters:**
- `path` *(str)*: Path to the CSV file.

**Returns:**
- *(np.ndarray)*: The loaded adjacency matrix.

---

### 3. **Constructing MST (`construct_mst`)**
**Description:**  
Builds the **Minimum Spanning Tree (MST)** using **Prim’s Algorithm**.

**Algorithm Overview:**
1. Start from node `0` and initialize a priority queue.
2. Extract the smallest edge and add the corresponding node to the MST.
3. Repeat until all nodes are included.

**Output:**
- Updates `self.mst` with the MST adjacency matrix.

---

## **Test Functions**

### **1. `check_mst()` (Helper Function)**
**Description:**  
A helper function that validates the correctness of the computed MST.

**Assertions:**
- The total weight of the MST is within the allowed error margin.
- The MST has exactly `n-1` edges for `n` nodes.
- The MST retains the same shape as the original adjacency matrix.

**Parameters:**
- `adj_mat` *(np.ndarray)* → Original adjacency matrix of the full graph.
- `mst` *(np.ndarray)* → Computed adjacency matrix of the MST.
- `expected_weight` *(int)* → Expected weight of the MST.
- `allowed_error` *(float, default=0.0001)* → Allowed numerical error margin.

---

### **2. `test_mst_small()`**
**Description:**  
Tests MST construction on a **small graph** stored in a CSV file.

**Process:**
1. Loads an adjacency matrix from `small.csv`.
2. Constructs the MST using `Graph.construct_mst()`.
3. Validates the MST using `check_mst()` with an expected weight of **8**.

**Expected Outcome:**  
- The MST contains exactly `n-1` edges.
- The total MST weight is **8**.
- The MST matrix has the correct shape.

---

### **3. `test_mst_single_cell_data()`**
**Description:**  
Tests MST construction using **single-cell data** from the **Slingshot R package**.

**Process:**
1. Loads **cell coordinates** from `slingshot_example.txt`.
2. Computes **pairwise distances** to form a weighted adjacency matrix.
3. Constructs the MST using `Graph.construct_mst()`.
4. Validates the MST using `check_mst()` with an expected weight of **57.263561605571695**.

**Expected Outcome:**  
- The MST contains exactly `n-1` edges.
- The total MST weight matches the expected value.
- The MST correctly represents the connectivity of the single-cell data.


* Write at least two unit tests for MST construction (2)

