#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#ALGO1-:-Introduction-à-l'algorithmique" data-toc-modified-id="ALGO1-:-Introduction-à-l'algorithmique-1"><span class="toc-item-num">1&nbsp;&nbsp;</span><a href="https://perso.crans.org/besson/teach/info1_algo1_2019/" target="_blank">ALGO1 : Introduction à l'algorithmique</a></a></div><div class="lev1 toc-item"><a href="#Cours-Magistral-4-&amp;-5" data-toc-modified-id="Cours-Magistral-4-&amp;-5-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Cours Magistral 4 &amp; 5</a></div><div class="lev2 toc-item"><a href="#Type-abstrait-des-$\alpha$-graphes" data-toc-modified-id="Type-abstrait-des-$\alpha$-graphes-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Type abstrait des <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-388-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mi>&amp;#x03B1;</mi></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-2772" style="width: 0.668em; display: inline-block;"><span style="display: inline-block; position: relative; width: 0.549em; height: 0px; font-size: 116%;"><span style="position: absolute; clip: rect(1.91em, 1000.55em, 2.596em, -1000em); top: -2.469em; left: 0em;"><span class="mrow" id="MathJax-Span-2773"><span class="mi" id="MathJax-Span-2774" style="font-family: STIXMathJax_Normal; font-style: italic;">𝛼<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.005em;"></span></span></span><span style="display: inline-block; width: 0px; height: 2.469em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.057em; border-left: 0px solid; width: 0px; height: 0.614em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi></math></span></span><script type="math/tex" id="MathJax-Element-388">\alpha</script> graphes</a></div><div class="lev3 toc-item"><a href="#Un-premier-exemple-de-graphe" data-toc-modified-id="Un-premier-exemple-de-graphe-211"><span class="toc-item-num">2.1.1&nbsp;&nbsp;</span>Un premier exemple de graphe</a></div><div class="lev3 toc-item"><a href="#Graphe-aléatoire-de-taille-$n$" data-toc-modified-id="Graphe-aléatoire-de-taille-$n$-212"><span class="toc-item-num">2.1.2&nbsp;&nbsp;</span>Graphe aléatoire de taille <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-408-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mi>n</mi></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-2883" style="width: 0.614em; display: inline-block;"><span style="display: inline-block; position: relative; width: 0.518em; height: 0px; font-size: 118%;"><span style="position: absolute; clip: rect(1.866em, 1000.49em, 2.597em, -1000em); top: -2.448em; left: 0em;"><span class="mrow" id="MathJax-Span-2884"><span class="mi" id="MathJax-Span-2885" style="font-family: STIXMathJax_Normal; font-style: italic;">𝑛</span></span><span style="display: inline-block; width: 0px; height: 2.448em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.065em; border-left: 0px solid; width: 0px; height: 0.641em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></span></span><script type="math/tex" id="MathJax-Element-408">n</script></a></div><div class="lev2 toc-item"><a href="#Trois-différentes-implémentations" data-toc-modified-id="Trois-différentes-implémentations-22"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Trois différentes implémentations</a></div><div class="lev3 toc-item"><a href="#Graphes-par-matrice-d'adjacence" data-toc-modified-id="Graphes-par-matrice-d'adjacence-221"><span class="toc-item-num">2.2.1&nbsp;&nbsp;</span>Graphes par matrice d'adjacence</a></div><div class="lev3 toc-item"><a href="#Graphes-par-listes-d'adjacence" data-toc-modified-id="Graphes-par-listes-d'adjacence-222"><span class="toc-item-num">2.2.2&nbsp;&nbsp;</span>Graphes par listes d'adjacence</a></div><div class="lev3 toc-item"><a href="#Graphes-par-liste-d'arêtes" data-toc-modified-id="Graphes-par-liste-d'arêtes-223"><span class="toc-item-num">2.2.3&nbsp;&nbsp;</span>Graphes par liste d'arêtes</a></div><div class="lev2 toc-item"><a href="#Test-numérique-des-complexités-des-différentes-opérations" data-toc-modified-id="Test-numérique-des-complexités-des-différentes-opérations-23"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Test numérique des complexités des différentes opérations</a></div><div class="lev2 toc-item"><a href="#Parcours-en-profondeur" data-toc-modified-id="Parcours-en-profondeur-24"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Parcours en profondeur</a></div><div class="lev2 toc-item"><a href="#Application-:-composantes-connexes-d'un-graphe-non-orienté" data-toc-modified-id="Application-:-composantes-connexes-d'un-graphe-non-orienté-25"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Application : composantes connexes d'un graphe non orienté</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-26"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>Conclusion</a></div>

