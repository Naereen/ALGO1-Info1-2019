#!/usr/bin/env python
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#ALGO1-:-Introduction-à-l'algorithmique" data-toc-modified-id="ALGO1-:-Introduction-à-l'algorithmique-1"><span class="toc-item-num">1&nbsp;&nbsp;</span><a href="https://perso.crans.org/besson/teach/info1_algo1_2019/" target="_blank">ALGO1 : Introduction à l'algorithmique</a></a></div><div class="lev1 toc-item"><a href="#Cours-Magistral-2" data-toc-modified-id="Cours-Magistral-2-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Cours Magistral 2</a></div><div class="lev2 toc-item"><a href="#Structures-de-données-pour-représenter-un-ensemble-de-valeurs-distinctes" data-toc-modified-id="Structures-de-données-pour-représenter-un-ensemble-de-valeurs-distinctes-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Structures de données pour représenter un ensemble de valeurs distinctes</a></div><div class="lev2 toc-item"><a href="#Type-abstrait" data-toc-modified-id="Type-abstrait-22"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Type abstrait</a></div><div class="lev2 toc-item"><a href="#Implémentation-des-opérations-non-primitives-à-partir-des-opérations-primitives" data-toc-modified-id="Implémentation-des-opérations-non-primitives-à-partir-des-opérations-primitives-23"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Implémentation des opérations non primitives à partir des opérations primitives</a></div><div class="lev2 toc-item"><a href="#Tests-communs-aux-différentes-implémentations" data-toc-modified-id="Tests-communs-aux-différentes-implémentations-24"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Tests communs aux différentes implémentations</a></div><div class="lev2 toc-item"><a href="#Implémentation-naïve-avec-une-structure-linéaire-(liste,-tableau-etc)" data-toc-modified-id="Implémentation-naïve-avec-une-structure-linéaire-(liste,-tableau-etc)-25"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Implémentation naïve avec une structure linéaire (liste, tableau etc)</a></div><div class="lev2 toc-item"><a href="#Implémentation-native-avec-set-en-Python" data-toc-modified-id="Implémentation-native-avec-set-en-Python-26"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>Implémentation native avec <code>set</code> en Python</a></div><div class="lev2 toc-item"><a href="#Bidouillage-1/1-:-implémentation-avec-des-entiers-32/64-bits" data-toc-modified-id="Bidouillage-1/1-:-implémentation-avec-des-entiers-32/64-bits-27"><span class="toc-item-num">2.7&nbsp;&nbsp;</span>Bidouillage 1/1 : implémentation avec des entiers 32/64 bits</a></div><div class="lev2 toc-item"><a href="#Bidouillage-2/2-:-implémentation-avec-des-entiers-en-précision-infinie-avec-Python" data-toc-modified-id="Bidouillage-2/2-:-implémentation-avec-des-entiers-en-précision-infinie-avec-Python-28"><span class="toc-item-num">2.8&nbsp;&nbsp;</span>Bidouillage 2/2 : implémentation avec des entiers en précision infinie avec Python</a></div><div class="lev2 toc-item"><a href="#Implémentation-avec-des-tables-de-hachage-?" data-toc-modified-id="Implémentation-avec-des-tables-de-hachage-?-29"><span class="toc-item-num">2.9&nbsp;&nbsp;</span>Implémentation avec des tables de hachage ?</a></div><div class="lev2 toc-item"><a href="#Implémentation-avec-des-arbres-binaires-de-recherche-?" data-toc-modified-id="Implémentation-avec-des-arbres-binaires-de-recherche-?-210"><span class="toc-item-num">2.10&nbsp;&nbsp;</span>Implémentation avec des arbres binaires de recherche ?</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-211"><span class="toc-item-num">2.11&nbsp;&nbsp;</span>Conclusion</a></div>

# # [ALGO1 : Introduction à l'algorithmique](https://perso.crans.org/besson/teach/info1_algo1_2019/)
# 
# - [Page du cours](https://perso.crans.org/besson/teach/info1_algo1_2019/) : https://perso.crans.org/besson/teach/info1_algo1_2019/
# - Magistère d'Informatique de Rennes - ENS Rennes - Année 2019/2020
# - Intervenants :
#   + Cours : [Lilian Besson](https://perso.crans.org/besson/)
#   + Travaux dirigés : [Raphaël Truffet](http://perso.eleves.ens-rennes.fr/people/Raphael.Truffet/)
# - Références :
#   + [Open Data Structures](http://opendatastructures.org/ods-python.pdf)

