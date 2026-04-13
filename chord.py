import math

class Node:
    def __init__(self, node_id, m):
        self.id = node_id
        self.m = m
        self.finger_table = []
        self.successor = None

    def __repr__(self):
        return f"Node({self.id})"


def build_ring(nodes, m):
    nodes = sorted(nodes, key=lambda x: x.id)

    # Assign successors
    for i in range(len(nodes)):
        nodes[i].successor = nodes[(i + 1) % len(nodes)]

    # Build finger tables
    for node in nodes:
        node.finger_table = []
        for i in range(m):
            start = (node.id + 2**i) % (2**m)
            successor = find_successor(nodes, start)
            node.finger_table.append((start, successor))

    return nodes


def find_successor(nodes, key):
    for node in nodes:
        if node.id >= key:
            return node
    return nodes[0]


# --------------------------
# LOOKUP (CHORD ROUTING)
# --------------------------

def closest_preceding_node(node, key):
    for i in reversed(range(len(node.finger_table))):
        finger_node = node.finger_table[i][1]
        if node.id < finger_node.id < key:
            return finger_node
    return node


def lookup(start_node, key, log):
    hops = 0
    current = start_node

    log.append(f"Start lookup from Node {current.id} for key {key}")

    while True:
        hops += 1

        successor = current.successor

        # Check if key lies between current and successor
        if current.id < key <= successor.id or current.id > successor.id:
            log.append(f"Key {key} found at Node {successor.id}")
            return successor, hops

        next_node = closest_preceding_node(current, key)

        log.append(f"Hop: Node {current.id} → Node {next_node.id}")

        if next_node == current:
            return successor, hops

        current = next_node