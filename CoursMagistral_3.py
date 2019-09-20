#!/usr/bin/env python
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#ALGO1-:-Introduction-à-l'algorithmique" data-toc-modified-id="ALGO1-:-Introduction-à-l'algorithmique-1"><span class="toc-item-num">1&nbsp;&nbsp;</span><a href="https://perso.crans.org/besson/teach/info1_algo1_2019/" target="_blank">ALGO1 : Introduction à l'algorithmique</a></a></div><div class="lev1 toc-item"><a href="#Cours-Magistral-3" data-toc-modified-id="Cours-Magistral-3-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Cours Magistral 3</a></div><div class="lev2 toc-item"><a href="#Quelques-algorithmes-&quot;diviser-pour-régner&quot;-classiques" data-toc-modified-id="Quelques-algorithmes-&quot;diviser-pour-régner&quot;-classiques-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Quelques algorithmes "diviser pour régner" classiques</a></div><div class="lev3 toc-item"><a href="#Recherche-dans-un-tableau-trié-en-$\mathcal{O}(\log(n))$" data-toc-modified-id="Recherche-dans-un-tableau-trié-en-$\mathcal{O}(\log(n))$-211"><span class="toc-item-num">2.1.1&nbsp;&nbsp;</span>Recherche dans un tableau trié en <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-607-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mrow class=&quot;MJX-TeXAtom-ORD&quot;><mi class=&quot;MJX-tex-caligraphic&quot; mathvariant=&quot;script&quot;>O</mi></mrow><mo stretchy=&quot;false&quot;>(</mo><mi>log</mi><mo>&amp;#x2061;</mo><mo stretchy=&quot;false&quot;>(</mo><mi>n</mi><mo stretchy=&quot;false&quot;>)</mo><mo stretchy=&quot;false&quot;>)</mo></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-4424" style="width: 4.307em; display: inline-block;"><span style="display: inline-block; position: relative; width: 3.854em; height: 0px; font-size: 111%;"><span style="position: absolute; clip: rect(1.769em, 1003.81em, 2.971em, -1000em); top: -2.603em; left: 0em;"><span class="mrow" id="MathJax-Span-4425"><span class="texatom" id="MathJax-Span-4426"><span class="mrow" id="MathJax-Span-4427"><span class="mi" id="MathJax-Span-4428" style="font-family: STIXMathJax_Variants; font-style: italic;"></span></span></span><span class="mo" id="MathJax-Span-4429" style="font-family: STIXMathJax_Main;">(</span><span class="mi" id="MathJax-Span-4430" style="font-family: STIXMathJax_Main;">log</span><span class="mo" id="MathJax-Span-4431"></span><span class="mo" id="MathJax-Span-4432" style="font-family: STIXMathJax_Main;">(</span><span class="mi" id="MathJax-Span-4433" style="font-family: STIXMathJax_Normal; font-style: italic;">𝑛</span><span class="mo" id="MathJax-Span-4434" style="font-family: STIXMathJax_Main;">)</span><span class="mo" id="MathJax-Span-4435" style="font-family: STIXMathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.603em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.298em; border-left: 0px solid; width: 0px; height: 1.111em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mrow class="MJX-TeXAtom-ORD"><mi class="MJX-tex-caligraphic" mathvariant="script">O</mi></mrow><mo stretchy="false">(</mo><mi>log</mi><mo>⁡</mo><mo stretchy="false">(</mo><mi>n</mi><mo stretchy="false">)</mo><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-607">\mathcal{O}(\log(n))</script></a></div><div class="lev3 toc-item"><a href="#Recherche-dans-une-liste-triée-en-$\mathcal{O}(n)$" data-toc-modified-id="Recherche-dans-une-liste-triée-en-$\mathcal{O}(n)$-212"><span class="toc-item-num">2.1.2&nbsp;&nbsp;</span>Recherche dans une liste triée en <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-515-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mrow class=&quot;MJX-TeXAtom-ORD&quot;><mi class=&quot;MJX-tex-caligraphic&quot; mathvariant=&quot;script&quot;>O</mi></mrow><mo stretchy=&quot;false&quot;>(</mo><mi>n</mi><mo stretchy=&quot;false&quot;>)</mo></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3649" style="width: 2.105em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.902em; height: 0px; font-size: 111%;"><span style="position: absolute; clip: rect(1.776em, 1001.85em, 2.93em, -1000em); top: -2.603em; left: 0em;"><span class="mrow" id="MathJax-Span-3650"><span class="texatom" id="MathJax-Span-3651"><span class="mrow" id="MathJax-Span-3652"><span class="mi" id="MathJax-Span-3653" style="font-family: STIXMathJax_Variants; font-style: italic;"></span></span></span><span class="mo" id="MathJax-Span-3654" style="font-family: STIXMathJax_Main;">(</span><span class="mi" id="MathJax-Span-3655" style="font-family: STIXMathJax_Normal; font-style: italic;">𝑛</span><span class="mo" id="MathJax-Span-3656" style="font-family: STIXMathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.603em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.252em; border-left: 0px solid; width: 0px; height: 1.058em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mrow class="MJX-TeXAtom-ORD"><mi class="MJX-tex-caligraphic" mathvariant="script">O</mi></mrow><mo stretchy="false">(</mo><mi>n</mi><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-515">\mathcal{O}(n)</script></a></div><div class="lev3 toc-item"><a href="#Tri-fusion-(merge-sort)" data-toc-modified-id="Tri-fusion-(merge-sort)-213"><span class="toc-item-num">2.1.3&nbsp;&nbsp;</span>Tri fusion (<em>merge sort</em>)</a></div><div class="lev3 toc-item"><a href="#Enveloppe-convexe-de-points-en-2D-(quickhull)" data-toc-modified-id="Enveloppe-convexe-de-points-en-2D-(quickhull)-214"><span class="toc-item-num">2.1.4&nbsp;&nbsp;</span>Enveloppe convexe de points en 2D (<em>quickhull</em>)</a></div><div class="lev2 toc-item"><a href="#Algorithme-de-Gauss-Karatsuba" data-toc-modified-id="Algorithme-de-Gauss-Karatsuba-22"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Algorithme de Gauss-Karatsuba</a></div><div class="lev2 toc-item"><a href="#Algorithme-de-Strassen" data-toc-modified-id="Algorithme-de-Strassen-23"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Algorithme de Strassen</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-24"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Conclusion</a></div>

