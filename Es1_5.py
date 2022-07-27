# LECTURES ON NETWORK SYSTEMS
# E1.5 

# If using the Spyder IDE, clear the console and the variable in the namespace
try:
    from IPython import get_ipython
    get_ipython().magic('clear')
    get_ipython().magic('reset -f')
except:
    pass

# Import packages
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import networkx as nx

# Import self defined functions
import ch1_lib  # Chapter 1 specific library
import lib  # General library

# For interactive graphs
import ipywidgets as widgets

# Settings
custom_figsize= (6, 4) # Might need to change this value to fit the figures to your screen
custom_figsize_square = (5, 5)  

# Close open plots
plt.close('all')

n = 5
# ----------------------------------------------------------------------------
# COMPLETE GRAPH
# ---------------------------------------------------------------------------
G = nx.complete_graph(n)
# Define adjiacency matrix A
Adj = nx.adjacency_matrix(G)+np.identity(n)
# Count neighbours
neigh = np.sum(Adj,axis=1)
# Create averaging matrix
A = Adj/neigh
print("\nA matrix: \n", A)

# Define position of nodes on graph
l = 1 # side of the polygon
pos0 = [0.2,0.2]
pos1 = [0.2+l,0.2]
pos2 = [pos1[0]+np.cos(72*np.pi/180)*l, pos1[1]+l*np.sin(72*np.pi/180)]
pos3 = [(pos1[0]+pos0[0])/2,l*np.sin(36*np.pi/180)+pos2[1]]
pos4 = [0.2-l*np.cos(72*np.pi/180),0.2+l*np.sin(72*np.pi/180)]
pos = {0: pos0,1: pos1,2:pos2,3:pos3,4:pos4}
fig, ax1 = plt.subplots(figsize = custom_figsize)  # Init figure
nx.draw_networkx(G, pos, node_size=200, ax = ax1)  # Draw network
ax1.margins(0.05) # Zooming out for better visualization
plt.title("Network Configuration: Complete Graph") 
for kp in ['right', 'top', 'bottom', 'left']:
    plt.gca().spines[kp].set_visible(False)

# Define initial state
x0 = [-2,-1,0,1,2]
# Choose the time horizon
T = 15
# Initialize figure
fig, ax2 = plt.subplots(figsize=custom_figsize)
states = lib.simulate_network(A,x0, T)  # Simulate network and save states for each time step in a t*n np.array
lib.plot_node_val_2D(states, x0, T, ax2)  # Visualize states in a 2D Graph
plt.title("Linear averaging over the complete graph") 

# ----------------------------------------------------------------------------
# CYCLE GRAPH
# ---------------------------------------------------------------------------
Gcycle = nx.cycle_graph(n)
# Define adjiacency matrix A
Adjcycle = nx.adjacency_matrix(Gcycle)+np.identity(n)
print("CYCLE GRAPH\nAdjiancency matrix: \n", Adjcycle)
# Count neighbours
neigh = np.sum(Adjcycle,axis=1)
# Create averaging matrix
Acycle = Adjcycle/neigh
print("CYCLE GRAPH\nA matrix: \n", Acycle)

# Define position of nodes on graph

fig, ax1 = plt.subplots(figsize = custom_figsize)  # Init figure
nx.draw_networkx(Gcycle, pos, node_size=200, ax = ax1)  # Draw network
ax1.margins(0.05) # Zooming out for better visualization
plt.title("Network Configuration: Cycle Graph") 
for kp in ['right', 'top', 'bottom', 'left']:
    plt.gca().spines[kp].set_visible(False)

# Define initial state
x0 = [-2,-1,0,1,2]
# Choose the time horizon
T =30
# Initialize figure
fig, ax2 = plt.subplots(figsize=custom_figsize)
states_cycle = lib.simulate_network(Acycle,x0, T)  # Simulate network and save states for each time step in a t*n np.array
lib.plot_node_val_2D(states_cycle, x0, T, ax2)  # Visualize states in a 2D Graph
plt.title("Linear averaging over the cycle graph") 

# ----------------------------------------------------------------------------
# STAR GRAPH
# ---------------------------------------------------------------------------
Gstar = nx.star_graph(4)
# Define adjiacency matrix A
Adjstar = nx.adjacency_matrix(Gstar)
# Count neighbours
neigh = np.sum(Adjstar+np.identity(n),axis=1)
# Create averaging matrix
Astar = (Adjstar+np.identity(n))/neigh
print("\n\nSTAR GRAPG: A matrix: \n", Astar)

# Define position of nodes on graph
l = 1 # side of the polygon
pos2 = [0.2,0.2]
pos3 = [0.2+l,0.2]
pos4 = [pos3[0]+np.cos(72*np.pi/180)*l, pos3[1]+l*np.sin(72*np.pi/180)]
pos0 = [(pos3[0]+pos2[0])/2,l*np.sin(36*np.pi/180)+pos1[1]]
pos1 = [0.2-l*np.cos(72*np.pi/180),0.2+l*np.sin(72*np.pi/180)]
pos = {0: pos0,1: pos1,2:pos2,3:pos3,4:pos4}
fig, ax1 = plt.subplots(figsize = custom_figsize)  # Init figure
nx.draw_networkx(Gstar, pos, node_size=200, ax = ax1)  # Draw network
ax1.margins(0.05) # Zooming out for better visualization
plt.title("Network Configuration: Cycle Graph") 
for kp in ['right', 'top', 'bottom', 'left']:
    plt.gca().spines[kp].set_visible(False)

# Define initial state
x0 = [-2,-1,0,1,2]
# Choose the time horizon
T = 15
# Initialize figure
fig, ax2 = plt.subplots(figsize=custom_figsize)
states_star = lib.simulate_network(Astar,x0, T)  # Simulate network and save states for each time step in a t*n np.array
lib.plot_node_val_2D(states_star, x0, T, ax2)  # Visualize states in a 2D Graph
plt.title("Linear averaging over the star graph") 

