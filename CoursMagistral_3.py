#!/usr/bin/env python
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#ALGO1-:-Introduction-à-l'algorithmique" data-toc-modified-id="ALGO1-:-Introduction-à-l'algorithmique-1"><span class="toc-item-num">1&nbsp;&nbsp;</span><a href="https://perso.crans.org/besson/teach/info1_algo1_2019/" target="_blank">ALGO1 : Introduction à l'algorithmique</a></a></div><div class="lev1 toc-item"><a href="#Cours-Magistral-3" data-toc-modified-id="Cours-Magistral-3-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Cours Magistral 3</a></div><div class="lev2 toc-item"><a href="#Quelques-algorithmes-&quot;diviser-pour-régner&quot;-classiques" data-toc-modified-id="Quelques-algorithmes-&quot;diviser-pour-régner&quot;-classiques-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Quelques algorithmes "diviser pour régner" classiques</a></div><div class="lev3 toc-item"><a href="#Recherche-dans-un-tableau-trié-en-$\mathcal{O}(\log(n))$" data-toc-modified-id="Recherche-dans-un-tableau-trié-en-$\mathcal{O}(\log(n))$-211"><span class="toc-item-num">2.1.1&nbsp;&nbsp;</span>Recherche dans un tableau trié en <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-607-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mrow class=&quot;MJX-TeXAtom-ORD&quot;><mi class=&quot;MJX-tex-caligraphic&quot; mathvariant=&quot;script&quot;>O</mi></mrow><mo stretchy=&quot;false&quot;>(</mo><mi>log</mi><mo>&amp;#x2061;</mo><mo stretchy=&quot;false&quot;>(</mo><mi>n</mi><mo stretchy=&quot;false&quot;>)</mo><mo stretchy=&quot;false&quot;>)</mo></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-4424" style="width: 4.307em; display: inline-block;"><span style="display: inline-block; position: relative; width: 3.854em; height: 0px; font-size: 111%;"><span style="position: absolute; clip: rect(1.769em, 1003.81em, 2.971em, -1000em); top: -2.603em; left: 0em;"><span class="mrow" id="MathJax-Span-4425"><span class="texatom" id="MathJax-Span-4426"><span class="mrow" id="MathJax-Span-4427"><span class="mi" id="MathJax-Span-4428" style="font-family: STIXMathJax_Variants; font-style: italic;"></span></span></span><span class="mo" id="MathJax-Span-4429" style="font-family: STIXMathJax_Main;">(</span><span class="mi" id="MathJax-Span-4430" style="font-family: STIXMathJax_Main;">log</span><span class="mo" id="MathJax-Span-4431"></span><span class="mo" id="MathJax-Span-4432" style="font-family: STIXMathJax_Main;">(</span><span class="mi" id="MathJax-Span-4433" style="font-family: STIXMathJax_Normal; font-style: italic;">𝑛</span><span class="mo" id="MathJax-Span-4434" style="font-family: STIXMathJax_Main;">)</span><span class="mo" id="MathJax-Span-4435" style="font-family: STIXMathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.603em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.298em; border-left: 0px solid; width: 0px; height: 1.111em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mrow class="MJX-TeXAtom-ORD"><mi class="MJX-tex-caligraphic" mathvariant="script">O</mi></mrow><mo stretchy="false">(</mo><mi>log</mi><mo>⁡</mo><mo stretchy="false">(</mo><mi>n</mi><mo stretchy="false">)</mo><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-607">\mathcal{O}(\log(n))</script></a></div><div class="lev3 toc-item"><a href="#Recherche-dans-une-liste-triée-en-$\mathcal{O}(n)$" data-toc-modified-id="Recherche-dans-une-liste-triée-en-$\mathcal{O}(n)$-212"><span class="toc-item-num">2.1.2&nbsp;&nbsp;</span>Recherche dans une liste triée en <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-515-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mrow class=&quot;MJX-TeXAtom-ORD&quot;><mi class=&quot;MJX-tex-caligraphic&quot; mathvariant=&quot;script&quot;>O</mi></mrow><mo stretchy=&quot;false&quot;>(</mo><mi>n</mi><mo stretchy=&quot;false&quot;>)</mo></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3649" style="width: 2.105em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.902em; height: 0px; font-size: 111%;"><span style="position: absolute; clip: rect(1.776em, 1001.85em, 2.93em, -1000em); top: -2.603em; left: 0em;"><span class="mrow" id="MathJax-Span-3650"><span class="texatom" id="MathJax-Span-3651"><span class="mrow" id="MathJax-Span-3652"><span class="mi" id="MathJax-Span-3653" style="font-family: STIXMathJax_Variants; font-style: italic;"></span></span></span><span class="mo" id="MathJax-Span-3654" style="font-family: STIXMathJax_Main;">(</span><span class="mi" id="MathJax-Span-3655" style="font-family: STIXMathJax_Normal; font-style: italic;">𝑛</span><span class="mo" id="MathJax-Span-3656" style="font-family: STIXMathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.603em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.252em; border-left: 0px solid; width: 0px; height: 1.058em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mrow class="MJX-TeXAtom-ORD"><mi class="MJX-tex-caligraphic" mathvariant="script">O</mi></mrow><mo stretchy="false">(</mo><mi>n</mi><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-515">\mathcal{O}(n)</script></a></div><div class="lev3 toc-item"><a href="#Tri-fusion-(merge-sort)" data-toc-modified-id="Tri-fusion-(merge-sort)-213"><span class="toc-item-num">2.1.3&nbsp;&nbsp;</span>Tri fusion (<em>merge sort</em>)</a></div><div class="lev3 toc-item"><a href="#Enveloppe-convexe-de-points-en-2D-(quickhull)" data-toc-modified-id="Enveloppe-convexe-de-points-en-2D-(quickhull)-214"><span class="toc-item-num">2.1.4&nbsp;&nbsp;</span>Enveloppe convexe de points en 2D (<em>quickhull</em>)</a></div><div class="lev4 toc-item"><a href="#Un-exemple" data-toc-modified-id="Un-exemple-2141"><span class="toc-item-num">2.1.4.1&nbsp;&nbsp;</span>Un exemple</a></div><div class="lev4 toc-item"><a href="#Exemples-aléatoires-de-taille-contrôlée" data-toc-modified-id="Exemples-aléatoires-de-taille-contrôlée-2142"><span class="toc-item-num">2.1.4.2&nbsp;&nbsp;</span>Exemples aléatoires de taille contrôlée</a></div><div class="lev4 toc-item"><a href="#Complexité-temporelle-de-ce-calcul-d'enveloppe-convexe" data-toc-modified-id="Complexité-temporelle-de-ce-calcul-d'enveloppe-convexe-2143"><span class="toc-item-num">2.1.4.3&nbsp;&nbsp;</span>Complexité temporelle de ce calcul d'enveloppe convexe</a></div><div class="lev2 toc-item"><a href="#Algorithme-de-Gauss-Karatsuba" data-toc-modified-id="Algorithme-de-Gauss-Karatsuba-22"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Algorithme de Gauss-Karatsuba</a></div><div class="lev2 toc-item"><a href="#Algorithme-de-Strassen" data-toc-modified-id="Algorithme-de-Strassen-23"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Algorithme de Strassen</a></div><div class="lev2 toc-item"><a href="#Transformée-de-Fourier-Rapide-(FFT)" data-toc-modified-id="Transformée-de-Fourier-Rapide-(FFT)-24"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Transformée de Fourier Rapide (FFT)</a></div><div class="lev3 toc-item"><a href="#Transformée-de-Fourier-Discrète-(DFT),-implémentation-naïve" data-toc-modified-id="Transformée-de-Fourier-Discrète-(DFT),-implémentation-naïve-241"><span class="toc-item-num">2.4.1&nbsp;&nbsp;</span>Transformée de Fourier Discrète (DFT), implémentation naïve</a></div><div class="lev3 toc-item"><a href="#Implémentation-de-FFT-dans-le-module-numpy" data-toc-modified-id="Implémentation-de-FFT-dans-le-module-numpy-242"><span class="toc-item-num">2.4.2&nbsp;&nbsp;</span>Implémentation de FFT dans le module <code>numpy</code></a></div><div class="lev3 toc-item"><a href="#Implémentation-de-la-DFT-par-multiplication-matricielle" data-toc-modified-id="Implémentation-de-la-DFT-par-multiplication-matricielle-243"><span class="toc-item-num">2.4.3&nbsp;&nbsp;</span>Implémentation de la DFT par multiplication matricielle</a></div><div class="lev3 toc-item"><a href="#Implémentation-manuelle-de-la-FFT-(Cooley-Tucker)" data-toc-modified-id="Implémentation-manuelle-de-la-FFT-(Cooley-Tucker)-244"><span class="toc-item-num">2.4.4&nbsp;&nbsp;</span>Implémentation manuelle de la FFT (Cooley-Tucker)</a></div><div class="lev3 toc-item"><a href="#Tests-avec-des-vecteurs-aléatoires" data-toc-modified-id="Tests-avec-des-vecteurs-aléatoires-245"><span class="toc-item-num">2.4.5&nbsp;&nbsp;</span>Tests avec des vecteurs aléatoires</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-25"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Conclusion</a></div>

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

