import math
from numpy import zeros
from numpy.random import random
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
# Definition des paramètres de la simulation
ISOLANT = 0.0       	# en cyan
CONDUCTEUR = 1.0        # en marron
PERCO = 0.5             # en vert
N = 100

# Fonction de creation de la matrice de simulation.
def Grid(n,p):
    grid = zeros((n,n))
    for i in range(n):
        for j in range(n):
            if random() < p:
                grid[i][j]=CONDUCTEUR
    return grid

# Algorithme de percolation isolant/conducteur
def Percolate(grid):
    pgrid = grid.copy()
    n,n = pgrid.shape
    chemin = []

    # Recherche des particules conductrices en haut de la
    for j in range(n):
        if pgrid[0][j] == CONDUCTEUR:
            chemin.append((0,j))
            pgrid[0][j] = PERCO
    # Recherche d'un chemin percolant
    while len(chemin) > 0:
        i,j = chemin.pop()
        pgrid[i][j] = PERCO
        if i > 0 and pgrid[i-1][j] == CONDUCTEUR:
            chemin.append((i-1,j))
            pgrid[i-1][j] = PERCO
        if i < n-1 and pgrid[i+1][j] == CONDUCTEUR:
            chemin.append((i+1,j))
            pgrid[i+1][j] = PERCO
        if j > 0 and pgrid[i][j-1]==CONDUCTEUR:
            chemin.append((i,j-1))
            pgrid[i][j-1] = PERCO
        if j < n-1 and pgrid[i][j+1] == CONDUCTEUR:
            chemin.append((i,j+1))
            pgrid[i][j+1] = PERCO
    return pgrid

# Fonction de détérmination de la percolation
def IfPercolate(grid):
    n,n=grid.shape
    for j in range(n):
        if grid[n-1][j]==PERCO:
            return True
    return False

# Choisir une répartition conducteur/isolant
p=float(input("Choisissez une répartition conducteur/isolant "))
# Création de la grille de percolation
mat = Grid(N,p)
# Essai de percolation
pmat = Percolate(mat)
# Détermination si la percolation a eu lieu
if IfPercolate(pmat):
    print("Percolation")
else: print("Pas de percolation")
# Tracé de grilles
fig=plt.figure(figsize=(10,6))
axe1 = fig.add_subplot(2,2,1)
axe1.imshow(mat,origin = "upper",interpolation='nearest',cmap=ListedColormap(['cyan','green','brown']))
axe2=fig.add_subplot(2,2,2)
axe2.imshow(pmat,origin = "upper",interpolation='nearest',cmap=ListedColormap(['cyan','green','brown']))


plt.show()