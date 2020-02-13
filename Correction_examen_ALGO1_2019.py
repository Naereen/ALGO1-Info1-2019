#!/usr/bin/env python
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Correction-examen-ALGO1---Décembre-2019" data-toc-modified-id="Correction-examen-ALGO1---Décembre-2019-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Correction examen ALGO1 - Décembre 2019</a></div><div class="lev1 toc-item"><a href="#Problème-1-:-Programmation-dynamique" data-toc-modified-id="Problème-1-:-Programmation-dynamique-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Problème 1 : Programmation dynamique</a></div><div class="lev2 toc-item"><a href="#Question-2." data-toc-modified-id="Question-2.-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Question 2.</a></div><div class="lev2 toc-item"><a href="#Question-3." data-toc-modified-id="Question-3.-22"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Question 3.</a></div><div class="lev2 toc-item"><a href="#Question-4." data-toc-modified-id="Question-4.-23"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Question 4.</a></div><div class="lev2 toc-item"><a href="#Question-5." data-toc-modified-id="Question-5.-24"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Question 5.</a></div><div class="lev1 toc-item"><a href="#Problème-3-:-Morito" data-toc-modified-id="Problème-3-:-Morito-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Problème 3 : Morito</a></div><div class="lev2 toc-item"><a href="#Question-1.-echanger" data-toc-modified-id="Question-1.-echanger-31"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Question 1. <code>echanger</code></a></div><div class="lev2 toc-item"><a href="#Question-2.-morito" data-toc-modified-id="Question-2.-morito-32"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Question 2. <code>morito</code></a></div><div class="lev3 toc-item"><a href="#Question-3.-Exemple" data-toc-modified-id="Question-3.-Exemple-321"><span class="toc-item-num">3.2.1&nbsp;&nbsp;</span>Question 3. Exemple</a></div><div class="lev3 toc-item"><a href="#Question-5.-Complexité-temporelle-?" data-toc-modified-id="Question-5.-Complexité-temporelle-?-322"><span class="toc-item-num">3.2.2&nbsp;&nbsp;</span>Question 5. Complexité temporelle ?</a></div><div class="lev1 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Conclusion</a></div>

# # Correction examen ALGO1 - Décembre 2019
# 
# - [Page du cours](https://perso.crans.org/besson/teach/info1_algo1_2019/) : https://perso.crans.org/besson/teach/info1_algo1_2019/
# - Magistère d'Informatique (L3 SIF) & L3 Maths de Rennes - ENS Rennes - Année 2019/2020
# - Intervenants :
#   + Cours : [Lilian Besson](https://perso.crans.org/besson/) (info) et [François Schwarzentruber](http://people.irisa.fr/Francois.Schwarzentruber/math1_algo1_2019/) (maths)
#   + Travaux dirigés : [Raphaël Truffet](http://perso.eleves.ens-rennes.fr/people/Raphael.Truffet/) (info) et [Léo Henry](http://perso.eleves.ens-rennes.fr/people/leo.henry/) (maths)

# ---
# # Problème 1 : Programmation dynamique

# <img width="50%" src="Probleme2_Q2Q3.png"></img>

# On va représenter les dominos et les chaînes de domino de façon naïve :

# In[1]:


exemple_dominos = [
    ("A", "H"),
    ("A", "Z"),
    ("K", "V"),
    ("H", "K"),
    ("Z", "V"),
    ("V", "X"),
]


# ## Question 2.
# 
# On peut implémenter l'algorithme de "programmation dynamique" naïvement :

# In[2]:


def calculer_tableau_C(dominos):
    n = len(dominos)
    x = [D[0] for D in dominos]
    y = [D[1] for D in dominos]
    C = [0] * n
    C[0] = 1
    for i in range(1, n):
        meilleur = 1
        for j in range(0, i-1 + 1):
            if y[j] == x[i] and C[j] + 1 > meilleur:
                meilleur = C[j] + 1
        C[i] = meilleur
    return C


# Et par exemple :

# In[3]:


calculer_tableau_C(exemple_dominos)


# ## Question 3.

# In[4]:


def longueur_sous_chaine_la_plus_longue(dominos):
    return max(calculer_tableau_C(dominos))


# Et par exemple :

# In[5]:


longueur_sous_chaine_la_plus_longue(exemple_dominos)


# ## Question 4.
# On va juste réécrire la fonction de la question 2, en ajoutant de l'affichage :