# In[433]:


import timeit
try:
    from tqdm import tqdm_notebook as tqdm
except ImportError:
    def tqdm(iterator, *args, **kwargs):
        return iterator


# In[357]:


values_n = np.array(np.floor(np.logspace(2, 6.5, num=50)), dtype=int)
values_L = [ random_sorted_sequence(n) for n in values_n ]


# In[358]:


values_times = [
    timeit.timeit(
        stmt=f"merge_sort(shuffle({L}))",
        number= 10000 if n <= 1000 else (1000 if n <= 10000 else (100 if n <= 100000 else 10)),
        globals=globals()
    )
    for (n, L) in tqdm(list(zip(values_n, values_L)))
]


# In[363]:


import numpy as np

import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (8, 5)
mpl.rcParams['figure.dpi'] = 120
    
import matplotlib.pyplot as plt

import seaborn as sns
sns.set(context="notebook", style="whitegrid", palette="hls", font="sans-serif", font_scale=1.1)


# In[364]:


plt.figure()
plt.xlabel("Size of the input array $n$")
plt.ylabel("Time in second")
plt.title("Time complexity of the merge sort algorithm (naive code in Python)")
plt.plot(values_n, values_times, "d-")
plt.show()


# In[368]:


plt.figure()
plt.xlabel("Size of the input array $n$")
plt.ylabel("Time in milli-second, normalized by $n \log(n)$")
plt.title("Time complexity of the merge sort algorithm (naive code in Python)")
normalized_values_times = 1e6 * np.array(values_times) / (values_n * np.log(values_n))
min_time = 1e5
plt.plot(values_n[values_n >= min_time], normalized_values_times[values_n >= min_time], "d-")
plt.show()


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

# In[374]:


exemple_points = [(1, 3) for _ in range(21)]
for i in range(1, 21):
    x, y = exemple_points[i-1]
    exemple_points[i] = (x * 17) % 23, (y * 17) % 19


# In[407]:


plt.figure()
plt.title("Des points en 2D")
Xs = [p[0] for p in exemple_points]
Ys = [p[1] for p in exemple_points]
ax = plt.scatter(Xs, Ys)
plt.show()


# In[376]:


def alpha(a, b, c):
    xa, ya = a
    xb, yb = b
    xc, yc = c
    return (xb - xa) * (yc - ya) - (xc - xa) * (yb - ya)


# In[380]:


p = exemple_points
for i in range(2, 21):
    for j in range(1, i):
        for k in range(0, j):
            if alpha(p[i], p[j], p[k]) == 0:
                print(f"Les trois points #{i}, #{j} et #{k} sont alignés ({p[i]}, {p[j]} et {p[k]}).")


# In[381]:


plt.figure()
plt.title("Des points en 2D, certains sont alignés")
Xs = [p[0] for p in exemple_points]
Ys = [p[1] for p in exemple_points]
plt.scatter(Xs, Ys)
p = exemple_points
for i in range(2, 21):
    for j in range(1, i):
        for k in range(0, j):
            if alpha(p[i], p[j], p[k]) == 0:
                plt.plot([p[i][0], p[j][0], p[k][0]], [p[i][1], p[j][1], p[k][1]], ':')
plt.show()


# In[391]:


def plus_bas(points):
    """ Trouve le point (xa, ya) le plus en bas à gauche, en temps linéaire."""
    n = len(points)
    xa, ya = points[0]
    for j in range(1, n):
        xj, yj = points[j]
        if (ya > yj) or (ya == yj and xa > xj):
            xa, ya = xj, yj
    return xa, ya


# In[392]:


plus_bas(exemple_points)  # (12, 2)


# In[393]:


def plus_haut(points):
    """ Trouve le point (xb, yb) le plus en haut à droite, en temps linéaire."""
    n = len(points)
    xb, yb = points[0]
    for j in range(1, n):
        xj, yj = points[j]
        if (yb < yj) or (yb == yj and xb < xj):
            xb, yb = xj, yj
    return xb, yb


# In[395]:


plus_haut(exemple_points)  # (21, 8)


# In[396]:


def plus_a_droite(b, h, points):
    if not points:
        return b, []
    t = points[0]
    q = points[1:]
    m, d = plus_a_droite(b, h, q)  # recursif !
    angle = alpha(b, t, h)
    if angle <= 0:
        return m, d
    else:
        if not d:
            return t, [t]
        if angle > alpha(b, m, h):
            return t, [t] + d
        else:
            return m, [t] + d


# In[400]:


def quickHull_droite(b, h, points):
    m, d = plus_a_droite(b, h, points)
    # si aucun point n'est à droite du segment orienté [b h], on en garde un seul, [b]
    if not d:
        return [b]
    # on fait les deux appels récursifs !
    return quickHull_droite(b, m, d) + quickHull_droite(m, h, d)


# In[408]:


def quickHull(points):
    b = plus_haut(points)
    h = plus_bas(points)
    return quickHull_droite(b, h, points) + quickHull_droite(h, b, points)


# In[409]:


quickHull(exemple_points)


# La complexité de cet algorithme est en $\mathcal{O}(n \log(n))$.
# 
# **Avec le _master theorem_**, on a $a=2, b=2, k=1$ : on divise les entrées en $a=2$ entrées de tailles $\leq b=2$ plus petites, sur lesquels on applique un traitement linéaire ($\mathcal{O}(n^{k=1})$ avant et après l'appel récursif.
# (*En supposant les points uniformément répartis dans le plan*.)
# 
# On pourrait l'implémenter, et vérifier la complexité sur des entrées aléatoires (ie. les points sont tirés uniformément dans une boîte carrée $(x_i,y_i) \sim [x_\min,x_\max] \times [y_\min,y_\max]$).
# 
# **Attention** ici avec Python, les ajout en tête de listes peuvent prendre un coût linéaire (et pas constant comme en OCaml) et les concaténations de listes prennent un coût linéaire ! Donc la vraie implémentation sera plus coûteuse que ce $\mathcal{O}(n \log(n))$ annoncé.

# #### Un exemple

# In[415]:


plt.figure()
plt.title("Des points en 2D, et leur enveloppe convexe")
Xs = [p[0] for p in exemple_points]
Ys = [p[1] for p in exemple_points]
plt.scatter(Xs, Ys)
p = exemple_points
enveloppe = quickHull(p)
q = enveloppe
h = len(enveloppe)
for i in range(h - 1):
    plt.plot([q[i][0], q[i+1][0]], [q[i][1], q[i+1][1]])
plt.plot([q[-1][0], q[0][0]], [q[-1][1], q[0][1]])
plt.show()


# #### Exemples aléatoires de taille contrôlée

# In[416]:


import random

def points_aleatoires(n=100, xmin=-10, xmax=10, ymin=-10, ymax=10):
    return [(random.randint(xmin, xmax), random.randint(ymin, ymax)) for _ in range(n)]


# In[424]:


xmin, xmax, ymin, ymax = -10, 10, -10, 10

for n in [5, 10, 50, 100, 500, 1000]:
    p = points_aleatoires(n=n, xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax)
    _ = plt.figure()
    _ = plt.title(f"{n} points aléatoires dans [{xmin},{xmax}] x [{ymin},{ymax}] en 2D, et leur enveloppe convexe")
    Xs = [pi[0] for pi in p]
    Ys = [pi[1] for pi in p]
    _ = plt.scatter(Xs, Ys)
    enveloppe = quickHull(p)
    q = enveloppe
    h = len(enveloppe)
    for i in range(h - 1):
        _ = plt.plot([q[i][0], q[i+1][0]], [q[i][1], q[i+1][1]])
    _ = plt.plot([q[-1][0], q[0][0]], [q[-1][1], q[0][1]])
    _ = plt.show()