# # [ALGO1 : Introduction à l'algorithmique](https://perso.crans.org/besson/teach/info1_algo1_2019/)
# 
# - [Page du cours](https://perso.crans.org/besson/teach/info1_algo1_2019/) : https://perso.crans.org/besson/teach/info1_algo1_2019/
# - Magistère d'Informatique de Rennes - ENS Rennes - Année 2019/2020
# - Intervenants :
#   + Cours : [Lilian Besson](https://perso.crans.org/besson/)
#   + Travaux dirigés : [Raphaël Truffet](http://perso.eleves.ens-rennes.fr/people/Raphael.Truffet/)
# - Références :
#   + [Open Data Structures](http://opendatastructures.org/ods-python.pdf)

# # Cours Magistral 3
# 
# - Ce cours traite du paradigme "Diviser pour Régner",
# - Un important résultat théorique est donné (et prouvé) :
# 
# <img width="75%" src="figures/CM3_Master-Theorem.png">
# 
# - Ce notebook commence par donner quelques algorithmes "Diviser pour Régner" assez classiques, et permettent d'illustrer les deux premiers cas du "master theorem" (recherche dans une liste triée ou un tableau trié, tri fusion,
# 
# - Ce théorème ne suffit pas à couvrir tous les différents algorithmes "Diviser pour Régner", avec comme contre exemple l'algorithme de tri rapide,
# 
# - Puis on implémente les deux algorithmes présentés dans le cours, la multiplication de grands entiers par l'algorithme de Gauss-Karatsuba, et la multiplication de grandes matrices par l'algorithme de Strassen (Straßen).

# ----
# ## Quelques algorithmes "diviser pour régner" classiques

# ### Recherche dans un tableau trié en $\mathcal{O}(\log(n))$
# 
# Si un tableau `T = [a1, ..., an]` est trié, et qu'on donne une valeur `x`, on cherche un indice `i` tel que `T[i] = ai = x`, s'il existe (sans spécification s'il n'est pas unique), et une erreur si `x` n'est pas présent dans le tableau.
# 
# En utilisant des indices `left` et `right`, qu'on fait augmenter ou diminuer, on évite de faire des recopies du tableau.

