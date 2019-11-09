#!/usr/bin/env python
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#ALGO1-:-Introduction-à-l'algorithmique" data-toc-modified-id="ALGO1-:-Introduction-à-l'algorithmique-1"><span class="toc-item-num">1&nbsp;&nbsp;</span><a href="https://perso.crans.org/besson/teach/info1_algo1_2019/" target="_blank">ALGO1 : Introduction à l'algorithmique</a></a></div><div class="lev1 toc-item"><a href="#Cours-Magistral-9" data-toc-modified-id="Cours-Magistral-9-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Cours Magistral 9</a></div><div class="lev2 toc-item"><a href="#Documentation-de-scipy.opt.linprog" data-toc-modified-id="Documentation-de-scipy.opt.linprog-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Documentation de <code>scipy.opt.linprog</code></a></div><div class="lev2 toc-item"><a href="#Fonction-de-débogage" data-toc-modified-id="Fonction-de-débogage-22"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Fonction de débogage</a></div><div class="lev2 toc-item"><a href="#Premier-exemple" data-toc-modified-id="Premier-exemple-23"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Premier exemple</a></div><div class="lev2 toc-item"><a href="#Second-exemple" data-toc-modified-id="Second-exemple-24"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Second exemple</a></div><div class="lev3 toc-item"><a href="#Essayons-avec-différentes-méthodes-de-résolution-:" data-toc-modified-id="Essayons-avec-différentes-méthodes-de-résolution-:-241"><span class="toc-item-num">2.4.1&nbsp;&nbsp;</span>Essayons avec différentes méthodes de résolution :</a></div><div class="lev4 toc-item"><a href="#Avec-la-méthode-du-simplexe" data-toc-modified-id="Avec-la-méthode-du-simplexe-2411"><span class="toc-item-num">2.4.1.1&nbsp;&nbsp;</span>Avec la méthode du simplexe</a></div><div class="lev4 toc-item"><a href="#Avec-la-méthode-du-simplexe" data-toc-modified-id="Avec-la-méthode-du-simplexe-2412"><span class="toc-item-num">2.4.1.2&nbsp;&nbsp;</span>Avec la méthode du simplexe</a></div><div class="lev2 toc-item"><a href="#Implémentation-manuelle-de-l'algorithme-du-simplexe" data-toc-modified-id="Implémentation-manuelle-de-l'algorithme-du-simplexe-25"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Implémentation manuelle de l'algorithme du simplexe</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-26"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>Conclusion</a></div>

# # [ALGO1 : Introduction à l'algorithmique](https://perso.crans.org/besson/teach/info1_algo1_2019/)
# 
# - [Page du cours](https://perso.crans.org/besson/teach/info1_algo1_2019/) : https://perso.crans.org/besson/teach/info1_algo1_2019/
# - Magistère d'Informatique de Rennes - ENS Rennes - Année 2019/2020
# - Intervenants :
#   + Cours : [Lilian Besson](https://perso.crans.org/besson/)
#   + Travaux dirigés : [Raphaël Truffet](http://perso.eleves.ens-rennes.fr/people/Raphael.Truffet/)
# - Références :
#   + [Open Data Structures](http://opendatastructures.org/ods-python.pdf)

# # Cours Magistral 9
# 
# - Ce cours traite de programmation linéaire.
# 
# - On va illustrer deux programmes linéaires résolus avec la fonction `scipy.optimize.linprog`.

# In[1]:


import numpy as np

import matplotlib.pyplot as plt

import scipy.optimize as opt


# ## Documentation de `scipy.opt.linprog`

# In[2]:


help(opt.linprog)


# La programmation linéaire résout des problèmes de la forme suivante :
# 
# $$
# \begin{align}
# \min_x \ & c^T x \\
# \mbox{such that} \ & A_{ub} x \leq b_{ub},\\
# & A_{eq} x = b_{eq},\\
# & l \leq x \leq u ,
# \end{align}
# $$
# 
# avec $x$ un vecteur de variables de décisions ; $c$, $b_{ub}$, $b_{eq}$, $l$, et $u$ sont des vecteurs ; $A_{ub}$ et $A_{eq}$ sont des matrices.