# #### Complexité temporelle de ce calcul d'enveloppe convexe

# In[444]:


values_n = np.array(np.floor(np.logspace(1, 3.5, num=20)), dtype=int)
values_points = [ points_aleatoires(n=n) for n in values_n ]


# In[445]:


values_times = [
    timeit.timeit(
        stmt=f"quickHull({points})",
        number= 1000 if n <= 1000 else (100 if n <= 10000 else (10 if n <= 100000 else 1)),
        globals=globals()
    )
    for (n, points) in tqdm(list(zip(values_n, values_points)))
]


# In[446]:


plt.figure()
plt.xlabel("Size of the input array $n$")
plt.ylabel("Time in second")
plt.title("Time complexity of the quick hull algorithm (naive code in Python)")
plt.plot(values_n, values_times, "d-")
plt.show()


# In[447]:


plt.figure()
plt.xlabel("Size of the input array $n$")
plt.ylabel("Time in milli-second, normalized by $n \log(n)$")
plt.title("Time complexity of the quick hull algorithm (naive code in Python)")
normalized_values_times = 1e6 * np.array(values_times) / (values_n * np.log(values_n))
min_time = 1
plt.plot(values_n[values_n >= min_time], normalized_values_times[values_n >= min_time], "d-")
plt.show()


# ----
# ## Algorithme de Gauss-Karatsuba
# 
# - Problème :
#   + entrée = deux nombres `x` et `y`, avec `n` chiffres dans leurs écritures décimales,
#   + sortie = un nombre `z = x * y` produit des deux nombres.
# 
# - Algorithme :
#   + on découpe les deux nombres en nombres avec au plus `n/2` chiffres :
#     * découper `x` = `b + 10^{n/2} a`, avec `a` et `b` de taille au plus `n/2`
#     * découper `y` = `d + 10^{n/2} c`, avec `c` et `d` de taille au plus `n/2`
#   + trois appels récursifs au produit de nombres, de tailles deux fois plus petites
#   + on calcule `a * c` et `b * d`
#   + l'astuce vient de `ad_plus_bc = ad + bc = (a+b)(c+d) - ac - bd` comme `(a+b)(c+d) = ac + ad + bc + bd`
#   + `x y = (b + 10^{n/2} a) (d + 10^{n/2} c) = bd + 10^{n/2} (ad_plus_bc) + 10^{n} (a c)`

# La complexité de cet algorithme est en $\mathcal{O}(n^{\log_2(3)})$, asymptotiquement meilleur que $\mathcal{O}(n^2)$ la méthode naïve.
# 
# **Avec le _master theorem_**, on a $a=3, b=2, k=1$ : on divise les entrées en $a=7$ entrées de tailles $\leq b=2$ plus petites [1], sur lesquels on applique un traitement linéaire (toutes les additions $\mathcal{O}(n^{k=1})$ avant et après l'appel récursif.
# 
# Donc $a = 3 > b^k = 2$ ce qui donne $T(n) = \mathcal{O}(n^{\log_b(a)})$.
# 
# En comparaison, la méthode naïve, que voici, sera en avec $a=4$ appels récursifs, soit $a = 4 > b^k = 2$ ce qui donne $T(n) = \mathcal{O}(n^{\log_b(a)}) = \mathcal{O}(n^2)$.

# In[305]:


def naivemult(x, y, base=10):
    """ Function to multiply 2 numbers using the grade school algorithm."""
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        n = max(len(str(x)),len(str(y)))
        # that's suboptimal, and ugly, but it's quick to write

        nby2 = n // 2
        # split x in b + 10^{n/2} a, with a and b of sizes at most n/2
        a = x // base**(nby2)
        b = x %  base**(nby2)
        # split y in d + 10^{n/2} a, with c and d of sizes at most n/2
        c = y // base**(nby2)
        d = y %  base**(nby2)

        # we make 3 calls to entries which are 2 times smaller
        ac = naivemult(a, c)
        ad = naivemult(a, d)
        bd = naivemult(b, d)
        bc = naivemult(b, c)
        # x y = (b + 10^{n/2} a) (d + 10^{n/2} c)
        # ==> x y = bd + 10^{n/2} (b c + a d) + 10^{n} (a c)

        # this little trick, writing n as 2*nby2 takes care of both even and odd n
        prod = ac * base**(2*nby2) + ((ad + bc) * base**nby2) + bd

        return prod


# Et la fonction implémentant l'algorithme de Karatsuba.

# In[306]:


def karatsuba(x, y, base=10):
    """ Function to multiply 2 numbers in a more efficient manner than the grade school algorithm."""
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        n = max(len(str(x)),len(str(y)))
        # that's suboptimal, and ugly, but it's quick to write

        nby2 = n // 2
        # split x in b + 10^{n/2} a, with a and b of sizes at most n/2
        a = x // base**(nby2)
        b = x %  base**(nby2)
        # split y in d + 10^{n/2} c, with c and d of sizes at most n/2
        c = y // base**(nby2)
        d = y %  base**(nby2)

        # we make 3 calls to entries which are 2 times smaller
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        # ad + bc = (a+b)(c+d) - ac - bd as (a+b)(c+d) = ac + ad + bc + bd
        ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
        # x y = (b + 10^{n/2} a) (d + 10^{n/2} c)
        # ==> x y = bd + 10^{n/2} (ad_plus_bc) + 10^{n} (a c)

        # this little trick, writing n as 2*nby2 takes care of both even and odd n
        prod = ac * base**(2*nby2) + (ad_plus_bc * base**nby2) + bd

        return prod