# # Cours Magistral 2

# ## Structures de données pour représenter un ensemble de valeurs distinctes
# 
# - Après avoir étudié comment représenter $<a_1,\dots,a_n>$ une *séquence ordonnée* de valeurs $a_i$ dans un domaine $D$ (e.g., des entiers), on s'intéresse aujourd'hui à représenter un *ensemble non ordonné* de valeurs : $\{a_1,\dots,a_n\}$.
# - On va utiliser des valeurs entières, par concision : $D=\mathbb{N}$, `d = int`.

# ## Type abstrait
# - On fixe $D$ le domaine de nos valeurs, et `d` leur type.
# - On définit `Set<d>` le type abstrait des ensembles (collections non ordonnés) de valeurs de type `d`.
# 
# On veut les opérations suivantes :
# 
#     newEmptySet : () -> Set<d>          // créer un ensemble vide
#     len         : Set<d> -> int         // donner le nombre d'éléments de cet ensemble
#     contains    : Set<d> * d -> bool    // tester l'appartenance
#     add         : Set<d> * d -> Set<d>  // ajouter un élément à cet ensemble
#     pop         : Set<d> * d -> Set<d>  // retirer un élément à cet ensemble (s'il est présent)
#     values      : Set<d> -> List<d>     // retourne la liste de valeurs présentes dans l'ensemble

# On peut aussi vouloir les opérations suivantes, qui peuvent toutes s'implémenter avec les primitives ci-dessus :
# 
#     isEmpty : Set<d> -> bool    // test si l'ensemble est vide
#     copy    : Set<d> -> Set<d>  // copie l'ensemble
# 
# On peut aussi vouloir les opérations entre ensembles suivantes, qui peuvent toutes s'implémenter avec les primitives ci-dessus :
# 
#     union                : Set<d> * Set<d> -> Set<d>
#     // contient les éléments présents dans au moins un des deux ensembles
#     
#     intersection         : Set<d> * Set<d> -> Set<d>
#     // contient les éléments présents dans les deux ensembles
#     
#     difference           : Set<d> * Set<d> -> Set<d>
#     // contient les éléments présents dans le premier mais pas le deuxième ensemble
#     
#     symmetric_difference : Set<d> * Set<d> -> Set<d>
#     // contient les éléments présents dans le premier mais pas le deuxième ensemble ou dans le deuxième mais pas le premier (xor)
#     
#     issubset             : Set<d> * Set<d> -> bool
#     // test si le premier ensemble est contenu dans le second
#     
#     issuperset           : Set<d> * Set<d> -> bool
#     // test si le premier ensemble est contenu dans le second

# ## Implémentation des opérations non primitives à partir des opérations primitives
# - Avec OCaml, on pourrait écrire un foncteur.
# - Avec Python, on va écrire une classe, et on pourra obtenir différentes implémentations complètes de la structure de données d'ensemble, à partir de différentes implémentations partielles des opérations primitives. C'est assez naïf : le code est indépendant de l'implémentation sous jacente de `add`/`pop` et de l'itérations :

# In[58]:


class SetIterator():
    def __init__(self, a_set):
        self.values = a_set.values()
        self.maxcurrent = len(a_set)
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.maxcurrent:
            raise StopIteration
        else:
            self.current += 1
            return self.values[self.current - 1]


# In[63]:


class SetWithNonPrimOperations():
    def isEmpty(self):
        return len(self) == 0

    def __iter__(self):
        return SetIterator(self)
    
    def copy(self):
        """ A new set containing the same values."""
        new_set = self.__class__()
        for value in self:
            new_set.add(value)
        return new_set
    
    def difference(self, other_set):
        """ A new set containing the values in self but not other_set."""
        new_set = self.__class__()
        for value in self:
            if value not in other_set:
                new_set.add(value)
        return new_set
    
    def symmetric_difference(self, other_set):
        """ A new set containing the values in self but not other_set and the values in other_set but not self (XOR)."""
        new_set = self.__class__()
        for value in self:
            if value not in other_set:
                new_set.add(value)
        for value in other_set:
            if value not in self:
                new_set.add(value)
        return new_set
    
    def intersection(self, other_set):
        """ A new set containing the values in self and in other_set."""
        new_set = self.__class__()
        for value in self:
            if value in other_set:
                new_set.add(value)
        return new_set
    
    def union(self, other_set):
        """ A new set containing the values in self or in other_set."""
        new_set = self.__class__()
        for value in self:
            new_set.add(value)
        for value in other_set:
            new_set.add(value)
        return new_set

    def isdisjoint(self, other_set):
        """ True if all the values in self are not in other_set."""
        for value in self:
            if value in other_set:
                return False
        return True

    def issubset(self, other_set):
        """ True if all the values in self are in other_set."""
        for value in self:
            if value not in other_set:
                return False
        return True

    def issuperset(self, other_set):
        """ True if all the values in other_set are in self."""
        for value in other_set:
            if value not in self:
                return False
        return True

    def clear(self):
        """ Remove (pop) all the values in self."""
        for value in self:
            self.pop(value)
    
    def __str__(self):
        """ Represent the values of the set in a string {a1,...,an}."""
        str_list = str(self.values())
        return "{" + str_list.strip("[]") + "}"


