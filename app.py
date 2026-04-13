import streamlit as st
from simulation import run_simulation

st.set_page_config(page_title="Chord DHT", layout="centered")

st.title("Chord Distributed Hash Table Simulation")

st.markdown(
    "This simulation demonstrates Chord lookup in a distributed ring. "
    "Each node maintains a finger table for efficient O(log N) lookup."
)

# Inputs
n = st.slider("Number of Nodes", 3, 15, 6)
key = st.number_input("Key to Lookup", min_value=0, max_value=31, value=10)

if st.button("Run Simulation"):

    nodes, log, hops, result_node = run_simulation(n, key)

    # Show nodes
    st.subheader("Ring Nodes")
    node_ids = [node.id for node in nodes]
    st.write("Nodes in ring:", node_ids)

    # Show lookup result
    st.subheader("Lookup Result")
    st.success(f"Key {key} found at Node {result_node.id}")
    st.metric("Number of Hops", hops)

    st.info("Chord lookup scales as O(log N)")

    st.markdown("---")

    # Finger table
    selected = st.selectbox("Select Node to view Finger Table", node_ids)

    for node in nodes:
        if node.id == selected:
            st.subheader(f"Finger Table for Node {node.id}")
            for i, entry in enumerate(node.finger_table):
                st.write(f"Entry {i}: start={entry[0]} → Node {entry[1].id}")

    st.markdown("---")

    # Logs
    st.subheader("Lookup Path")

    for line in log:
        if "Hop" in line:
            st.write("[HOP] " + line)
        elif "found" in line:
            st.success(line)
        else:
            st.text(line)