# Un exemple :

# In[308]:


x = 1234
y = 4567
x * y
naivemult(x, y)
karatsuba(x, y)


# Des exemples de grandes tailles :

# In[278]:


def rand_largeint(n=1024):
    return int("".join(str(random.randint(0, 9)) for _ in range(n)))


# In[279]:


x = rand_largeint(1024)
y = rand_largeint(1024)
get_ipython().run_line_magic('timeit', 'x * y')
get_ipython().run_line_magic('timeit', 'naivemult(x, y)')
get_ipython().run_line_magic('timeit', 'karatsuba(x, y)')


# Quelle est l'influence de la base ?

# In[317]:


n = 1024
base = 10
get_ipython().run_line_magic('timeit', 'rand_largeint(n) * rand_largeint(n)')
get_ipython().run_line_magic('timeit', 'naivemult(rand_largeint(n), rand_largeint(n), base=base)')
get_ipython().run_line_magic('timeit', 'karatsuba(rand_largeint(n), rand_largeint(n), base=base)')


# In[318]:


n = 1024
base = 2
get_ipython().run_line_magic('timeit', 'rand_largeint(n) * rand_largeint(n)')
get_ipython().run_line_magic('timeit', 'naivemult(rand_largeint(n), rand_largeint(n), base=base)')
get_ipython().run_line_magic('timeit', 'karatsuba(rand_largeint(n), rand_largeint(n), base=base)')


# Et pour des entrées de tailles croissantes :

# In[281]:


for n in [2**3, 2**4, 2**5, 2**6, 2**7, 2**8, 2**9, 2**10, 2**11, 2**12]:
    print(f"\nFor n = {n} : Python native, naive then Karatsuba :")
    x = rand_largeint(n)
    y = rand_largeint(n)
    get_ipython().run_line_magic('timeit', 'x * y  # crazy fast!')
    get_ipython().run_line_magic('timeit', 'naivemult(x, y)')
    get_ipython().run_line_magic('timeit', 'karatsuba(x, y)')


# Ce n'est pas facile de vérifier le comportement en $n^{\log_2(3)}$ mais on voit déjà que la méthode de Gauss-Karatsuba est bien plus rapide que la méthode naïve !

# ----
# ## Algorithme de Strassen
# 
# - Cf le cours pour l'algorithme, ou https://fr.wikipedia.org/wiki/Algorithme_de_Strassen.
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


# <span style="color:red;">Attention</span> : peut-être que je devrais utiliser numba pour faire que ces fonctions naïves soient aussi efficaces que celles de Numpy (en gros).

# In[450]:


try:
    from numba import jit
except ImportError:
    def jit(f, *args, **kwargs):
        return f


# In[451]:


@jit
def ikjMatrixProduct(A, B):
    n = len(A)
    C = np.zeros((n, n), dtype=type(A[0,0]))
    for i in range(n):
        for k in range(n):
            for j in range(n):
                C[i,j] += A[i,k] * B[k,j]
    return C


# In[452]:


@jit
def add(A, B):
    n = len(A)
    C = np.zeros((n, n), dtype=type(A[0,0]))
    for i in range(n):
        for j in range(n):
            C[i,j] = A[i,j] + B[i,j]
    return C


# In[223]:


@jit
def subtract(A, B):
    n = len(A)
    C = np.zeros((n, n), dtype=type(A[0,0]))
    for i in range(n):
        for j in range(n):
            C[i,j] = A[i,j] - B[i,j]
    return C


# In[224]:


LEAF_SIZE = 64


# In[500]:


def strassenR(A, B, leaf_size=LEAF_SIZE):
    n = len(A)

    if n <= leaf_size:
        return ikjMatrixProduct(A, B)
    else:
        # initializing the new sub-matrices
        newSize = n//2
        a11 = A[:newSize, :newSize]  # top left
        a12 = A[:newSize, newSize:]  # top right
        a21 = A[newSize:, :newSize]  # bottom left
        a22 = A[newSize:, newSize:]  # bottom right
        b11 = A[:newSize, :newSize]  # top left
        b12 = A[:newSize, newSize:]  # top right
        b21 = A[newSize:, :newSize]  # bottom left
        b22 = A[newSize:, newSize:]  # bottom right

        # Calculating p1 to p7:
        p1 = strassenR(add(a11, a22), add(b11, b22)) # p1 = (a11+a22) * (b11+b22)
        p2 = strassenR(add(a21, a22), b11)  # p2 = (a21+a22) * (b11)
        p3 = strassenR(a11, subtract(b12, b22))  # p3 = (a11) * (b12 - b22)
        p4 = strassenR(a22, subtract(b21, b11))   # p4 = (a22) * (b21 - b11)
        p5 = strassenR(add(a11, a12), b22)  # p5 = (a11+a12) * (b22)   
        p6 = strassenR(subtract(a21, a11), add(b11, b12)) # p6 = (a21-a11) * (b11+b12)
        p7 = strassenR(subtract(a12, a22), add(b21, b22)) # p7 = (a12-a22) * (b21+b22)

        # calculating c21, c21, c11 e c22:
        c12 = add(p3, p5) # c12 = p3 + p5
        c21 = add(p2, p4)  # c21 = p2 + p4
        c11 = subtract(add(add(p1, p4), p7), p5) # c11 = p1 + p4 - p5 + p7
        c22 = subtract(add(add(p1, p3), p6), p2) # c22 = p1 + p3 - p2 + p6

        # Grouping the results obtained in a single matrix:
        C = np.zeros((n, n), dtype=type(A[0,0]))
        for i in range(newSize):
            for j in range(newSize):
                C[i,j] = c11[i,j]
                C[i,j + newSize] = c12[i,j]
                C[i + newSize,j] = c21[i,j]
                C[i + newSize,j + newSize] = c22[i,j]
        return C


# In[501]:


def strassen(A, B, leaf_size=LEAF_SIZE):
    assert isinstance(A, np.ndarray) and isinstance(B, np.ndarray)
    assert len(A) == len(A[0]) == len(B) == len(B[0])

    # Make the matrices bigger so that you can apply the strassen
    # algorithm recursively without having to deal with odd matrix sizes
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


# En fait, on devrait essayer d'utiliser les opérations les plus efficaces pour les additions et soustractions de matrices, afin de vraiment voir où se situe le gain de l'algorithme de Strassen.

# In[502]:


def strassenR_with_numpy_for_add_sub(A, B, leaf_size=LEAF_SIZE):
    n = len(A)

    if n <= leaf_size:
        return ikjMatrixProduct(A, B)
    else:
        # initializing the new sub-matrices
        newSize = n//2
        # dividing the matrices in 4 sub-matrices:
        a11 = A[:newSize, :newSize]  # top left
        a12 = A[:newSize, newSize:]  # top right
        a21 = A[newSize:, :newSize]  # bottom left
        a22 = A[newSize:, newSize:]  # bottom right
        b11 = A[:newSize, :newSize]  # top left
        b12 = A[:newSize, newSize:]  # top right
        b21 = A[newSize:, :newSize]  # bottom left
        b22 = A[newSize:, newSize:]  # bottom right

        # Calculating p1 to p7:
        p1 = strassenR(a11 + a22, b11 + b22) # p1 = (a11+a22) * (b11+b22)
        p2 = strassenR(a21 + a22, b11)  # p2 = (a21+a22) * (b11)
        p3 = strassenR(a11, b12 - b22)  # p3 = (a11) * (b12 - b22)
        p4 = strassenR(a22, b21 - b11)   # p4 = (a22) * (b21 - b11)
        p5 = strassenR(a11 + a12, b22)  # p5 = (a11+a12) * (b22)   
        p6 = strassenR(a21 - a11, b11 + b12) # p6 = (a21-a11) * (b11+b12)
        p7 = strassenR(a12 - a22, b21 + b22) # p7 = (a12-a22) * (b21+b22)

        # calculating c21, c21, c11 e c22:
        c12 = p3 + p5 # c12 = p3 + p5
        c21 = p2 + p4  # c21 = p2 + p4
        c11 = p1 + p4 + p7 - p5 # c11 = p1 + p4 - p5 + p7
        c22 = p1 + p3 + p6 - p2 # c22 = p1 + p3 - p2 + p6

        # Grouping the results obtained in a single matrix:
        C = np.zeros((n, n), dtype=type(A[0,0]))
        C[:newSize, :newSize] = c11
        C[:newSize, newSize:] = c12
        C[newSize:, :newSize] = c21
        C[newSize:, newSize:] = c22
        return C


# In[503]:


def strassen_with_numpy_for_add_sub(A, B, leaf_size=LEAF_SIZE):
    assert isinstance(A, np.ndarray) and isinstance(B, np.ndarray)
    assert len(A) == len(A[0]) == len(B) == len(B[0])

    # Make the matrices bigger so that you can apply the strassen
    # algorithm recursively without having to deal with odd matrix sizes
    nextPowerOfTwo = lambda n: 2**int(ceil(log(n,2)))
    n = len(A)
    m = nextPowerOfTwo(n)
    APrep = np.zeros((m, m), dtype=type(A[0,0]))
    BPrep = np.zeros((m, m), dtype=type(A[0,0]))
    APrep[:n, :n] = A
    BPrep[:n, :n] = B
    CPrep = strassenR_with_numpy_for_add_sub(APrep, BPrep, leaf_size=leaf_size)
    return CPrep[:n, :n]


# Pour générer des exemples de tailles grandissantes :

# In[471]:


import random


# In[472]:


def random_matrix(n, minint=0, maxint=1000):
    A = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            A[i, j] = random.randint(minint, maxint)
    return A


# In[504]:


A = random_matrix(4)
A


# In[505]:


B = random_matrix(4)
B


# On vérifie sur un exemple que nos deux algorithmes calculant le produit $AB$ de matrices sont corrects :

# In[506]:


A @ B


# In[507]:


ikjMatrixProduct(A, B)


# In[508]:


strassenR(A, B, leaf_size=1)


# In[509]:


strassenR(A, B, leaf_size=2)


# In[510]:


strassenR_with_numpy_for_add_sub(A, B, leaf_size=1)


# In[511]:


strassenR_with_numpy_for_add_sub(A, B, leaf_size=2)


# Pour des tests de taille $n$ croissantes :

# In[302]:


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


# Ce premier test était les versions les plus lentes :

# In[304]:


for n in [2**5, 2**6, 2**7]:
    print(f"\nFor n = {n} : numpy, ten ikj naive algorithm, then Strassen, then (slightly) faster Strassen :")
    A = random_matrix(n)
    B = random_matrix(n)
    get_ipython().run_line_magic('timeit', 'A @ B  # crazy fast!')
    get_ipython().run_line_magic('timeit', 'ikjMatrixProduct(A, B)')
    get_ipython().run_line_magic('timeit', 'strassen(A, B, leaf_size=4)')
    get_ipython().run_line_magic('timeit', 'strassen_with_numpy_for_add_sub(A, B, leaf_size=4)')