# # [ALGO1 : Introduction à l'algorithmique](https://perso.crans.org/besson/teach/info1_algo1_2019/)
# 
# - [Page du cours](https://perso.crans.org/besson/teach/info1_algo1_2019/) : https://perso.crans.org/besson/teach/info1_algo1_2019/
# - Magistère d'Informatique de Rennes - ENS Rennes - Année 2019/2020
# - Intervenants :
#   + Cours : [Lilian Besson](https://perso.crans.org/besson/)
#   + Travaux dirigés : [Raphaël Truffet](http://perso.eleves.ens-rennes.fr/people/Raphael.Truffet/)
# - Références :
#   + [Open Data Structures](http://opendatastructures.org/ods-python.pdf)

# # Cours Magistral 4 & 5
# 
# - Ce cours traite de graphes.
# - On donne le type abstrait des graphes, et plusieurs implémentations de la même structure de données (plusieurs classes).
# 
# - CM4 : On implémente le parcours en profondeur, qu'on illustre sur quelques exemples.
# - CM5 : On implémente le parcours en largeur, qu'on illustre sur quelques exemples.

# ----
# ## Type abstrait des $\alpha$ graphes
# 
# On se donne un type $\alpha$ pour les sommets, et on va en fait se restreindre à $\alpha=$`int`, et les sommets seront $\{0,\dots,n-1\}$ où $n = |S|$ pour des graphes $G = (S, A)$.
# 
# On va écrire une classe qui implémente des opérations "plus haut niveau", en fonction des opérations bas niveau.

# In[1]:


class BaseGraph():
    def out_degree(self, vertex):
        return len(self.succ(vertex))

    def in_degree(self, vertex):
        return len(self.pred(vertex))
    
    def degree(self, vertex):
        return len(self.neighbors(vertex))

    def is_vertex(self, vertex):
        """ Test presence of a vertex."""
        return vertex in self.vertexes
    
    @property
    def vertexes(self):
        """ List of vertexes."""
        return list(range(self.nb_vertexes))
    
    def is_neighbor(self, u, v):
        """ Test neighborhood."""
        return u in self.neighbors(v)

    @property
    def edges(self):
        """ Set of edges (pairs), in O(|A|) if well implemented."""
        return {(u, v) for u in self.vertexes for v in self.neighbors(u)}
    
    @property
    def nb_edges(self):
        return len(self.edges)


# ### Un premier exemple de graphe
# 
# On va travailler avec le graphe exemple suivant, qu'il soit orienté ou non :
# 
# | Orienté | Non orienté |
# |---------|-------------|
# | <img width="75%" src="figures/CM4_ExampleDiGraph.png"> | <img width="75%" src="figures/CM4_ExampleGraph.png"> |

# In[2]:


def defaultGraph(GraphClass, oriented=True):
    print(f"Creating empty graph with class {GraphClass}...")
    graph = GraphClass(oriented=oriented)
    n = 7
    for i in range(n):
        print(f"Adding vertex {i}...")
        graph.add_vertex(i)
    for edge in [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]:
        print(f"Adding edge {edge}...")
        graph.add_edge(*edge)
    return graph


# On va tester les différentes implémentations avec la petite fonction suivante, qui vérifie que l'on peut accéder à toute l'information contenu dans le graphe.

# In[3]:


def test_defaultGraph(GraphClass):
    for oriented in [True, False]:
        graph = defaultGraph(GraphClass, oriented=oriented)
        print(f"Graph:")
        print(graph)
        print(f"Number of vertexes: {graph.nb_vertexes}")
        print(f"Is the graph oriented? {graph.oriented}")
        print(f"Number of edges: {graph.nb_edges}")
        print(f"List of vertexes: {graph.vertexes}")
        print(f"List of edges: {graph.edges}")
        for i in graph.vertexes:
            print(f"  List of neighbors of {i}: {graph.neighbors(i)} (degree {graph.degree(i)})")
            print(f"    List of succ of {i}: {graph.succ(i)} (out degree {graph.out_degree(i)})")
            print(f"    List of pred of {i}: {graph.pred(i)} (in degree {graph.in_degree(i)})")


# ### Graphe aléatoire de taille $n$
# 
# On va étudier un graphe aléatoire suivant un modèle très simple : on fixe $n$ le nombre de sommets, et ensuite chaque arête $(i, j)$ est ajoutée dans le graphe avec une probabilité $p\in(0,1)$ fixée ([graphe d'Erdös-Rényi](https://en.wikipedia.org/wiki/Erd%C5%91s-R%C3%A9nyi_model)).

# In[15]:


import random


# In[16]:


def with_probability(p):
    return random.random() <= p


# In[37]:


def randomGraph(GraphClass, n=10, probability=0.1, oriented=True):
    graph = GraphClass(oriented=oriented)
    for i in range(n):
        graph.add_vertex(i)
    for i in range(n):
        for j in range(n):
            if with_probability(probability):
                graph.add_edge(i, j)
    return graph


# In[38]:


print(randomGraph(AdjMatrixGraph, 10, 0.1, oriented=True))


# In[39]:


print(randomGraph(AdjMatrixGraph, 10, 0.5, oriented=True))


# In[40]:


print(randomGraph(AdjMatrixGraph, 10, 0.9, oriented=True))


# ----
# ## Trois différentes implémentations

# ### Graphes par matrice d'adjacence

# In[4]:


import numpy as np


# In[5]:


class AdjMatrixGraph(BaseGraph):
    def __init__(self, oriented=True, n=0):
        """ Takes O(n^2) time and space."""
        self.oriented = oriented
        self.nb_vertexes = n
        self._matrix = np.zeros((n, n), dtype=bool)
    
    def __str__(self):
        return str(self._matrix)

    def is_vertex(self, vertex):
        """ Test presence of a vertex."""
        return 0 <= vertex < self.nb_vertexes
    
    def add_vertex(self, m):
        """ Worst case is O(m^2) to extend the matrix. Best case is O(1) if nothing to do."""
        if not self.is_vertex(m):
            n = self.nb_vertexes
            assert 0 <= m and n <= m
            self.nb_vertexes = m + 1
            old_matrix = self._matrix[:,:]
            # extend the matrix
            self._matrix = np.zeros((m + 1, m + 1), dtype=bool)
            # copy the old matrix
            self._matrix[:n, :n] = old_matrix
    
    def add_edge(self, i, j):
        """ O(1) time."""
        assert 0 <= i < self.nb_vertexes and 0 <= j < self.nb_vertexes
        self._matrix[i, j] = True
        if not self.oriented:
            self._matrix[j, i] = True
    
    def remove_vertex(self, m):
        """ TODO do it yourself, it's not hard!"""
        raise NotImplementedError
    
    def remove_edge(self, i, j):
        """ O(1) time."""
        assert 0 <= i < self.nb_vertexes and 0 <= j < self.nb_vertexes
        self._matrix[i, j] = False
        if not self.oriented:
            self._matrix[j, i] = False
    
    def merge_vertexes(self, i, j):
        """ TODO do it yourself, it's not hard!"""
        raise NotImplementedError
    
    def pred(self, i):
        assert 0 <= i < self.nb_vertexes
        return [j for j in self.vertexes if self.is_neighbor(j, i)]
    
    def is_pred(self, u, v):
        """ O(1) time."""
        return self._matrix[v, u]
    
    def succ(self, i):
        assert 0 <= i < self.nb_vertexes
        return [j for j in self.vertexes if self.is_neighbor(i, j)]
    
    def is_succ(self, u, v):
        """ O(1) time."""
        return self._matrix[u, v]
    
    def neighbors(self, i):
        assert 0 <= i < self.nb_vertexes
        if self.oriented:
            return self.succ(i)
        else:
            return [j for j in self.vertexes if self.is_neighbor(i, j) or self.is_neighbor(j, i)]
    
    def is_neighbor(self, u, v):
        """ O(1) time."""
        if self.oriented:
            return self._matrix[u, v]
        else:
            return self._matrix[u, v] or self._matrix[v, u]


