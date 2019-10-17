#!/usr/bin/env python
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#ALGO1-:-Introduction-à-l'algorithmique" data-toc-modified-id="ALGO1-:-Introduction-à-l'algorithmique-1"><span class="toc-item-num">1&nbsp;&nbsp;</span><a href="https://perso.crans.org/besson/teach/info1_algo1_2019/" target="_blank">ALGO1 : Introduction à l'algorithmique</a></a></div><div class="lev1 toc-item"><a href="#Cours-Magistral-8" data-toc-modified-id="Cours-Magistral-8-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Cours Magistral 8</a></div><div class="lev2 toc-item"><a href="#Algorithme-de-Ford-Fulkerson" data-toc-modified-id="Algorithme-de-Ford-Fulkerson-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Algorithme de Ford-Fulkerson</a></div><div class="lev3 toc-item"><a href="#Etape-de-base-:-augmente-un-chemin" data-toc-modified-id="Etape-de-base-:-augmente-un-chemin-211"><span class="toc-item-num">2.1.1&nbsp;&nbsp;</span>Etape de base : augmente un chemin</a></div><div class="lev3 toc-item"><a href="#Etape-de-base-:-ajoute-un-arc-retour" data-toc-modified-id="Etape-de-base-:-ajoute-un-arc-retour-212"><span class="toc-item-num">2.1.2&nbsp;&nbsp;</span>Etape de base : ajoute un arc retour</a></div><div class="lev3 toc-item"><a href="#Calcul-du-flot-maximum" data-toc-modified-id="Calcul-du-flot-maximum-213"><span class="toc-item-num">2.1.3&nbsp;&nbsp;</span>Calcul du flot maximum</a></div><div class="lev3 toc-item"><a href="#Exemple" data-toc-modified-id="Exemple-214"><span class="toc-item-num">2.1.4&nbsp;&nbsp;</span>Exemple</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-22"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Conclusion</a></div>

# # [ALGO1 : Introduction à l'algorithmique](https://perso.crans.org/besson/teach/info1_algo1_2019/)
# 
# - [Page du cours](https://perso.crans.org/besson/teach/info1_algo1_2019/) : https://perso.crans.org/besson/teach/info1_algo1_2019/
# - Magistère d'Informatique de Rennes - ENS Rennes - Année 2019/2020
# - Intervenants :
#   + Cours : [Lilian Besson](https://perso.crans.org/besson/)
#   + Travaux dirigés : [Raphaël Truffet](http://perso.eleves.ens-rennes.fr/people/Raphael.Truffet/)
# - Références :
#   + [Open Data Structures](http://opendatastructures.org/ods-python.pdf)

# # Cours Magistral 8
# 
# - Ce cours traite du problème du flot maximal.

# ---
# ## Algorithme de Ford-Fulkerson
# 
# - On va utiliser l'exemple donné sur la page Wikipédia :
#   <img width="30%" src="figures/CM8_Ford-Fulkerson_exemple.svg">
# - Cf. [la page Wikipédia](https://en.wikipedia.org/wiki/Ford-Fulkerson_algorithm).

# ### Etape de base : augmente un chemin

# In[14]:


def augment(graph, capacity, flow, val, u, target, visit):
    """ Find an augmenting path from u to target with value at most val."""
    visit[u] = True
    if u == target:
        return val
    for v in graph[u]:
        cuv = capacity[u][v]
        if not visit[v] and cuv > flow[u][v]:  # reachable arc
            res = min(val, cuv - flow[u][v])
            delta = augment(graph, capacity, flow, res, v, target, visit)
            if delta > 0:
                flow[u][v] += delta            # augment flow
                flow[v][u] -= delta
                return delta
    return 0


# ### Etape de base : ajoute un arc retour

# In[15]:


def add_reverse_arcs(graph, capac=None):
    """ Utility function for flow algorithms that need for every arc (u,v),
    the existence of an (v,u) arc, by default with zero capacity.
    graph can be in adjacency list, possibly with capacity matrix capac.
    or graph can be in adjacency dictionary, then capac parameter is ignored.

    :param capac: arc capacity matrix
    :param graph: in listlist representation, or in listdict representation,
    in this case capac is ignored
    :complexity: linear
    :returns: nothing, but graph is modified
    """
    for u, _ in enumerate(graph):
        for v in graph[u]:
            if u not in graph[v]:
                if type(graph[v]) is list:
                    graph[v].append(u)
                    if capac:
                        capac[v][u] = 0
                else:
                    assert type(graph[v]) is dict
                    graph[v][u] = 0


# ### Calcul du flot maximum

# In[16]:


def ford_fulkerson(graph, capacity, s, t):
    """Maximum flow by Ford-Fulkerson

    :param graph: directed graph in listlist or listdict format
    :param capacity: in matrix format or same listdict graph
    :param int s: source vertex
    :param int t: target vertex

    :returns: flow matrix, flow value
    :complexity: `O(|V|*|E|*max_capacity)`
    """
    add_reverse_arcs(graph, capacity)
    n = len(graph)
    flow = [[0] * n for _ in range(n)]
    INF = float('inf')
    while augment(graph, capacity, flow, INF, s, t, [False] * n) > 0:
        pass                         # work already done in _augment
    return (flow, sum(flow[s]))      # flow network, amount of flow


# ### Exemple
# Un exemple de graphe, comme celui utilisé [dans la page Wikipédia](https://en.wikipedia.org/wiki/Ford-Fulkerson_algorithm) :
# 
# <img width="30%" src="figures/CM8_Ford-Fulkerson_exemple.svg">

# In[17]:


A, B, C, D = 0, 1, 2, 3
graph = [
    [B, C], # A
    [C, D], # B
    [D], # C
    [], # D
]
capacity = [
    [0, 1000, 1000, 0], # A
    [0, 0, 1, 1000], # B
    [0, 0, 0, 1000], # C
    [0, 0, 0, 0], # D
]


# In[18]:


ford_fulkerson(graph, capacity, A, D)


# On voit que le résultat est le même que celui donné dans l'exemple sur Wikipédia :
# <img width="30%" src="figures/CM8_Ford-Fulkerson_exemple2.svg">

# ## Conclusion
# 
# C'est bon pour aujourd'hui !
