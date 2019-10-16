#!/usr/bin/env python
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#ALGO1-:-Introduction-à-l'algorithmique" data-toc-modified-id="ALGO1-:-Introduction-à-l'algorithmique-1"><span class="toc-item-num">1&nbsp;&nbsp;</span><a href="https://perso.crans.org/besson/teach/info1_algo1_2019/" target="_blank">ALGO1 : Introduction à l'algorithmique</a></a></div><div class="lev1 toc-item"><a href="#Cours-Magistral-7" data-toc-modified-id="Cours-Magistral-7-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Cours Magistral 7</a></div><div class="lev2 toc-item"><a href="#Plus-longue-sous-séquence-commune" data-toc-modified-id="Plus-longue-sous-séquence-commune-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Plus longue sous séquence commune</a></div><div class="lev2 toc-item"><a href="#Algorithme-de-Bellman-Ford" data-toc-modified-id="Algorithme-de-Bellman-Ford-22"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Algorithme de Bellman-Ford</a></div><div class="lev2 toc-item"><a href="#Algorithme-de-Floyd-Warshall" data-toc-modified-id="Algorithme-de-Floyd-Warshall-23"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Algorithme de Floyd-Warshall</a></div><div class="lev2 toc-item"><a href="#Résolution-du-problème-du-sac-à-dos-par-programmation-dynamique" data-toc-modified-id="Résolution-du-problème-du-sac-à-dos-par-programmation-dynamique-24"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Résolution du problème du sac à dos par programmation dynamique</a></div><div class="lev2 toc-item"><a href="#Mémoïzation-générique" data-toc-modified-id="Mémoïzation-générique-25"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Mémoïzation générique</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-26"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>Conclusion</a></div>

# # [ALGO1 : Introduction à l'algorithmique](https://perso.crans.org/besson/teach/info1_algo1_2019/)
# 
# - [Page du cours](https://perso.crans.org/besson/teach/info1_algo1_2019/) : https://perso.crans.org/besson/teach/info1_algo1_2019/
# - Magistère d'Informatique de Rennes - ENS Rennes - Année 2019/2020
# - Intervenants :
#   + Cours : [Lilian Besson](https://perso.crans.org/besson/)
#   + Travaux dirigés : [Raphaël Truffet](http://perso.eleves.ens-rennes.fr/people/Raphael.Truffet/)
# - Références :
#   + [Open Data Structures](http://opendatastructures.org/ods-python.pdf)

# # Cours Magistral 7
# 
# - Ce cours traite des algorithmes par programmation dynamique.

# ---
# ## Plus longue sous séquence commune

# In[13]:


def longest_common_subsequence(x, y):
    """Longest common subsequence

    Dynamic programming

    :param x:
    :param y: x, y are lists or strings
    :returns: longest common subsequence in form of a string
    :complexity: `O(|x|*|y|)`
    """
    n = len(x)
    m = len(y)
    #                      -- compute optimal length
    A = [[0 for j in range(m + 1)] for i in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if x[i] == y[j]:
                A[i + 1][j + 1] = A[i][j] + 1
            else:
                A[i + 1][j + 1] = max(A[i][j + 1],  A[i + 1][j])
    #                      -- extract solution
    sol = []
    i, j = n, m
    while A[i][j] > 0:
        if A[i][j] == A[i - 1][j]:
            i -= 1
        elif A[i][j] == A[i][j - 1]:
            j -= 1
        else:
            i -= 1
            j -= 1
            sol.append(x[i])
    return ''.join(sol[::-1])    # inverse solution


# Exemples :

# In[14]:


longest_common_subsequence("BABAR", "ACAB")


# In[15]:


longest_common_subsequence("J'aime bien les oiseaux !", "Les oiseaux sont des animaux à protéger.")


# In[16]:


longest_common_subsequence("Je suis amoureux de la vie", "Tu n'es pas amoureux d'elle ?")


# ---
# ## Algorithme de Bellman-Ford

# In[25]:


def bellman_ford(graph, weight, source=0):
    """ Single source shortest paths by Bellman-Ford

    :param graph: directed graph in listlist or listdict format
    :param weight: can be negative.
                   in matrix format or same listdict graph
    :returns: distance table, precedence table, bool
    :explanation: bool is True if a negative circuit is
                  reachable from the source, circuits
                  can have length 2.
    :complexity: `O(|V|*|E|)`
    """
    n = len(graph)
    dist = [float('inf')] * n
    prec = [None] * n
    dist[source] = 0
    for nb_iterations in range(n):
        changed = False
        for node in range(n):
            for neighbor in graph[node]:
                alt = dist[node] + weight[node][neighbor]
                if alt < dist[neighbor]:
                    dist[neighbor] = alt
                    prec[neighbor] = node
                    changed = True
        if not changed:                   # fixed point
            return dist, prec, False
    return dist, prec, True


# Un exemple de graphe, comme celui utilisé [dans la page Wikipédia](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm#Example) :

# In[26]:


oo = float('+inf')

weight = [
    [0, oo, -2, oo],
    [4, 0, 3, oo],
    [oo, oo, 0, 2],
    [oo, -1, oo, 0],
]


# In[27]:


n = len(weight)
graph = [
    [ v for v in range(n) if weight[u][v] < oo ]
    for u in range(n)
]


# In[28]:


bellman_ford(graph, weight)


# ---
# ## Algorithme de Floyd-Warshall

# In[17]:


from copy import deepcopy


# In[18]:


def floyd_warshall(weight):
    """All pairs shortest paths by Floyd-Warshall

    :param weight: edge weight matrix
    :returns: weight, and True if there are negative cycles
    :complexity: :math:`O(|V|^3)`
    """
    weight = deepcopy(weight)
    V = range(len(weight))
    for k in V:  # considering paths using 0..k
        # to go from u to v
        for u in V:
            for v in V:
                weight[u][v] = min(weight[u][v],
                                   weight[u][k] + weight[k][v])
    for v in V:
        if weight[v][v] < 0:      # negative cycle found
            return weight, True
    return weight, False


# Un exemple de graphe, comme celui utilisé [dans la page Wikipédia](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm#Example) :

# In[21]:


oo = float('+inf')

weight = [
    [0, oo, -2, oo],
    [4, 0, 3, oo],
    [oo, oo, 0, 2],
    [oo, -1, oo, 0],
]


# In[22]:


floyd_warshall(weight)


# <img width="75%" src="figures/CM7_Floyd-Warshall.png">

# ---
# ## Résolution du problème du sac à dos par programmation dynamique

# In[29]:


def knapsack(p, v, cmax):
    """Knapsack problem: select maximum value set of items if total size not
    more than capacity

    :param p: table with size of items
    :param v: table with value of items
    :param cmax: capacity of bag
    :requires: number of items non-zero
    :returns: value optimal solution, list of item indexes in solution
    :complexity: O(n * cmax), for n = number of items
    """
    n = len(p)
    opt = [[0] * (cmax + 1) for _ in range(n + 1)]
    sel = [[False] * (cmax + 1) for _ in range(n + 1)]
    #                               --- basic case
    for cap in range(p[0], cmax + 1):
        opt[0][cap] = v[0]
        sel[0][cap] = True
    #                               --- induction case
    for i in range(1, n):
        for cap in range(cmax + 1):
            if cap >= p[i] and opt[i-1][cap - p[i]] + v[i] > opt[i-1][cap]:
                opt[i][cap] = opt[i-1][cap - p[i]] + v[i]
                sel[i][cap] = True
            else:
                opt[i][cap] = opt[i-1][cap]
                sel[i][cap] = False
    #                               --- reading solution
    cap = cmax
    solution = []
    for i in range(n-1, -1, -1):
        if sel[i][cap]:
            solution.append(i)
            cap -= p[i]
    return (opt[n - 1][cmax], solution)


# On peut considérer l'exemple de la page Wikipédia :
# 
# For example, there are 10 different items and the weight limit is 67.
# And with : $$\begin{align}
# &w[  1]= 23 ,w[  2]= 26,w[  3]= 20,w[  4]= 18,w[  5]= 32,w[  6]= 27,w[  7]= 29,w[  8]= 26,w[  9]= 30,w[ 10]= 27 \\
# &v[  1]=505 ,v[  2]=352,v[  3]=458,v[  4]=220,v[  5]=354,v[  6]=414,v[  7]=498,v[  8]=545,v[  9]=473,v[ 10]=543 \\
# \end{align}$$

# In[30]:


p = [23, 26, 20, 18, 32, 27, 29, 26, 30, 27]  # param p, table with size of items
v = [505, 352, 458, 220, 354, 414, 498, 545, 473, 543]  # param v, table with value of items
cmax = 67  # param cmax, capacity of bag


# In[31]:


knapsack(p, v, cmax)


# $$\begin{align}
# &m(10, 67) = 1270\\
# &m(9, 67) = 1270, m(9, 40) = 678\\
# &m(8, 67) = 1270, m(8, 40) = 678, m(8, 37) = 545\\
# &m(7, 67) = 1183, m(7, 41) = 725, m(7, 40) = 678, m(7, 37) = 505\\
# &m(6, 67) = 1183, m(6, 41) = 725, m(6, 40) = 678, m(6, 38) = 678, m(6, 37) = 505\\
# &m(5, 67) = 1183, m(5, 41) = 725, m(5, 40) = 678, m(5, 38) = 678, m(5, 37) = 505\\
# &m(4, 67) = 1183, m(4, 41) = 725, m(4, 40) = 678, m(4, 38) = 678, m(4, 37) = 505, m(4, 35) = 505\\
# &m(3, 67) = 963, m(3, 49) = 963, m(3, 41) = 505, m(3, 40) = 505, m(3, 38) = 505, m(3, 37) = 505, m(3, 35) = 505, m(3, 23) = 505, m(3, 22) = 458, m(3, 20) = 458\\
# &m(2, 67) = 857, m(2, 49) = 857, m(2, 47) = 505, m(2, 41) = 505, m(2, 40) = 505, m(2, 38) = 505, m(2, 37) = 505, m(2, 35) = 505, m(2, 29) = 505, m(2, 23) = 505\\
# &m(1, 67) = 505, m(1, 49) = 505, m(1, 47) = 505, m(1, 41) = 505, m(1, 40) = 505, m(1, 38) = 505, m(1, 37) = 505, m(1, 35) = 505, m(1, 29) = 505, m(1, 23) = 505\\
# \end{align}$$

# ---
# ## Mémoïzation générique

# In[1]:


from time import sleep


# In[2]:


def f1(n):
    sleep(3)
    return n + 3


# In[3]:


print("3 secondes...")
print(f1(10))  # 13, 3 secondes après


# In[4]:


def f2(n):
    sleep(4)
    return n * n


# In[5]:


print("4 secondes...")
print(f2(10))  # 100, 4 secondes après


# Mémoïsation générique, non typée

# In[6]:


def memo(f):
    memoire = {}  # dictionnaire vide, {} ou dict()
    def memo_f(n):
        if n not in memoire:
             memoire[n] = f(n)
        return memoire[n]
    return memo_f


# In[7]:


memo_f1 = memo(f1)

print("3 secondes...")
print(memo_f1(10))  # 13, 3 secondes après
print("0 secondes !")
print(memo_f1(10))  # instantanné !


# In[8]:


# différent de ces deux lignes !

print("3 secondes...")
print(memo(f1)(10))
print("3 secondes...")
print(memo(f1)(10))  # 3 secondes aussi !


# In[9]:


memo_f2 = memo(f2)

print("4 secondes...")
print(memo_f2(10))  # 100, 4 secondes après
print("0 secondes !")
print(memo_f2(10))  # instantanné !


# In[10]:


# bonus : on peut utiliser la syntaxe d'un décorateur en Python :

def fibo(n):
    if n <= 1: return 1
    else: return fibo(n-1) + fibo(n-2)

print("Test de fibo() non mémoisée :")
for n in range(10):
    print("F_{} = {}".format(n, fibo(n)))


# In[11]:


# version plus rapide !
@memo
def fibo(n):
    if n <= 1: return 1
    else: return fibo(n-1) + fibo(n-2)

print("Test de fibo() mémoisée (plus rapide) :")
for n in range(10):
    print("F_{} = {}".format(n, fibo(n)))


# In[12]:


@memo
def factorielle(n):
    if n <= 0: return 0
    elif n == 1: return 1
    else: return n * factorielle(n-1)

print("Test de factorielle() mémoisée :")
for n in range(10):
    print("{}! = {}".format(n, factorielle(n)))


# ## Conclusion
# 
# C'est bon pour aujourd'hui !
