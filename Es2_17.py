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
import lib  # General library



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
print("COMPLETE GRAPH \nA matrix: \n", A)
lambdaA, wA = np.linalg.eig(np.transpose(A))
# The normalized (unit “length”) eigenvectors, such that the column wA[:,i] 
#is the left eigenvector of A corresponding to the eigenvalue lambdaA[i].

# compute dominant left eigenvector
dom_eigvec = wA[:,lambdaA.argmax()]
# normalize it so that w'1_n = 1
dom_eigvec = dom_eigvec/dom_eigvec.sum()

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
x0 = [1,-1,1,-1,1]
# Choose the time horizon
T = 30
# Initialize figure
fig, ax2 = plt.subplots(figsize=custom_figsize)
states = lib.simulate_network(A,x0, T)  # Simulate network and save states for each time step in a t*n np.array
lib.plot_node_val_2D(states, x0, T, ax2)  # Visualize states in a 2D Graph
plt.title("Linear averaging over the complete graph") 

print("\nExpected final vector: ",x0@dom_eigvec*np.ones(5))
print("Actual final vector:   ",states[-1,:])

# ----------------------------------------------------------------------------
# CYCLE GRAPH
# ---------------------------------------------------------------------------
Gcycle = nx.cycle_graph(n)
# Define adjiacency matrix A
Adjcycle = nx.adjacency_matrix(Gcycle)+np.identity(n)
print("\nCYCLE GRAPH\nAdjiancency matrix: \n", Adjcycle)
# Count neighbours
neigh = np.sum(Adjcycle,axis=1)
# Create averaging matrix
Acycle = Adjcycle/neigh
print("\nA matrix: \n", Acycle)

lambdaAcycle, wAcycle = np.linalg.eig(np.transpose(Acycle))
# The normalized (unit “length”) eigenvectors, such that the column wA[:,i] 
#is the left eigenvector of A corresponding to the eigenvalue lambdaA[i].

# compute dominant left eigenvector
dom_eigvec = wAcycle[:,lambdaAcycle.argmax()]
# normalize it so that w'1_n = 1
dom_eigvec = dom_eigvec/dom_eigvec.sum()


# Define position of nodes on graph

fig, ax1 = plt.subplots(figsize = custom_figsize)  # Init figure
nx.draw_networkx(Gcycle, pos, node_size=200, ax = ax1)  # Draw network
ax1.margins(0.05) # Zooming out for better visualization
plt.title("Network Configuration: Cycle Graph") 
for kp in ['right', 'top', 'bottom', 'left']:
    plt.gca().spines[kp].set_visible(False)

# Choose the time horizon
T =30
# Initialize figure
fig, ax2 = plt.subplots(figsize=custom_figsize)
states_cycle = lib.simulate_network(Acycle,x0, T)  # Simulate network and save states for each time step in a t*n np.array
lib.plot_node_val_2D(states_cycle, x0, T, ax2)  # Visualize states in a 2D Graph
plt.title("Linear averaging over the cycle graph") 
print("\nExpected final vector: ",x0@dom_eigvec*np.ones(5))
print("Actual final vector:   ",states_cycle[-1,:])

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
print("STAR GRAPG\n: A matrix: \n", Astar)

lambdaAstar, wAstar = np.linalg.eig(np.transpose(Astar))
# The normalized (unit “length”) eigenvectors, such that the column wA[:,i] 
#is the left eigenvector of A corresponding to the eigenvalue lambdaA[i].

# compute dominant left eigenvector
dom_eigvec = wAstar[:,lambdaAstar.argmax()]
# normalize it so that w'1_n = 1
dom_eigvec = dom_eigvec/dom_eigvec.sum()

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

# Choose the time horizon
T = 30
# Initialize figure
fig, ax2 = plt.subplots(figsize=custom_figsize)
states_star = lib.simulate_network(Astar,x0, T)  # Simulate network and save states for each time step in a t*n np.array
lib.plot_node_val_2D(states_star, x0, T, ax2)  # Visualize states in a 2D Graph
plt.title("Linear averaging over the star graph") 
print("\nExpected final vector: ",x0@dom_eigvec*np.ones(5))
print("Actual final vector:   ",states_star[-1,:])