# La complexité de cet algorithme est en $\mathcal{O}(\log(n))$.
# 
# **Avec le _master theorem_**, on a $a=1, b=2, k=0$ : on divise les entrées en $a=2$ entrées de tailles $\leq b=2$ plus petites, sur lesquels on applique un traitement **constant** ($\mathcal{O}(n^{k=0})$ avant l'appel récursif (**aucune recopie, juste des changements d'indices !**).

# In[206]:


def dichotomy_in_array(array, value, left=0, right=None):
    if depth > len(array):    raise KeyError
    if right is None:
        right = len(array) - 1
    n = right - left + 1
    if n == 0:                raise KeyError
    elif n == 1:
        if array[left] == value:
            return left
        else:                 raise KeyError
    index_of_middle = left + (n // 2)
    middle_of_list = array[index_of_middle]
    if value < middle_of_list:  # search on left
        return dichotomy_in_array(array, value, left=left, right=index_of_middle - 1, debug=debug, depth=depth+1)
    elif value > middle_of_list:  # search on right
        return dichotomy_in_array(array, value, left=index_of_middle + 1, right=right, debug=debug, depth=depth+1)
    else:
        return index_of_middle


# Et avec juste un peu d'affichage pour (un rappel ou pour) comprendre le fonctionnement :

# In[206]:


def dichotomy_in_array(array, value, left=0, right=None, debug=False, depth=0):
    if depth > len(array):
        raise KeyError
    if right is None:
        right = len(array) - 1
    n = right - left + 1
    if debug: print(f"    {'  '*(depth+1)}Searching for {value} in sequence of size {n} = {array[left:right+1]}")
    if n == 0:
        raise KeyError
    elif n == 1:
        if array[left] == value:
            return left
        else:
            raise KeyError
    index_of_middle = left + (n // 2)
    middle_of_list = array[index_of_middle]
    #if debug: print(f"    {'  '*(depth+1)}{value} >/</=? {middle_of_list}")
    if value < middle_of_list:  # search on left
        if debug: print(f"    {'  '*(depth+1)}-> going left...")
        return dichotomy_in_array(array, value, left=left, right=index_of_middle - 1, debug=debug, depth=depth+1)
    elif value > middle_of_list:  # search on right
        if debug: print(f"    {'  '*(depth+1)}-> going right...")
        return dichotomy_in_array(array, value, left=index_of_middle + 1, right=right, debug=debug, depth=depth+1)
    elif value == middle_of_list:
        if debug: print(f"    {'  '*(depth+1)}-> found at index {index_of_middle} !")
        return index_of_middle
    else:
        raise KeyError


# Faisons quelques essais :

# In[85]:


n = 16
example_of_array = list(range(n))


# In[86]:


for value in example_of_array:
    print(f"\n    Looking for value {value} in {example_of_array} :")
    dichotomy_in_array(example_of_array, value, debug=True)


# Et maintenant des essais sur des entrées de tailles croissantes :

# In[119]:


import random

def random_sorted_sequence(n, minint=0, maxint=1000):
    sequence = [random.randint(minint, maxint) for _ in range(n)]
    return sorted(sequence)


# In[151]:


def test_dichotomy_in_array(n, debug=False, array=None):
    if array is None:
        array = random_sorted_sequence(n)
    value = random.choice(array)
    return dichotomy_in_array(array, value, debug=debug)


# In[152]:


test_dichotomy_in_array(16, debug=True)


# In[153]:


import sys
sys.setrecursionlimit(10000)


# In[154]:


T = random_sorted_sequence(100)
get_ipython().run_line_magic('timeit', 'test_dichotomy_in_array(100, array=T)')


# In[155]:


T = random_sorted_sequence(1000)
get_ipython().run_line_magic('timeit', 'test_dichotomy_in_array(1000, array=T)')


# In[156]:


T = random_sorted_sequence(10000)
get_ipython().run_line_magic('timeit', 'test_dichotomy_in_array(10000, array=T)')


# In[157]:


T = random_sorted_sequence(100000)
get_ipython().run_line_magic('timeit', 'test_dichotomy_in_array(100000, array=T)')


# In[158]:


T = random_sorted_sequence(1000000)
get_ipython().run_line_magic('timeit', 'test_dichotomy_in_array(1000000, array=T)')


# La complexité semble bien logarithmique en $n$ (ie., $\mathcal{O}(\log(n))$) !

# ### Recherche dans une liste triée en $\mathcal{O}(n)$
# 
# C'est comme la recherche dans un tableau trié, sauf qu'on recopie la liste de gauche ou de droite lors des appels récursifs.

# La complexité de cet algorithme est en $\mathcal{O}(n)$.
# 
# **Avec le _master theorem_**, on a $a=1, b=2, k=1$ : on divise les entrées en $a=2$ entrées de tailles $\leq b=2$ plus petites, sur lesquels on applique un traitement linéaire ($\mathcal{O}(n^{k=1})$ avant l'appel récursif (**à cause des recopies !**).

# In[207]:


def dichotomy_in_list(sequence, value):
    n = len(sequence)
    if n == 0:            raise KeyError
    index_of_middle = n // 2
    middle_of_list = sequence[index_of_middle]
    if value < middle_of_list:  # search on left
        # creating this list takes O(n/2) time
        left_list = sequence[:index_of_middle]
        return dichotomy_in_list(left_list, value, debug=debug, depth=depth+1)
    elif value > middle_of_list:  # search on right
        # creating this list takes O(n/2) time
        right_list = sequence[index_of_middle:]
        return index_of_middle + dichotomy_in_list(right_list, value, debug=debug, depth=depth+1)
    else:
        return index_of_middle


# Et avec juste un peu d'affichage pour (un rappel ou pour) comprendre le fonctionnement :

# In[131]:


def dichotomy_in_list(sequence, value, debug=False, depth=0):
    n = len(sequence)
    if debug:
        print(f"    {'  '*(depth+1)}Sequence of size {n} = {sequence}")
    if n == 0:
        raise KeyError
    index_of_middle = n // 2
    middle_of_list = sequence[index_of_middle]
    if value < middle_of_list:  # search on left
        left_list = sequence[:index_of_middle]
        if debug: print(f"    {'  '*(depth+1)}-> going left, in {left_list} of size {len(left_list)}...")
        return dichotomy_in_list(left_list, value, debug=debug, depth=depth+1)
    elif value > middle_of_list:  # search on right
        right_list = sequence[index_of_middle:]
        if debug: print(f"    {'  '*(depth+1)}-> going right, in {right_list} of size {len(right_list)}...")
        return index_of_middle + dichotomy_in_list(right_list, value, debug=debug, depth=depth+1)
    elif value == middle_of_list:
        if debug: print(f"    {'  '*(depth+1)}-> found at index {index_of_middle} !")
        return index_of_middle
    else:
        raise KeyError


# Faisons quelques essais :

# In[132]:


n = 16
example_of_list = list(range(n))


# In[133]:


for value in example_of_list:
    print(f"\n    Looking for value {value} in {example_of_list} :")
    dichotomy_in_list(example_of_list, value, debug=True)


# Et maintenant des essais sur des entrées de tailles croissantes :

# In[134]:


import random

def random_sorted_sequence(n, minint=0, maxint=1000):
    sequence = [random.randint(minint, maxint) for _ in range(n)]
    return sorted(sequence)


# In[161]:


def test_dichotomy_in_list(n, debug=False, sequence=None):
    if sequence is None:
        sequence = random_sorted_sequence(n)
    value = random.choice(sequence)
    return dichotomy_in_list(sequence, value, debug=debug)


# In[162]:


test_dichotomy_in_array(16, debug=True)


# In[163]:


import sys
sys.setrecursionlimit(10000)


# In[164]:


L = random_sorted_sequence(100)
get_ipython().run_line_magic('timeit', 'test_dichotomy_in_list(100, sequence=L)')


# In[165]:


L = random_sorted_sequence(1000)
get_ipython().run_line_magic('timeit', 'test_dichotomy_in_list(1000, sequence=L)')


# In[169]:


L = random_sorted_sequence(10000)
get_ipython().run_line_magic('timeit', 'test_dichotomy_in_list(10000, sequence=L)')


# In[168]:


L = random_sorted_sequence(100000)
get_ipython().run_line_magic('timeit', 'test_dichotomy_in_list(100000, sequence=L)')


# In[170]:


L = random_sorted_sequence(1000_000)
get_ipython().run_line_magic('timeit', 'test_dichotomy_in_list(1000_000, sequence=L)')


# In[171]:


L = random_sorted_sequence(10_000_000)
get_ipython().run_line_magic('timeit', 'test_dichotomy_in_list(10_000_000, sequence=L)')


# La complexité semble bien linéaire en $n$ (ie., $\mathcal{O}(n)$) !

# ### Tri fusion (*merge sort*)
# 
# - Problème :
#   + entrée = tableau `T = [a1, ..., an]` de `n` valeurs
#   + sortie = tableau trié par ordre croissant
# 
# - Algorithme :
#   + on divise en deux le tableau, `gauche = [a1, ..., a_n/2]` et `droite = [a_n/2+1, ..., an]`,
#   + on trie récursivement les deux sous tableaux,
#   + on fusionne (*merge*) les deux sous tableaux en un.
# 
# La fusion est simple à réaliser : on commence tout à gauche des deux tableaux, on avance dans le tableau de gauche ou le tableau de droite, séquentiellement, jusqu'à avoir épuiser leurs valeurs, en prenant la valeur de gauche tant qu'elle est plus petite que celle de droite.

# La complexité de cet algorithme est en $\mathcal{O}(n \log(n))$.
# 
# **Avec le _master theorem_**, on a $a=2, b=2, k=1$ : on divise les entrées en $a=2$ entrées de tailles $\leq b=2$ plus petites, sur lesquels on applique un traitement linéaire ($\mathcal{O}(n^{k=1})$ avant et après l'appel récursif.

# In[197]:


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0  # growing pointers
    while left_idx < len(left) and right_idx < len(right):
        # this loop terminates because left_idx + right_idx is strictly increasing
        # and bounded by len(left) + len(right)
        # change the direction of this comparison to change the direction of the sort
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    # we still have values to take on the left
    if left_idx < len(left):
        result.extend(left[left_idx:])
    # we still have values to take on the right
    if right_idx < len(right):
        result.extend(right[right_idx:])
    return result


# In[198]:


def merge_sort(m):
    if len(m) <= 1:
        return m
 
    middle = len(m) // 2
    # separating the array in two pieces is easy with Python
    # but keep in mind, this takes a linear time to copy the arrays!
    left = m[:middle]
    right = m[middle:]
 
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return list(merge(sorted_left, sorted_right))


# Quelques tests :

# In[199]:


L = random_sorted_sequence(100)
get_ipython().run_line_magic('timeit', 'merge_sort(shuffle(L))')


# In[200]:


L = random_sorted_sequence(1000)
get_ipython().run_line_magic('timeit', 'merge_sort(shuffle(L))')


# In[201]:


L = random_sorted_sequence(10_000)
get_ipython().run_line_magic('timeit', 'merge_sort(shuffle(L))')


# In[202]:


L = random_sorted_sequence(100_000)
get_ipython().run_line_magic('timeit', 'merge_sort(shuffle(L))')


# In[203]:


L = random_sorted_sequence(1000_000)
get_ipython().run_line_magic('timeit', 'merge_sort(shuffle(L))')


# On pourrait vérifier que la complexité est bien en $\mathcal{O}(n \log(n))$.

# ### Enveloppe convexe de points en 2D (*quickhull*)
# 
# - Problème :
#   + entrée = tableau `T = [xy1, ..., xyn]` de `n` points dans le plan (`xy = (x, y)`)
#   + sortie = tableau `hull = [xy_i1, ..., xy_ip]` des `p` points constituant l'enveloppe convexe des `n` points d'entrée
# 
# - Algorithme :
#   + on identifie le point le plus en bas à gauche $P_{bg}$, le point le plus en haut à droite $P_{hd}$,
#   + la diagonale $D$ est le segment orienté qui va de $P_{bg}$ à $P_{hd}$,
#   + on sépare l'ensemble en deux, les points à gauche de $D$ (coin bas droite), ceux à droite de $D$,
#   + on calcule les deux enveloppes convexes $E_g$ et $E_d$ des deux ensembles de points (récursivement),
#   + on fusionne les deux enveloppes convexes $E_g$ et $E_d$ en les ordonnant comme il faut (et en enlevant l'arête $P_{hd} \to P_{pg}$ qui est présente dans $E_g$ et $P_{pg} \to P_{hd}$ présente dans $E_d$.
# 
# La fusion est naïve simple à réaliser.
# Le test pour savoir si un point est à gauche, à droite, ou sur $D$, se fait en temps $O(1)$ avec un calcul de produit scalaire.

# In[205]:


def quickhull(points):
    raise NotImplementedError


# La complexité de cet algorithme est en $\mathcal{O}(n \log(n))$.
# 
# **Avec le _master theorem_**, on a $a=2, b=2, k=1$ : on divise les entrées en $a=2$ entrées de tailles $\leq b=2$ plus petites, sur lesquels on applique un traitement linéaire ($\mathcal{O}(n^{k=1})$ avant et après l'appel récursif.
# (*En supposant les points uniformément répartis dans le plan*.)
# 
# On pourrait l'implémenter, et vérifier la complexité sur des entrées aléatoires (ie. les points sont tirés uniformément dans une boîte carrée $(x_i,y_i) \sim [x_\min,x_\max] \times [y_\min,y_\max]$).

# ----
# ## Algorithme de Gauss-Karatsuba

# In[ ]:





# In[ ]:





# ----
# ## Algorithme de Strassen
# 
# 
# > Part of this code is coming from [this blog post](https://martin-thoma.com/strassen-algorithm-in-python-java-cpp/).

# La complexité de cet algorithme est en $\mathcal{O}(n^{\log_2(7)})$, asymptotiquement meilleur que $\mathcal{O}(n^3)$ la méthode naïve.
# 
# **Avec le _master theorem_**, on a $a=7, b=2, k=2$ : on divise les entrées en $a=7$ entrées de tailles $\leq b=2$ plus petites [1], sur lesquels on applique un traitement quadratique (toutes les additions $\mathcal{O}(n^{k=2})$ avant et après l'appel récursif.
# 
# Donc $a = 7 > b^k = 4$ ce qui donne $T(n) = \mathcal{O}(n^{\log_b(a)})$.
# 
# > [1] : c'est $n$ qui est divisé par deux, bien que $n^2$ soit divisé par $4$ et que l'on puisse considérer que la taille d'une matrice $(n,m)$ est $n \times m$.

# In[208]:


import numpy as np


# In[221]:


def ikjMatrixProduct(A, B):
    n = len(A)
    C = np.zeros((n, n), dtype=type(A[0,0]))
    for i in range(n):
        for k in range(n):
            for j in range(n):
                C[i,j] += A[i,k] * B[k,j]
    return C


# In[222]:


def add(A, B):
    n = len(A)
    C = np.zeros((n, n), dtype=type(A[0,0]))
    for i in range(n):
        for j in range(n):
            C[i,j] = A[i,j] + B[i,j]
    return C


# In[223]:


def subtract(A, B):
    n = len(A)
    C = np.zeros((n, n), dtype=type(A[0,0]))
    for i in range(n):
        for j in range(n):
            C[i,j] = A[i,j] - B[i,j]
    return C


# In[224]:


LEAF_SIZE = 64


# In[255]:


def strassenR(A, B, leaf_size=LEAF_SIZE):
    n = len(A)

    if n <= leaf_size:
        return ikjMatrixProduct(A, B)
    else:
        # initializing the new sub-matrices
        newSize = n//2
        a11 = np.zeros((newSize, newSize), dtype=type(A[0,0]))
        a12 = np.zeros((newSize, newSize), dtype=type(A[0,0]))
        a21 = np.zeros((newSize, newSize), dtype=type(A[0,0]))
        a22 = np.zeros((newSize, newSize), dtype=type(A[0,0]))
        b11 = np.zeros((newSize, newSize), dtype=type(A[0,0]))
        b12 = np.zeros((newSize, newSize), dtype=type(A[0,0]))
        b21 = np.zeros((newSize, newSize), dtype=type(A[0,0]))
        b22 = np.zeros((newSize, newSize), dtype=type(A[0,0]))

        aResult = np.zeros((newSize, newSize), dtype=type(A[0,0]))
        bResult = np.zeros((newSize, newSize), dtype=type(A[0,0]))

        # dividing the matrices in 4 sub-matrices:
        for i in range(newSize):
            for j in range(newSize):
                a11[i,j] = A[i, j]            # top left
                a12[i,j] = A[i, j + newSize]    # top right
                a21[i,j] = A[i + newSize, j]    # bottom left
                a22[i,j] = A[i + newSize, j + newSize] # bottom right
                b11[i,j] = B[i, j]            # top left
                b12[i,j] = B[i, j + newSize]    # top right
                b21[i,j] = B[i + newSize, j]    # bottom left
                b22[i,j] = B[i + newSize, j + newSize] # bottom right

        # Calculating p1 to p7:
        aResult = add(a11, a22)
        bResult = add(b11, b22)
        p1 = strassenR(aResult, bResult) # p1 = (a11+a22) * (b11+b22)

        aResult = add(a21, a22)      # a21 + a22
        p2 = strassenR(aResult, b11)  # p2 = (a21+a22) * (b11)

        bResult = subtract(b12, b22) # b12 - b22
        p3 = strassenR(a11, bResult)  # p3 = (a11) * (b12 - b22)

        bResult = subtract(b21, b11) # b21 - b11
        p4 =strassenR(a22, bResult)   # p4 = (a22) * (b21 - b11)

        aResult = add(a11, a12)      # a11 + a12
        p5 = strassenR(aResult, b22)  # p5 = (a11+a12) * (b22)   

        aResult = subtract(a21, a11) # a21 - a11
        bResult = add(b11, b12)      # b11 + b12
        p6 = strassenR(aResult, bResult) # p6 = (a21-a11) * (b11+b12)

        aResult = subtract(a12, a22) # a12 - a22
        bResult = add(b21, b22)      # b21 + b22
        p7 = strassenR(aResult, bResult) # p7 = (a12-a22) * (b21+b22)

        # calculating c21, c21, c11 e c22:
        c12 = add(p3, p5) # c12 = p3 + p5
        c21 = add(p2, p4)  # c21 = p2 + p4

        aResult = add(p1, p4) # p1 + p4
        bResult = add(aResult, p7) # p1 + p4 + p7
        c11 = subtract(bResult, p5) # c11 = p1 + p4 - p5 + p7

        aResult = add(p1, p3) # p1 + p3
        bResult = add(aResult, p6) # p1 + p3 + p6
        c22 = subtract(bResult, p2) # c22 = p1 + p3 - p2 + p6

        # Grouping the results obtained in a single matrix:
        C = np.zeros((n, n), dtype=type(A[0,0]))
        for i in range(newSize):
            for j in range(newSize):
                C[i,j] = c11[i,j]
                C[i,j + newSize] = c12[i,j]
                C[i + newSize,j] = c21[i,j]
                C[i + newSize,j + newSize] = c22[i,j]
        return C


# In[256]:


def strassen(A, B, leaf_size=LEAF_SIZE):
    assert isinstance(A, np.ndarray) and isinstance(B, np.ndarray)
    assert len(A) == len(A[0]) == len(B) == len(B[0])

    # Make the matrices bigger so that you can apply the strassen
    # algorithm recursively without having to deal with odd
    # matrix sizes
    nextPowerOfTwo = lambda n: 2**int(ceil(log(n,2)))
    n = len(A)
    m = nextPowerOfTwo(n)
    APrep = np.zeros((m, m), dtype=type(A[0,0]))
    BPrep = np.zeros((m, m), dtype=type(A[0,0]))
    for i in range(n):
        for j in range(n):
            APrep[i,j] = A[i,j]
            BPrep[i,j] = B[i,j]
    CPrep = strassenR(APrep, BPrep, leaf_size=leaf_size)
    C = np.zeros((n, n), dtype=type(A[0,0]))
    for i in range(n):
        for j in range(n):
            C[i,j] = CPrep[i,j]
    return C


# Un exemple de petite taille ($n=4$) :

# In[257]:


NotImplemented


# Générer des exemples de tailles grandissantes :

# In[242]:


import random


# In[243]:


def random_matrix(n, minint=0, maxint=1000):
    A = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            A[i, j] = random.randint(minint, maxint)
    return A


# In[244]:


A = random_matrix(4)
A


# In[245]:


B = random_matrix(4)
B


# In[246]:


A @ B


# In[247]:


ikjMatrixProduct(A, B)


# In[249]:


strassenR(A, B, leaf_size=1)


# In[250]:


strassenR(A, B, leaf_size=2)


# Pour des tests de taille $n$ croissantes :

# In[258]:


def test_ijk(n):
    A = random_matrix(n)
    B = random_matrix(n)
    C = ikjMatrixProduct(A, B)
    return C

def test_strassen(n):
    A = random_matrix(n)
    B = random_matrix(n)
    C = strassen(A, B)
    return C


# In[ ]:


for n in [2**5, 2**6, 2**7, 2**8]:
    print(f"\nFor n = {n} : first is the ikj naive algorithm, then Strassen :")
    A = random_matrix(n)
    B = random_matrix(n)
    get_ipython().run_line_magic('timeit', 'ikjMatrixProduct(A, B)')
    get_ipython().run_line_magic('timeit', 'strassen(A, B)')


# ## Conclusion
# 
# C'est bon pour aujourd'hui !