# Je pense que cette implémentation est assez nulle, parce que les allocations de mémoire, et les boucles `for` en Python sont très lentes.

# C'était très lent ! Beaucoup trop d'allocations mémoire !
# J'ai optimisé et (naïvement) simplifié le code, en enlevant les déclarations mémoires inutiles, mais surtout en utilisant [`numba.jit`](https://numba.pydata.org/numba-doc/latest/reference/jit-compilation.html#numba.jit) pour optimiser les opérations `add` et `substract`, et on obtient des temps bien plus courts :

# In[513]:


for n in [2**5, 2**6, 2**7, 2**8, 2**9]:
    print(f"\nFor n = {n} : numpy, ten ikj naive algorithm, then Strassen, then (slightly) faster Strassen :")
    A = random_matrix(n)
    B = random_matrix(n)
    get_ipython().run_line_magic('timeit', 'A @ B  # crazy fast!')
    get_ipython().run_line_magic('timeit', 'ikjMatrixProduct(A, B)')
    get_ipython().run_line_magic('timeit', 'strassen(A, B, leaf_size=4)')
    get_ipython().run_line_magic('timeit', 'strassen_with_numpy_for_add_sub(A, B, leaf_size=4)')


# Est-ce que les temps sont vraiment différents si les deux matrices `A` et `B` changent à chaque test ? Pas vraiment ! Mais pour les petites valeurs de `n`, les quatre façons de multiplier sont toutes aussi lentes : le temps est principalement passé à générer `A` et `B` !

# In[514]:


for n in [2**5, 2**6, 2**7, 2**8, 2**9, 2**10]:
    print(f"\nFor n = {n} : numpy, ten ikj naive algorithm, then Strassen, then (slightly) faster Strassen :")
    get_ipython().run_line_magic('timeit', 'random_matrix(n) @ random_matrix(n)')
    get_ipython().run_line_magic('timeit', 'ikjMatrixProduct(random_matrix(n), random_matrix(n))')
    get_ipython().run_line_magic('timeit', 'strassen(random_matrix(n), random_matrix(n), leaf_size=64)')
    get_ipython().run_line_magic('timeit', 'strassen_with_numpy_for_add_sub(random_matrix(n), random_matrix(n), leaf_size=64)')


# In[515]:


for n in [2**7, 2**8]:
    print(f"\nFor n = {n} : numpy, ten ikj naive algorithm, then Strassen, then (slightly) faster Strassen :")
    get_ipython().run_line_magic('timeit', 'random_matrix(n) @ random_matrix(n)')
    get_ipython().run_line_magic('timeit', 'ikjMatrixProduct(random_matrix(n), random_matrix(n))')
    for leaf_size in [1, 8, 32, 64, 128]:
        print(f"Both Strassen, with a leaf size = {leaf_size}")
        get_ipython().run_line_magic('timeit', 'strassen(random_matrix(n), random_matrix(n), leaf_size=leaf_size)')
        get_ipython().run_line_magic('timeit', 'strassen_with_numpy_for_add_sub(random_matrix(n), random_matrix(n), leaf_size=leaf_size)')


# ----
# ## Transformée de Fourier Rapide (FFT)
# 
# - Regardez [ces notes de cours]() pour les détails, [ou cette page](http://algorithms.wtf/notes/A-fft.pdf).

# ### Transformée de Fourier Discrète (DFT), implémentation naïve
# 
# Ce premier algorithme est simple à écrire, et a une complexité en $\Theta(n^2)$.

# In[538]:


def dft(x):
    n = len(x)
    omega = lambda j, k: np.exp(- (j * k) * 2j * np.pi / n)
    f = np.zeros_like(x)
    for j in range(n):
        for k in range(n):
            f[j] += x[k] * omega(j, k)
    return f


# In[533]:


def round_complex(x, decimals=0):
    return np.round(np.real(x), decimals=decimals) + 1j * np.round(np.imag(x), decimals=decimals)


# In[580]:


x = np.exp(2j * np.pi * np.arange(8) / 8)
x
f = dft(x)
f


# In[581]:


round_complex(f)


# On va faire des tests numériques, avec une version "optimisée" automatiquement grâce à [`numba.jit`](https://numba.pydata.org/numba-doc/latest/reference/jit-compilation.html#numba.jit).

# In[541]:


@jit
def dft_jit(x):
    n = len(x)
    pi_2j_by_n = 2j * np.pi / n
    f = np.zeros_like(x)
    for j in range(n):
        for k in range(n):
            f[j] += x[k] * np.exp(- (j * k) * pi_2j_by_n)
    return f


# In[542]:


round_complex(dft_jit(x))


# ### Implémentation de FFT dans le module `numpy`

# In[543]:


f2 = np.fft.fft(x)
round_complex(f2)


# In this example, real input has an FFT which is Hermitian, i.e., symmetric
# in the real part and anti-symmetric in the imaginary part, as described in
# the `numpy.fft` documentation:

# In[517]:


import matplotlib.pyplot as plt
t = np.arange(256)
sp = np.fft.fft(np.sin(t))
freq = np.fft.fftfreq(t.shape[-1])
plt.plot(freq, sp.real, freq, sp.imag)


# ### Implémentation de la DFT par multiplication matricielle
# 
# On peut calculer la matrice de Vandermonde $W_N \in\mathbb{C}^{N \times N}$, associée à la racine $\omega_N = \exp(-i \frac{2\pi}{N}$ pour un signal de taille $N$, et ensuite calculer la DFT(x) comme $z = W_N x$ (produit matriciel). Cf [cette page Wikipédia](https://fr.wikipedia.org/wiki/Transformation_de_Fourier_discr%C3%A8te#Interpr%C3%A9tation_matricielle).