# ## Fonction de débogage

# In[60]:


def make_callback():
    list_of_x, list_of_fun = [], []
    def debug_callback(opt_res):
        print("\nA new optimization step gave:")
        print(f"Current solution x = {opt_res.x}")
        list_of_x.append(opt_res.x)
        print(f"Current value of c @ x = {opt_res.fun}")
        list_of_fun.append(opt_res.fun)
        print(f"Success? = {opt_res.success}")
        print(f"The (nominally positive) values of the slack, b_ub - A_ub @ x. = {opt_res.slack}")
        print(f"The (nominally zero) residuals of the equality constraints, b_eq - A_eq @ x. = {opt_res.con}")
        print(f"Algorithm in phase {opt_res.phase}")
        print(f"Algorithm in iteration number {opt_res.nit}")
        status = {
            0: "Optimization proceeding nominally.",
            1: "Iteration limit reached.",
            2: "Problem appears to be infeasible.",
            3: "Problem appears to be unbounded.",
            4: "Numerical difficulties encountered.",
        }
        print(f"Algorithm status {status[opt_res.status]}")
        if opt_res.message: print(f"Algorithm message: {opt_res.message}")
    return list_of_x, list_of_fun, debug_callback


# ## Premier exemple
# 
# On va suivre l'exemple détaillé en cours :
# 
# - Variables
#   + $x$ nombre de tables fabriquées par semaine,
#   + $y$ nombre de chaises fabriquées par semaine.
# 
# - Objectif :
#   + maximiser $30x + 10y$.
# 
# - Contraintes :
#   + heures de travail : $6x+3y \leq 36$,
#   + demande : $y \geq 3x$,
#   + stockage : $x + y/4 \leq 4$,
#   + positivité : $x \geq 0$,
#   + positivité : $y \geq 0$.

# Mise sous la forme requise par la fonction `linprog`, cela va donner :
# 
# $$
# \begin{align}
# \min_{[x, y]} \ & [-30, -10]^T [x, y] \\
# \mbox{such that} \ & 
#     [
#         [6, 3], [-3, 1], [1, 1/4]
#     ]
#     [x, y]
# = [6x + 3y, y - 3x, x + y/4] \leq [36, 0, 4],\\
# & [0, 0] \leq [x, y] \leq [+\infty,+\infty] ,
# \end{align}
# $$

# Et donc avec Python cela sera :

# In[83]:


c = np.array([-30, -10])

A_ub = np.array([[6, 3], [-3, 1], [1, 1/4]])
b_ub = np.array([36, 0, 4])

A_eq = None
b_eq = None

# all variables are bound to be in (0, +inf)
bounds = (0, None)


# Objectif :

# In[84]:


import sympy
x, y = sympy.var('x y')


# In[85]:


c.T @ [x, y]


# Contraintes d'inéqualités :

# In[86]:


A_ub @ [x, y]


# In[87]:


b_ub


# Essaysons avec différentes méthodes de résolution :

# In[88]:


opt.linprog(c,
            A_ub=A_ub, b_ub=b_ub,
            A_eq=A_eq, b_eq=b_eq,
            bounds=bounds,
            method="simplex",
            callback=debug_callback,
)


# In[89]:


x_opt, y_opt = _.x


# La solution obtenue est donc $x = 2.28$ et $y = 6.85$, qui donnerait un profit maximal de $+137 €$ par semaine en respectant toutes les contraintes.
# 
# Pour obtenir une solution entière, on essaie $x = 2, 3$ et $y = 6, 7$, ie. on arrondit en dessous et au dessus, et on prend la solution qui satisfait les contraintes et maximise l'objectif :

# In[90]:


x_opt, y_opt


# In[96]:


import itertools


# In[95]:


sol = None
min_obj = float("+inf")

