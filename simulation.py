import random
import simpy
import chord

def run_simulation(n, key):

    m = 5  # identifier space (2^m)

    log = []

    # Create nodes with random IDs
    ids = sorted(random.sample(range(2**m), n))
    nodes = [chord.Node(i, m) for i in ids]

    nodes = chord.build_ring(nodes, m)

    # Pick random start node
    start_node = random.choice(nodes)

    # Perform lookup
    result_node, hops = chord.lookup(start_node, key, log)

    return nodes, log, hops, result_node