# ## Tests communs aux différentes implémentations

# In[64]:


def un_petit_test_avec_une_structure_densemble(SetClass):
    ens = SetClass()
    print(ens)
    assert not ens
    for x in range(10):
        assert x not in ens
        ens.add(x)
        assert x in ens
        print(ens)
    # ens = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    assert ens
    assert str(ens) == "{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}"
    print("S1 =", ens)
    for x in range(20, 30):
        assert x not in ens
    
    ens2 = SetClass()
    print(ens2)
    for x in range(5, 10):
        assert x not in ens2
        ens2.add(x)
        assert x in ens2
        print(ens2)
    # ens2 = {5, 6, 7, 8, 9}
    assert str(ens2) == "{5, 6, 7, 8, 9}"
    print("S2 =", ens2)
    assert ens2.issubset(ens)
    assert ens.issuperset(ens2)
    
    assert [v for v in ens.intersection(ens2)] == [v for v in ens2]
    assert [v for v in ens.intersection(ens2)] == [5, 6, 7, 8, 9]
    assert [v for v in ens.difference(ens2)] == [0, 1, 2, 3, 4]
    
    ens3 = SetClass()
    print(ens3)
    for x in range(20, 25):
        assert x not in ens3
        ens3.add(x)
        assert x in ens3
        print(ens3)
    assert len(ens3) == 5
    for x in range(20, 25):
        ens3.add(x)
        assert x in ens3
        print(ens3)
    assert len(ens3) == 5
    # ens3 = {20, 21, 22, 23, 24}
    assert str(ens3) == "{20, 21, 22, 23, 24}"
    print("S3 =", ens3)

    assert not ens.issubset(ens3)
    assert not ens.issuperset(ens3)
    assert not ens3.issubset(ens)
    assert not ens3.issuperset(ens)
    
    assert not ens3.intersection(ens)
    assert not ens.intersection(ens3)
    
    print("S1 union S2 =", ens.union(ens2), " = S2 union S1 =", ens2.union(ens))
    print("S1 union S3 =", ens.union(ens3))
    print("S2 union S3 =", ens2.union(ens3))

    print("S1 inter S2 =", ens.intersection(ens2), " != S2 inter S1 =", ens2.intersection(ens))
    print("S1 inter S3 =", ens.intersection(ens3), " != S3 inter S1 =", ens3.intersection(ens))
    print("S2 inter S3 =", ens2.intersection(ens3), " != S3 inter S2 =", ens3.intersection(ens2))

    print("S1 diff S2 =", ens.difference(ens2), " != S2 diff S1 =", ens2.difference(ens))
    print("S1 diff S3 =", ens.difference(ens3), " != S3 diff S1 =", ens3.difference(ens))
    print("S2 diff S3 =", ens2.difference(ens3), " != S3 diff S2 =", ens3.difference(ens2))

    print("S1 diff sym S2 =", ens.symmetric_difference(ens2), " != S2 diff sym S1 =", ens2.symmetric_difference(ens))
    print("S1 diff sym S3 =", ens.symmetric_difference(ens3), " != S3 diff sym S1 =", ens3.symmetric_difference(ens))
    print("S2 diff sym S3 =", ens2.symmetric_difference(ens3), " != S3 diff sym S2 =", ens3.symmetric_difference(ens2))
    


# ## Implémentation naïve avec une structure linéaire (liste, tableau etc)
# - On utilise une liste ou un tableau (en Python, `list<d>`) pour stocker les valeurs.
# - Voyons les implémentations concrètes (les complexités sont discutées pour chacune plus bas).

# In[65]:


class SetWithList(SetWithNonPrimOperations):
    def __init__(self):
        self._values = []

    def __len__(self):
        """ Return n the current size of the set."""
        return len(self._values)

    def contains(self, value):
        """ Test if value is in the set.
        
        - Test linearly the equality with all values in the list.
        - Takes O(n) time in worst case."""
        for other_value in self._values:
            if other_value == value:
                return True
        return False
        # equivalent to
        # return value in self._values
    __contains__ = contains

    def add(self, value):
        """ Add value in the set if it is not present.
        
        - Takes O(n) time in worst case."""
        if value not in self:
            self._values.append(value)

    def pop(self, value):
        """ Add value in the set if it is not present.
        
        - Takes O(n) time in worst case."""
        if value in self:  # O(n)
            location = self._values.index(value)  # O(n), but happens only once
            del self._values[location]  # O(n)
    
    def values(self):
        """ Return a fresh list of the values of the set (not the actual list, to protect it).
        
        - Takes O(n) time in worst case."""
        return list(self._values)


# On test :

# In[66]:


un_petit_test_avec_une_structure_densemble(SetWithList)


# - On pourrait faire pareil avec n'importe quelle structure linéaire : liste simplement ou doublement chaînée, tableau dynamique (ce qu'on a fait avec `list` de Python), file/pile d'attente, etc.
# 
# - Le bilan des complexités des opérations est le suivant (si $n=\texttt{len}(S_1)$ et $m=\texttt{len}(S_2)$) :
# 
# | Opérations | Complexité pire cas | Complexité moyenne* |
# |------------|------------|------------|
# | `newEmptySet()` | $O(1)$ | $O(1)$ |
# | `len(S1)` | $O(n)$ | $O(n)$ |
# | `contains(S1, x)` | $O(n)$ | $O(n)$ |
# | `add(S1, x)` | $O(n)$ | $O(n)$ |
# | `pop(S1, x)` | $O(n)$ | $O(n)$ |
# | `values(S1)` | $O(n)$ | $O(n)$ |
# | `isEmpty(S1)` | $O(n)$ | $O(n)$ |
# | `copy(S1)` | $O(n)$ | $O(n)$ |
# | `union(S1, S2)` | $O(n + m)$ | $O(n + m)$ |
# | `intersection(S1, S2)` | $O(n + m)$ | $O(n + m)$ |
# | `difference(S1, S2)` | $O(n + m)$ | $O(n + m)$ |
# | `symmetric_difference(S1, S2)` | $O(n + m)$ | $O(n + m)$ |
# | `issubset(S1, S2)` | $O(n + m)$ | $O(n + m)$ |
# | `issuperset(S1, S2)` | $O(n + m)$ | $O(n + m)$ |
# 
# > Il reste à définir ce que signifie complexité moyenne. Regardez par exemple dans [Introduction à l'Algorithmique, de Cormen et al].

# ## Implémentation native avec `set` en Python

# In[31]:


NativeSet = set  # et c'est tout


# In[38]:


un_petit_test_avec_une_structure_densemble(NativeSet)


# - Le bilan des complexités des opérations est le suivant (si $n=\texttt{len}(S_1)$ et $m=\texttt{len}(S_2)$) :
# 
# | Opérations | Complexité pire cas | Complexité moyenne* |
# |------------|------------|------------|
# | `newEmptySet()` | $O(1)$ | $O(1)$ |
# | `len(S1)` | $O(1)$ | $O(1)$ |
# | `contains(S1, x)` | $O(n)$ | $O(1)$ 🎉 |
# | `add(S1, x)` | $O(n)$ | $O(1)$ 🎉 |
# | `pop(S1, x)` | $O(n)$ | $O(1)$ 🎉 |
# | `values(S1)` | $O(n)$ | $O(n)$ |
# | `isEmpty(S1)` | $O(1)$ | $O(1)$ |
# | `copy(S1)` | $O(n)$ | $O(n)$ |
# | `union(S1, S2)` | $O(n + m)$ | $O(n + m)$ |
# | `intersection(S1, S2)` | $O(n m)$ | $O(\min(n, m))$ 🎉 |
# | `difference(S1, S2)` | $O(n + m)$ | $O(n + m)$ |
# | `symmetric_difference(S1, S2)` | $O(n m)$ | $O(\max(n, m))$ |
# | `issubset(S1, S2)` | $O(n m)$ | $O(\min(n, m)))$ 🎉 |
# | `issuperset(S1, S2)` | $O(n m)$ | $O(\min(n, m)))$ 🎉 |
# 
# > Référence : https://stackoverflow.com/questions/3949310/ddg#3949350, https://hg.python.org/releasing/3.6/file/tip/Objects/setobject.c et https://wiki.python.org/moin/TimeComplexity#set