# Testons cette première implémentation :

# In[6]:


defaultGraph(AdjMatrixGraph)


# In[7]:


test_defaultGraph(AdjMatrixGraph)


# ### Graphes par listes d'adjacence

# In[8]:


class AdjListsGraph(BaseGraph):
    def __init__(self, oriented=True, n=0):
        """ Takes O(n) time and space to allocate the empty lists."""
        self.oriented = oriented
        self.nb_vertexes = n
        self._lists = [ [] for i in range(n) ]

    def __str__(self):
        return str(self._lists)
    
    def is_vertex(self, vertex):
        """ Test presence of a vertex."""
        return 0 <= vertex < self.nb_vertexes
    
    def add_vertex(self, m):
        """ Worst case is O(m^2) to extend the matrix. Best case is O(1) if nothing to do."""
        if not self.is_vertex(m):
            n = self.nb_vertexes
            assert 0 <= m and n <= m
            self.nb_vertexes = m + 1
            self._lists = [ [] if i >= n else self._lists[i] for i in range(m + 1) ]
    
    def add_edge(self, i, j):
        """ O(1) time: append j in head of list of neighbors of i."""
        assert 0 <= i < self.nb_vertexes and 0 <= j < self.nb_vertexes
        if not self.is_neighbor(i, j):
            self._lists[i].append(j)
        if not self.oriented:
            if not self.is_neighbor(j, i):
                self._lists[j].append(i)
    
    def remove_vertex(self, m):
        """ TODO do it yourself, it's not hard!"""
        raise NotImplementedError
    
    def remove_edge(self, i, j):
        """ O(1) time."""
        assert 0 <= i < self.nb_vertexes and 0 <= j < self.nb_vertexes
        self._lists[i].remove(j)
        if not self.oriented:
            self._lists[j].remove(i)
    
    def merge_vertexes(self, i, j):
        """ TODO do it yourself, it's not hard!"""
        raise NotImplementedError
    
    def pred(self, i):
        """ Not trivial, has to check all lists, in O(|S|*|A|)."""
        assert 0 <= i < self.nb_vertexes
        return [j for j in self.vertexes if self.is_pred(j, i)]
    
    def is_pred(self, u, v):
        """ O(|S|) time in worst case."""
        return u in self._lists[v]
    
    def succ(self, i):
        """ Create a new list, to be sure that we don't modify the underlying self._lists. In O(deg(i))."""
        assert 0 <= i < self.nb_vertexes
        return list(self._lists[i])
    
    def is_succ(self, u, v):
        """ O(|S|) time in worst case."""
        return v in self._lists[u]
    
    def neighbors(self, i):
        assert 0 <= i < self.nb_vertexes
        if self.oriented:
            return list(self.succ(i))
        else:
            return [j for j in self.vertexes if self.is_neighbor(i, j)]
    
    def is_neighbor(self, u, v):
        """ O(|S|) time in worst case."""
        if self.oriented:
            return v in self._lists[u]
        else:
            return v in self._lists[u] or u in self._lists[v]


# Testons cette première implémentation :

# In[9]:


defaultGraph(AdjListsGraph)


# In[10]:


test_defaultGraph(AdjListsGraph)


# ### Graphes par liste d'arêtes

# In[59]:


class EdgesListGraph(BaseGraph):
    def __init__(self, oriented=True, n=0):
        """ Takes O(n) time and space to allocate the empty lists."""
        self.oriented = oriented
        self.nb_vertexes = n
        self._edges = set()

    def __str__(self):
        return str(self._edges)
    
    def is_vertex(self, vertex):
        """ Test presence of a vertex."""
        return 0 <= vertex < self.nb_vertexes
    
    def add_vertex(self, m):
        """ Worst case is O(m^2) to extend the matrix. Best case is O(1) if nothing to do."""
        if not self.is_vertex(m):
            n = self.nb_vertexes
            assert 0 <= m and n <= m
            self.nb_vertexes = m + 1
    
    def add_edge(self, i, j):
        """ O(1) time: append j in head of list of neighbors of i."""
        assert 0 <= i < self.nb_vertexes and 0 <= j < self.nb_vertexes
        if not self.is_neighbor(i, j):
            self._edges.add((i, j))
        if not self.oriented:
            if not self.is_neighbor(j, i):
                self._edges.add((j, i))
    
    def remove_vertex(self, m):
        """ TODO do it yourself, it's not hard!"""
        raise NotImplementedError
    
    def remove_edge(self, i, j):
        """ O(1) time."""
        assert 0 <= i < self.nb_vertexes and 0 <= j < self.nb_vertexes
        self._edges.remove((i, j))
        if not self.oriented:
            self._edges.remove((j, i))
    
    def merge_vertexes(self, i, j):
        """ TODO do it yourself, it's not hard!"""
        raise NotImplementedError
    
    def pred(self, i):
        assert 0 <= i < self.nb_vertexes
        return [j for j in self.vertexes if self.is_pred(j, i)]
    
    def is_pred(self, u, v):
        """ O(|S|) time in worst case."""
        return (v, u) in self._edges
    
    def succ(self, i):
        assert 0 <= i < self.nb_vertexes
        return [j for j in self.vertexes if self.is_succ(i, j)]
    
    def is_succ(self, u, v):
        """ O(|S|) time in worst case."""
        return (u, v) in self._edges
    
    def neighbors(self, i):
        assert 0 <= i < self.nb_vertexes
        return [j for j in self.vertexes if self.is_neighbor(j, i)]
    
    def is_neighbor(self, u, v):
        """ O(|S|) time in worst case."""
        if self.oriented:
            return (u, v) in self._edges
        else:
            return (u, v) in self._edges or (v, u) in self._edges


# Testons cette première implémentation :

# In[60]:


defaultGraph(EdgesListGraph)


# In[61]:


test_defaultGraph(EdgesListGraph)


# ----
# ## Test numérique des complexités des différentes opérations
# 
# On rappelle qu'on devrait obtenir les résultats suivants, avec $n=|S|$, que l'on va valider expérimentalement.
# 
# | Opérations | Matrice d'adjacence | Listes d'adjacence | Liste d'arêtes |
# |:-----------|---------------------|--------------------|----------------|
# | Création (vide) | temps et mémoire $O(n^2)$ si vide | temps et mémoire $O(n)$ si vide | temps et mémoire $O(1)$ si vide |
# | Ajoute un sommet $u$ | $O(n^2)$ (recopie) | $O(1)$ | $O(1)$ |
# | Retire un sommet $u$ | $O(n^2)$ (recopie) | $O(d(u))$ si orienté, $O(|A|+|S|)$ sinon | $O(|A|)$ (suppression des arêtes) |
# | Ajoute un arc $(u,v)$ | $O(1)$ | $O(d(u))$ si orienté, $O(d(u)+d(v))$ sinon | $O(1)$ (si liste d'arêtes) ou $O(1)$ en amorti (si ensemble d'arêtes) |
# | Retire un arc $(u,v)$ | $O(1)$ | $O(d(u))$ si orienté, $O(d(u)+d(v))$ sinon | $O(|A|)$ (si liste d'arêtes) ou $O(1)$ en amorti (si ensemble d'arêtes) |
# | Liste des sommets | $O(n)$ | $O(n)$ | $O(n)$ |
# | Liste des arcs | $O(n^2)$ tout parcourir | $O(|A|)$ parcourir les $n$ listes de tailles $d(u)$, et $\sum_u d(u) = |A|$ | $O(1)$ (si liste d'arêtes) ou $O(|A|)$ (si ensemble d'arêtes) |
# | Liste des voisins du nœud $u$ | $O(n)$ | $O(d(u))$ ($O(1)$ si on ne crée pas de nouvelle liste) | $O(|A|)$ |
# | Degré du nœud $u$ | $O(n)$ | $O(n)$ | $O(|A|)$ |
# | Liste des voisins sortant du nœud $u$ | $O(n)$ | $O(n)$ | $O(|A|)$ |
# | Degré sortant du nœud $u$ | $O(n)$ | $O(n)$ | $O(|A|)$ |
# | Liste des voisins entrant du nœud $u$ | $O(n)$ | $O(n)$ | $O(|A|)$ |
# | Degré entrant du nœud $u$ | $O(n)$ | $O(n)$ | $O(|A|)$ |
# 

