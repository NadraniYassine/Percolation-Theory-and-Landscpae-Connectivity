from numpy import zeros, arange, exp
from numpy.random import rand
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

#Definition des états possibles de chaque site
ISOLANT = 0.0       #en blanc
CONDUCTEUR = 1.0    #en rouge
PERCO = 0.5         #en vert

# Definition des parametres de la simulation
N = 100

#Definition de la fonction sigmoïde
def Sigmoide(x,x0,k,a,c):
    return a/(1.0 + exp(-k*(x-x0))) + c
# Fonction de creation de la matrice carree de simulation.
# La probabilite p represente la proportion de sites conducteurs parmi l'ensemble des sites.
def Grid(n,p):
    grid = zeros((n,n))
    for i in range(n):
        for j in range(n):
            if rand() < p:
                 grid[i][j] = CONDUCTEUR
    return grid
#Algorithme de percolation isolant/conducteur
def Percolate(grid,n):
    pgrid = grid.copy()
    chemin = []
    #recherche des particules conductrices en haut de la matrice
    for j in range(n):
        if pgrid[0][j] == CONDUCTEUR:
            chemin.append((0,j))
            pgrid[0][j] = PERCO
    #recherche d'un chemin percolant
    while len(chemin) > 0:
        (i,j) = chemin.pop()
        pgrid[i][j] = PERCO
        if i > 0 and pgrid[i-1][0] == CONDUCTEUR:
            chemin.append((i-1,j))
            pgrid[i-1][j] = PERCO
        if i < n-1 and pgrid[i+1][j] == CONDUCTEUR:
            chemin.append((i+1,j))
            pgrid[i+1][j]=PERCO

        if j > 0 and pgrid[i][j-1] == CONDUCTEUR:
            chemin.append((i,j-1))
            pgrid[i][j-1] = PERCO
        if j < n-1 and pgrid[i][j+1] == CONDUCTEUR:
            chemin.append((i,j+1))
            pgrid[i][j+1] = PERCO
    return pgrid
# Fonction de calcul de la densite de percolation
def PercolateDensity(grid,n):
    a,b = 0.0,0.0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == PERCO:
                a += 1
            elif grid[i][j] == CONDUCTEUR:
                b += 1
    if a+b > 0:
        return a/(a+b)
    else: return 0
# Fonction de calcul de la densite de probabilite de percolation
# pour un echantillon de NbEch donne
def DPM(p):
    d =0.0
    for i in range(NbEch):
        mat = Grid(N,p)
        pmat = Percolate(mat,N)
        d += PercolateDensity(pmat,N)
        densite = d/NbEch
        return densite

# Definition des parametres du calcul
PasProba = 0.01
NbEch = 40

#Pour chaque probabilité p comprise entre 0.0 et 1.0 par pas de 0.05, calculer la densité de probabilité pour un échantillon de NbEssh
#Essais de percolation
px=arange(0.0,1.0,PasProba)
y=[DPM(p) for p in px]
#tracé de la courbe DPM(p)
plt.plot(px,y)
plt.grid()

# regression sigmoïde
#popt[0]=x0 donne le point d'inflexion
#popt[1]=k
#popt[2]=a
#popt[3]=c
popt,pcov = curve_fit(Sigmoide,px,y)
y = Sigmoide(px,*popt)
plt.plot(px,y,'red')

plt.show()