for (x, y) in itertools.product(
        [np.floor(x_opt), np.ceil(x_opt)],
        [np.floor(y_opt), np.ceil(y_opt)],
    ):
    obj = c.T @ [x, y]
    ctr = (A_ub @ [x, y]) <= b_ub
    print(f"Pour (x, y) = {x, y}, l'objectif vaut {obj}, la contrainte vaut {ctr}")
    if np.all(ctr) and obj < min_obj:
        min_obj = obj
        sol = [x, y]

print(f"==> Donc on utilise la solution entière optimale = {sol}")


# La solution entière optimale à ce premier problème est donc de fabriquer $x=2$ tables et $y=6$ chaises chaque semaine.

# ## Second exemple

# <img src="figures/CM9_ensemble_admissible.png">

# Mise sous la forme requise par la fonction `linprog`, cela va donner :
# 
# $$
# \begin{align}
# \min_{[x, y]} \ & [4, 3]^T [x, y] \\
# \mbox{such that} \ & 
#     [
#         [-1, 4], [1, 1], [3, -1]
#     ]
#     [x, y]
# = [-x + 4y, x + y, 3x - y] \leq [16, 9, 15],\\
# & [0, 0] \leq [x, y] \leq [+\infty,+\infty] ,
# \end{align}
# $$

# Et donc avec Python cela sera :

# In[54]:


c = np.array([-4, -3])

A_ub = np.array([[-1, 4], [1, 1], [3, -1]])
b_ub = np.array([16, 9, 15])

A_eq = None
b_eq = None

# all variables are bound to be in (0, +inf)
bounds = (0, None)


# Objectif :

# In[55]:


import sympy
x, y = sympy.var('x y')


# In[56]:


c.T @ [x, y]


# Contraintes d'inéqualités :

# In[57]:


A_ub @ [x, y]


# In[58]:


b_ub


# ### Essayons avec différentes méthodes de résolution :

# #### Avec la méthode du simplexe

# In[97]:


list_of_x, list_of_fun, debug_callback = make_callback()

opt.linprog(c,
            A_ub=A_ub, b_ub=b_ub,
            A_eq=A_eq, b_eq=b_eq,
            bounds=bounds,
            method="simplex",
            callback=debug_callback,
)


# In[98]:


plt.figure(figsize=(10, 7))
plt.title("Valeur de l'objectif étape par étape")
plt.plot(list_of_fun, "ro-", lw=3, ms=14)
plt.show()


# In[99]:


plt.figure(figsize=(10, 7))
plt.title("Position des points étape par étape")
list_of_X, list_of_Y = [x for (x,y) in list_of_x], [y for (x,y) in list_of_x]
# plt.plot(list_of_X, list_of_Y, 'bo-')
plt.plot(list_of_X, 'bo-', label="Valeur de x", lw=3, ms=14)
plt.plot(list_of_Y, 'gd-', label="Valeur de y", lw=3, ms=14)
plt.legend()
plt.show()


# #### Avec la méthode du simplexe

# In[100]:


list_of_x, list_of_fun, debug_callback = make_callback()

opt.linprog(c,
            A_ub=A_ub, b_ub=b_ub,
            A_eq=A_eq, b_eq=b_eq,
            bounds=bounds,
            method="interior-point",
            callback=debug_callback,
)


# In[101]:


plt.figure(figsize=(10, 7))
plt.title("Valeur de l'objectif étape par étape")
plt.plot(list_of_fun, "ro-", lw=3, ms=14)
plt.show()


# In[102]:


plt.figure(figsize=(10, 7))
plt.title("Position des points étape par étape")
list_of_X, list_of_Y = [x for (x,y) in list_of_x], [y for (x,y) in list_of_x]
# plt.plot(list_of_X, list_of_Y, 'bo-')
plt.plot(list_of_X, 'bo-', label="Valeur de x", lw=3, ms=14)
plt.plot(list_of_Y, 'gd-', label="Valeur de y", lw=3, ms=14)
plt.legend()
plt.show()


# ----
# ## Implémentation manuelle de l'algorithme du simplexe

# Je devrais essayer, si j'ai le temps

# ## Conclusion
# 
# C'est bon pour aujourd'hui !