# In[62]:


try:
    from tqdm import tqdm_notebook
except ImportError:
    def tqdm_notebook(iterator, *args, **kwargs):
        return iterator


# In[ ]:


graph.is_vertex(vertex)
graph.add_vertex(m)
graph.add_edge(i, j)
graph.remove_edge(i, j)
graph.pred(i)
graph.is_pred(u, v)
graph.succ(i)
graph.is_succ(u, v)
graph.neighbors(i)
graph.is_neighbor(u, v)


# In[64]:


def random_vertex(n):
    return random.randint(0, n+1)

def random_edge(n):
    return (random_vertex(n), random_vertex(n))


# In[69]:


for n in tqdm_notebook([100, 1000], desc="n"):  #, 1000, 10_000, 100_000]):
    print(f"\n\n For graphs with {n} vertexes:")
    for probability in tqdm_notebook([1.0/n, 1.0/np.sqrt(n), 0.9], desc="proba"):
        # p = 1/n => |A| ~= |S|
        # p = 1/sqrt(n) => |A| ~= |S|^(3/2)
        # p = 0.9 => |A| ~= 0.9 |S|^2
        print(f"\n  and link probability of {probability}:")
        for GraphClass in tqdm_notebook([AdjMatrixGraph, AdjListsGraph, EdgesListGraph], desc="class"):
            print(f"\n    for class {GraphClass}...")
            graph = randomGraph(GraphClass, n=n, probability=probability)
            print("Time to create a new graph:")
            get_ipython().run_line_magic('timeit', 'randomGraph(GraphClass, n=n, probability=probability)')
            print("Time to test presence of a vertex:")
            get_ipython().run_line_magic('timeit', 'graph.is_vertex(random_vertex(n))')
            print("Time to add the next vertex n + 2:")
            get_ipython().run_line_magic('timeit', 'graph.add_vertex(n + 2)')
            print("Time to compute pred:")
            get_ipython().run_line_magic('timeit', 'graph.pred(random_vertex(n))')
            print("Time to test pred:")
            get_ipython().run_line_magic('timeit', 'graph.is_pred(*random_edge(n))')
            print("Time to compute succ:")
            get_ipython().run_line_magic('timeit', 'graph.succ(random_vertex(n))')
            print("Time to test succ:")
            get_ipython().run_line_magic('timeit', 'graph.is_succ(*random_edge(n))')
            print("Time to compute neighbors:")
            get_ipython().run_line_magic('timeit', 'graph.neighbors(random_vertex(n))')
            print("Time to test neighbors:")
            get_ipython().run_line_magic('timeit', 'graph.is_neighbor(*random_edge(n))')
            print("Time to add an edge:")
            get_ipython().run_line_magic('timeit', 'graph.add_edge(*random_edge(n))')


# In[ ]:





# ----
# ## Parcours en profondeur

# ----
# ## Application : composantes connexes d'un graphe non orienté

# ----
# ## Conclusion
# 
# C'est bon pour aujourd'hui !