# ## Bidouillage 1/1 : implémentation avec des entiers 32/64 bits
# 
# - Si on sait que les valeurs qu'on va ajouter dans nos ensembles sont comprises entre 0 et 31, on peut représenter un (petit) ensemble avec *un seul* entier 32 bits : si le $i$ème bit est à 1, c'est que $i$ est dans l'ensemble.
# - On peut faire pareil avec 64 bits.
# - En Python, les entiers sont à précision arbitraire, mais on peut utiliser `np.int32` pour avoir des entiers 32 bits natifs :

# In[68]:


import numpy as np


# - On va voir comment utiliser les opérations bit à bit pour réaliser les opérations sur les ensembles. [Documentation ?](https://docs.scipy.org/doc/numpy/reference/routines.bitwise.html)

# In[74]:


i32 = np.int32
i64 = np.int64


# In[101]:


bin(0b0)  # set {}
bin(0b1)  # set {0}
bin(0b10)  # set {1}
bin(0b11)  # set {0, 1}

bin(np.bitwise_and(0b11, 0b01))  # {0, 1} inter {1} = {1}
bin(0b11 & 0b01)  # {0, 1} inter {1} = {1}
bin(np.bitwise_or(0b01, 0b10))  # {0} union {1} = {0, 1}
bin(0b01 | 0b10)  # {0} union {1} = {0, 1}

bin(np.bitwise_xor(0b11, 0b10)) # {0, 1} /\ {1} = {0} (symmetric difference)
bin(0b11 ^ 0b10) # {0, 1} /\ {1} = {0} (symmetric difference)
bin(np.bitwise_xor(0b101, 0b10)) # {0, 2} /\ {1} = {0, 1, 2} (symmetric difference)
bin(0b101 ^ 0b10) # {0, 2} /\ {1} = {0, 1, 2} (symmetric difference)
bin(np.bitwise_xor(0b11, 0b10)) # {1} - {0} = {}
bin(0b11 ^ 0b10) # {1} - {0} = {}

bin(np.left_shift(1, 0))  # = {0}
bin(1 << 0)  # = {0}
bin(np.left_shift(1, 1))  # = {1}
bin(1 << 1)  # = {1}
bin(np.left_shift(1, 7))  # = {7}
bin(1 << 7)  # = {7}


# Et voilà la classe

# In[102]:


class SetWithInt(SetWithNonPrimOperations):
    def __init__(self, dataType):
        self._dataType = dataType
        self.int = dataType(0)

    def __len__(self):
        """ Return n the current size of the set."""
        return len(self._values)

    def contains(self, value):
        """ Test if value is in the set.
        
        - Test linearly the equality with all values in the list.
        - Takes O(n) time in worst case."""
        for other_value in self._values:
            if other_value == value:
                return True
        return False
        # equivalent to
        # return value in self._values
    __contains__ = contains

    def add(self, value):
        """ Add value in the set if it is not present.
        
        - Takes O(n) time in worst case."""
        if value not in self:
            self._values.append(value)

    def pop(self, value):
        """ Add value in the set if it is not present.
        
        - Takes O(n) time in worst case."""
        if value in self:  # O(n)
            location = self._values.index(value)  # O(n), but happens only once
            del self._values[location]  # O(n)
    
    def values(self):
        """ Return a fresh list of the values of the set (not the actual list, to protect it).
        
        - Takes O(n) time in worst case."""
        return list(self._values)


# In[ ]:


SetWithInt32 = SetWithInt(np.int32)
SetWithInt64 = SetWithInt(np.int64)


# On test :

# In[66]:


un_petit_test_avec_une_structure_densemble(SetWithInt32)


# Parler de complexité n'aura pas de sens ici : on s'autorise seulement des ensembles ayant jusqu'à 32 valeurs.
# Donc $n\leq32$, alors que les notations $O(n)$ (etc) sont des **notations asymptotiques** (ie. valables quand $n\to\infty$ !).

# ## Bidouillage 2/2 : implémentation avec des entiers en précision infinie avec Python

# In[ ]:


SetWithIntInfinite = SetWithInt(int)


# In[ ]:


un_petit_test_avec_une_structure_densemble(SetWithIntInfinite)


# ## Implémentation avec des tables de hachage ?

# In[ ]:





# In[ ]:





# ## Implémentation avec des arbres binaires de recherche ?

# In[ ]:





# ## Conclusion
# 
# C'est bon pour aujourd'hui !

# In[ ]:




