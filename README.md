# Chord Distributed Hash Table Simulation

> **Course:** Distributed Systems Lab  
> **Experiment:** Chord DHT Simulation  
> **Name** Jesna Binu Mancherikalam
  **Register Nummber**:22MID0066
---

##  Overview

This project implements a **Chord Distributed Hash Table (DHT)** simulation using Python.  

Chord is a decentralized distributed system protocol that enables efficient lookup of keys across a network of nodes using **consistent hashing** and **finger tables**.

The system demonstrates how nodes are organized in a ring and how lookup operations are performed in **O(log N)** time.

The user interface is built using Streamlit.

---
## How It Works

###  Ring Structure

- Nodes are arranged in a circular identifier space of size `2^m`
- Each node is assigned a unique ID
- Each node maintains a reference to its **successor**

Example:
Finger[i] = successor(node.id + 2^i)

This allows fast jumps across the ring.

---

### Lookup Algorithm

1. Start from a node
2. Check if key lies between current node and successor
3. Otherwise, jump to closest preceding node
4. Repeat until key is found

---

## Project Structure
chord-dht/
│
├── app.py # Streamlit UI
├── chord.py # Chord algorithm implementation
├── simulation.py # Simulation logic
├── requirements.txt
└── README.md

---

## Technologies Used

| Technology | Purpose |
|----------|--------|
| Python 3 | Core programming |
| Streamlit | Web interface |
| SimPy | Simulation support |

---


---

## Technologies Used

| Technology | Purpose |
|----------|--------|
| Python 3 | Core programming |
| Streamlit | Web interface |
| SimPy | Simulation support |

---



---

## Usage

1. Select number of nodes
2. Enter key value
3. Click "Run Simulation"
4. View:
   - Nodes in ring
   - Finger tables
   - Lookup path
   - Number of hops

---

## Sample Output

Nodes: [2, 7, 12, 18, 25]

Start lookup from Node 7 for key 10
Hop: Node 7 → Node 12
Key 10 found at Node 12

Hops: 2

---

## Complexity

| Operation | Complexity |
|----------|----------|
| Lookup | O(log N) |
| Finger table size | O(log N) |

---

## Key Concepts

- Distributed Hash Tables
- Consistent Hashing
- Ring Topology
- Efficient Routing

---

## Conclusion

This project demonstrates how distributed systems efficiently locate data using structured overlays like Chord.

It highlights scalability, decentralization, and logarithmic lookup performance.

---