# In[22]:


def calculer_tableau_C_verbose(dominos):
    n = len(dominos)
    x = [D[0] for D in dominos]
    y = [D[1] for D in dominos]
    C = [0] * n
    C[0] = 1
    i = 0
    print(f"- C[{i+1}] = {C[i]}.")
    for i in range(1, n):
        meilleur = 1
        list_of_possible_j = []
        list_of_values_in_max = [1]
        for j in range(0, i-1 + 1):
            if y[j] == x[i] and C[j] + 1 > meilleur:
                meilleur = C[j] + 1
                list_of_possible_j.append(j)
                list_of_values_in_max.append(C[j] + 1)
        C[i] = meilleur
        if len(list_of_possible_j) > 1:
            s1 = ", ".join(f"C[{j+1}]+1" for j in list_of_possible_j)
            s2 = " et ".join(f"{j+1}-{i+1}" for j in list_of_possible_j)
            print(f"- C[{i+1}] = max(1, {s1}) = {C[i]} (les couples {s2} sont compatibles).")
        elif len(list_of_possible_j) == 1:
            j = list_of_possible_j[0]
            print(f"- C[{i+1}] = max(1, C[{j+1}]+1) = {C[i]} (les dés {j+1} et {i+1} sont compatibles).")
        else:
            print(f"- C[{i+1}] = {C[i+1]} (il n'y pas de dé compatible à gauche de la {i+1}ème pièce).")
    return C


# Et par exemple :

# In[21]:


calculer_tableau_C_verbose(exemple_dominos)


# ## Question 5.
# 
# On va avoir besoin d'une fonction `argmax` :

# In[23]:


def argmax(tableau):
    position = 0
    valeur = tableau[position] # Invariant: max(T[0],...,T[i])
    for i in range(1, len(tableau)):
        if tableau[i] > valeur:
            valeur = tableau[i]
            # Invariant: valeur' = max(T[0],...,T[i+1]) = max(valeur, T[i+1])
            position = i
    return position


# In[25]:


argmax([1, 1, 1, 2, 2, 3])
argmax([1, 1, 2, 2, 3, 1])
argmax([1, 2, 2, 3, 1, 1])
argmax([2, 2, 3, 1, 1, 1])
argmax([2, 3, 1, 1, 1, 2])
argmax([3, 1, 1, 1, 2, 2])


# Pour chaque $i$, il faut mémoriser le meilleur dé $j$ à mettre à gauche de $D[i]$.
# 
# Puis on prend le $i$ qui maximise $C[i]$, et on compose la sous-chaı̂ne optimale de droite à gauche : $i$, puis $J[i]$, puis $J[J[i]]$ etc, jusqu’à tomber sur un $0$.
# 
# Cela donne l'algorithme suivant :

# In[35]:


def calculer_sous_chaine_longueur_maximale(dominos):
    n = len(dominos)
    x = [D[0] for D in dominos]
    y = [D[1] for D in dominos]
    C = [0] * n
    J = [0] * n
    C[0] = 1
    J[0] = 0
    for i in range(1, n):
        meilleur = 1
        for j in range(0, i-1 + 1):
            if y[j] == x[i] and C[j] + 1 > meilleur:
                meilleur = C[j] + 1
                J[i] = j
        C[i] = meilleur
    i_maximisant_C = argmax(C)
    i = i_maximisant_C
    chaine_maximale = [i]
    while J[i] != 0:
        chaine_maximale.append(J[i])
        i = J[i]
    chaine = [dominos[i] for i in chaine_maximale[::-1]]
    print(f"Une chaine de longueur maximale = {max(C)} a été trouvée :")
    print(", ".join(f"[{d[0]}|{d[1]}]" for d in chaine))
    return chaine_maximale, chaine


# Et par exemple :

# In[36]:


calculer_sous_chaine_longueur_maximale(exemple_dominos)


# ---
# # Problème 3 : Morito

# ## Question 1. `echanger`

# In[37]:


def echanger(tableau, i, j):
    tmp = tableau[i]
    tableau[i] = tableau[j]
    tableau[j] = tmp
    # en Python, on peut aussi faire
    # tableau[i], tableau[j] = tableau[j], tableau[i]


# ## Question 2. `morito`
# 
# On implémente l'algorithme "mystère" :

# In[55]:


def morito(tableau, verb=False):
    n = len(tableau)
    échangé = True
    while échangé:
        échangé = False
        if verb: print("Début pour croissant...")
        for i in range(0, n-2 + 1):
            if verb: print(f"  Tableau = {tableau} et i = {i}")
            if tableau[i] > tableau[i+1]:
                if verb: print(f"    T[{i}] = {tableau[i]} > {tableau[i+1]} = T[{i+1}] sont échangés")
                echanger(tableau, i, i+1)
                échangé = True
        
        if verb: print("Début pour décroissant...")
        for i in range(n-2, 0 - 1, -1):
            if verb: print(f"  Tableau = {tableau} et i = {i}")
            if tableau[i] > tableau[i+1]:
                if verb: print(f"    T[{i}] = {tableau[i]} > {tableau[i+1]} = T[{i+1}] sont échangés")
                echanger(tableau, i, i+1)
                échangé = True
    if verb: print("Pas d'échange dans les deux parcours, l'algorithme s'arrête là.")


# ### Question 3. Exemple
# Par exemple :

# In[56]:


tableau = [16, 18, 19, 12, 2019]
print(tableau)

morito(tableau)
print(tableau)


# In[57]:


tableau = [16, 18, 19, 12, 2019]
print(tableau)

morito(tableau, verb=True)
print(tableau)


# ### Question 5. Complexité temporelle ?

# - Dans le meilleur cas, l'algorithme s'exécute en temps linéaire, ie., $\mathcal{O}(n)$ si $n$ est la longueur du tableau $T$. Le meilleur cas correspond à un tableau trié par ordre croissant.

# In[59]:


print("Pour des tableaux triés par ordre croissant :")
for n in [100, 1000, 10000, 100000]:
    print(f"Pour n = {n}, l'algorithme morito prend le temps suivant")
    get_ipython().run_line_magic('timeit', 'morito(list(range(n)))')


# Ce petit exemple montre que la complexité temporelle empirique semble bien linéaire : multiplier $n$ par $10$ multiplie le temps de calcul par $10$ aussi !

# - Dans le cas moyen, l'algorithme s'exécute en temps quadratique, ie., $\mathcal{O}(n^2)$.

# In[60]:


import numpy.random as rd

def tableau_aleatoire(n):
    return rd.randint(-1000, 1000, n)


# In[62]:


print("Pour des tableaux aléatoires :")
for n in [100, 1000, 10000]:
    print(f"Pour n = {n}, l'algorithme morito prend le temps suivant")
    get_ipython().run_line_magic('timeit', 'morito(tableau_aleatoire(n))')


# Ce petit exemple montre que la complexité temporelle empirique semble bien quadratique : multiplier $n$ par $10$ multiplie le temps de calcul par $10^2=100$ !
# (le temps est plus long que pour le pire cas ci dessous, mais c'est à cause du temps pris par le calcul d'un tableau aléatoire, pas le reste)

# - Dans le pire cas, l'algorithme s'exécute aussi en temps quadratique, ie., $\mathcal{O}(n^2)$.

# In[63]:


print("Pour des tableaux triés par ordre décroissant :")
for n in [100, 1000, 10000]:
    print(f"Pour n = {n}, l'algorithme morito prend le temps suivant")
    get_ipython().run_line_magic('timeit', 'morito(list(range(n))[::-1])')


# Ce petit exemple montre que la complexité temporelle empirique semble bien quadratique : multiplier $n$ par $10$ multiplie le temps de calcul par $10^2=100$ !

# ---
# # Conclusion
# 
# - Regardez aussi [la correction papier]() au partiel (envoyée par mail).
# 
# - Les autres problèmes pourraient aussi être implémentés, mais :
# 
#   + [le notebook du cours #8 sur les flots traitent déjà le problème 4](https://perso.crans.org/besson/teach/info1_algo1_2019/notebooks/CoursMagistral_8.html)
#   + le problème 2 ne demande pas de proposer un algorithme, mais les arbres rouge-noir peuvent être implémentés sans trop de difficultés, et on pourrait tester empiriquement les différents points du problème 2. Voir par exemple [des implémentations en Python](https://duckduckgo.com/?q=code+for+red-black+tree+in+python&t=canonical&ia=web), notamment celle ci : [github.com/stanislavkozlovski/Red-Black-Tree](https://github.com/stanislavkozlovski/Red-Black-Tree).