# In[555]:


def vandermonde_fourier(n):
    pi_2j_by_n = 2j * np.pi / n
    omega = np.zeros((n, n), dtype=np.complex)
    for j in range(n):
        for k in range(n):
            omega[j, k] = np.exp(- (j * k) * pi_2j_by_n)
    return omega


# In[567]:


def dft_naive_matmult(x):
    n = len(x)
    return vandermonde_fourier(len(x)) * np.array(x)


# In[582]:


f3 = dft_naive_matmult(x)
round_complex(f3)


# In[568]:


get_ipython().run_line_magic('timeit', 'dft_naive_matmult(random_complex_vector(2**8))')


# Une approche plus efficace :

# In[559]:


def vandermonde_fourier2(n):
    pi_2j_by_n = 2j * np.pi / n
    omega = np.zeros((n, n), dtype=np.complex)
    for j in range(n):
        omega[j, :] = np.exp(- (j * np.arange(n)) * pi_2j_by_n)
    return omega


# In[560]:


def dft_naive_matmult2(x):
    n = len(x)
    return vandermonde_fourier2(len(x)) * np.array(x)


# In[543]:


f4 = dft_naive_matmult2(x)
round_complex(f4)


# In[561]:


get_ipython().run_line_magic('timeit', 'dft_naive_matmult2(random_complex_vector(2**8))')


# Une approche encore un peu plus efficace :

# In[569]:


@jit
def vandermonde_fourier3(n):
    pi_2j_by_n = 2j * np.pi / n
    omega = np.zeros((n, n), dtype=np.complex)
    for j in range(n):
        omega[j, :] = np.exp(- (j * np.arange(n)) * pi_2j_by_n)
    return omega


# In[572]:


def dft_naive_matmult3(x):
    n = len(x)
    return vandermonde_fourier3(len(x)) * np.array(x)


# In[583]:


f5 = dft_naive_matmult3(x)
round_complex(f5)


# In[573]:


get_ipython().run_line_magic('timeit', 'dft_naive_matmult3(random_complex_vector(2**8))')


# ### Implémentation manuelle de la FFT (Cooley-Tucker)
# Comme avec notre petite implémentation de l'algorithme de Strassen, on va se restreindre aux valeurs $n = 2^p$ pour $p=\mathbb{N}$.
# On va utiliser la DFT naïve pour les valeurs trop petites, comme on sait que trop d'appels récursifs ajoutent un gros surcoût (avec `leaf_size=64`, cela devrait donner un bon compromis).
# 
# Cf. [cette page Wikipédia](https://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm#The_radix-2_DIT_case)

# In[554]:


LEAF_SIZE = 64


# In[574]:


x = np.arange(16)


# In[575]:


x


# In[576]:


even_x = x[::2]
even_x
odd_x = x[1::2]
odd_x


# <img width="45%" src="figures/CM3_Radix2FFT.png">

# In[586]:


def fft(x, leaf_size=64):
    n = len(x)
    if n <= leaf_size:
        return dft(x)
    n_by_2 = n//2
    assert n == 2 * n_by_2, "Error : only n = 2^k are accepted."
    # we split the entries in 2 vectors of size n/2
    # we compute the two FFT, recursively
    even_fft = fft(x[0::2])
    odd_fft  = fft(x[1::2])
    # combine the two
    full_fft = np.zeros(n, dtype=np.complex)
    omega_n = np.exp(2j * np.pi / n)
    omega = 1
    for j in range(n_by_2):
        full_fft[j]          = even_fft[j] + omega * odd_fft[j]
        full_fft[j + n_by_2] = even_fft[j] - omega * odd_fft[j]
        omega = omega * omega_n
    return full_fft


# Un exemple, pour vérifier notre implémentation :

# In[587]:


f6 = fft(x, leaf_size=1)
round_complex(f6)


# Pour l'instant, rien n'est correct !
# 
# <span style="font-size:300%; color:red;">FIXME finish this!</span>

# ### Tests avec des vecteurs aléatoires
# On va définir des vecteurs $x\in\mathbb{C}^n$ aléatoires, distribués selon des lois normales centrées.

# In[544]:


def random_complex_vector(n=16):
    return np.random.standard_normal(size=n) + 1j * np.random.standard_normal(size=n)


# In[548]:


x = random_complex_vector(4)
x
f1 = np.fft.fft(x)
f1
f2 = dft(x)
f2
f3 = dft_jit(x)
f3


# Maintenant quelques comparaisons, montrant que l'implémentation naïve est très mauvaise en comparaison de celle optimisée (en C) de `numpy.fft` :

# In[551]:


for n in [2**4, 2**5, 2**6, 2**7, 2**8]:
    print(f"""\nPour des vecteurs aléatoires de tailles {n}
    numpy.fft.fft | dft naive | dft numba""")
    x = random_complex_vector(n)
    get_ipython().run_line_magic('timeit', 'np.fft.fft(x)')
    get_ipython().run_line_magic('timeit', 'dft(x)')
    get_ipython().run_line_magic('timeit', 'dft_jit(x)')


# In[553]:


round(157_000 / 7.21)


# Avec une taille aussi petite que juste `n=2**8=256` échantillons, la DFT naïve (en $\Theta(n^2)$) et en pure Python est déjà environ **20_000 fois plus lente que la FFT optimisée**.
# La DFT naïve mais compilée avec [`numba.jit`](https://numba.pydata.org/numba-doc/latest/reference/jit-compilation.html#numba.jit) est quant à elle 1000 plus lente.

# ## Conclusion
# 
# C'est bon pour aujourd'hui !
