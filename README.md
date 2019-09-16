# ALGO1 : Introduction à l'algorithmique

- Magistère d'Informatique de Rennes - ENS Rennes - Année 2019/2020
- Intervenants :
  + Cours : [Lilian Besson](https://perso.crans.org/besson/)
  + Travaux dirigés : [Raphaël Truffet](http://perso.eleves.ens-rennes.fr/people/Raphael.Truffet/)

----

## Information à propos de ce cours

C'est en ligne, sur [cette page](https://perso.crans.org/besson/teach/info1_algo1_2019/) (`https://perso.crans.org/besson/teach/info1_algo1_2019/`).

- Liste des notebooks : [cette page](https://perso.crans.org/besson/teach/info1_algo1_2019/notebooks/) (`https://perso.crans.org/besson/teach/info1_algo1_2019/notebooks/`), [sur NBViewer (passif)](https://nbviewer.jupyter.org/github/Naereen/ALGO1-Info1-2019/tree/master/), [sur Binder (interactif)](https://beta.mybinder.org/v2/gh/Naereen/ALGO1-Info1-2019/master).

[![MyBinder v2](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Naereen/ALGO1-Info1-2019/master)

## Liste de notebooks

### Cours 1 : Introduction + File de priorité
- [CoursMagistral_1.ipynb](CoursMagistral_1.ipynb)
- (aussi [en python](CoursMagistral_1.py) et [en HTML](CoursMagistral_1.html))

### Cours 2 : Structures de données pour un ensemble
- [CoursMagistral_2.ipynb](CoursMagistral_2.ipynb)
- (aussi [en python](CoursMagistral_1.py) et [en HTML](CoursMagistral_1.html))

### Cours 3 : Diviser pour régner
- TODO : [CoursMagistral_3.ipynb](CoursMagistral_3.ipynb)
- (aussi [en python](CoursMagistral_1.py) et [en HTML](CoursMagistral_1.html))

### Cours 4 : Graphes, et parcours en profondeur
- TODO : [CoursMagistral_4.ipynb](CoursMagistral_4.ipynb)
- (aussi [en python](CoursMagistral_1.py) et [en HTML](CoursMagistral_1.html))

### Cours 5 : Parcours en largeur
- TODO : [CoursMagistral_5.ipynb](CoursMagistral_5.ipynb)
- (aussi [en python](CoursMagistral_1.py) et [en HTML](CoursMagistral_1.html))

### Cours 6 : Algorithmes gloutons
- TODO : [CoursMagistral_6.ipynb](CoursMagistral_6.ipynb)
- (aussi [en python](CoursMagistral_1.py) et [en HTML](CoursMagistral_1.html))

### Cours 7 : Programmation dynamique
- TODO : [CoursMagistral_7.ipynb](CoursMagistral_7.ipynb)
- (aussi [en python](CoursMagistral_1.py) et [en HTML](CoursMagistral_1.html))

### Cours 8 : Flots
- TODO : [CoursMagistral_8.ipynb](CoursMagistral_8.ipynb)
- (aussi [en python](CoursMagistral_1.py) et [en HTML](CoursMagistral_1.html))

### Cours 9 : Programmation linéaire
- TODO : [CoursMagistral_9.ipynb](CoursMagistral_9.ipynb)
- (aussi [en python](CoursMagistral_1.py) et [en HTML](CoursMagistral_1.html))

### Cours 10 : Algorithmes de recherche de solutions
- TODO : [CoursMagistral_10.ipynb](CoursMagistral_10.ipynb)
- (aussi [en python](CoursMagistral_1.py) et [en HTML](CoursMagistral_1.html))

----

## 1. *How to read these documents*?

### 1.a. View the notebooks statically :memo:
- Either directly in GitHub: [see the list of notebooks](https://github.com/Naereen/ALGO1-Info1-2019/search?l=jupyter-notebook);
- Or on [nbviewer.jupiter.org](https://nbviewer.jupiter.org/): [list of notebooks](https://nbviewer.jupyter.org/github/Naereen/ALGO1-Info1-2019/tree/master/).

### 1.b. Play with the notebooks dynamically :boom:
[![MyBinder](http://mybinder.org/badge.svg)](http://mybinder.org/repo/Naereen/ALGO1-Info1-2019)

Anyone can use the [mybinder.org](http://mybinder.org/) website (by [clicking](http://mybinder.org/repo/Naereen/ALGO1-Info1-2019) on the icon above) to run the notebook in her/his web-browser.
You can then play with it as long as you like, for instance by modifying the values or experimenting with the code.

[![MyBinder v2](https://beta.mybinder.org/badge.svg)](https://beta.mybinder.org/v2/gh/Naereen/ALGO1-Info1-2019/master)

> *Note:* Only the Python kernel is supported on the MyBinder interface!

----

## 2. *Requirements to run the notebooks locally*?
All [the requirements](requirements.txt) can be installed with [``pip``](https://pip.readthedocs.io/) and by running a few ``python -m ...`` commands.

> Note: if you use [Python 3](https://docs.python.org/3/) instead of [Python 2](https://docs.python.org/2/), you *might* have to *replace* ``pip`` and ``python`` by ``pip3`` and ``python3`` in the next commands (if both pip and pip3 are installed).

### 2.a. [Jupyter Notebook](http://jupyter.readthedocs.org/en/latest/install.html) and [IPython](http://ipython.org/)

```bash
sudo pip install jupyter ipython
```

It will also install all the dependencies, afterward you should have a ``jupyter-notebook`` command (or a ``jupyter`` command, to be ran as ``jupyter notebook``) available in your ``PATH``:

```bash
$ whereis jupyter-notebook
jupyter-notebook: /usr/local/bin/jupyter-notebook
$ jupyter-notebook --version  # version >= 4 is recommended
4.2.1
```

----

### :information_desk_person: More information?
> - More information about [notebooks (on the documentation of IPython)](https://nbviewer.jupiter.org/github/ipython/ipython/blob/3.x/examples/Notebook/Index.ipynb) or [on the FAQ on Jupyter's website](https://nbviewer.jupyter.org/faq).
> - More information about [mybinder.org](http://mybinder.org/): on [this example repository](https://github.com/binder-project/example-requirements).

## :scroll: License ? [![GitHub license](https://img.shields.io/github/license/Naereen/ALGO1-Info1-2019.svg)](https://github.com/Naereen/ALGO1-Info1-2019/blob/master/LICENSE.txt)
All the notebooks in this repository are published under the terms of the [MIT License](https://lbesson.mit-license.org/) (file [LICENSE.txt](LICENSE.txt)).
© [Lilian Besson](https://GitHub.com/Naereen), 2019.

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/ALGO1-Info1-2019/graphs/commit-activity)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/Naereen/ama)
[![Analytics](https://ga-beacon.appspot.com/UA-38514290-17/github.com/Naereen/ALGO1-Info1-2019/README.md?pixel)](https://GitHub.com/Naereen/ALGO1-Info1-2019/)

[![made-with-jupyter](https://img.shields.io/badge/Made%20with-Jupyter-1f425f.svg)](http://jupyter.org/) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![made-with-ocaml](https://img.shields.io/badge/Made%20with-OCaml-1f425f.svg)](https://ocaml.org/)
[![ForTheBadge uses-badges](http://ForTheBadge.com/images/badges/uses-badges.svg)](http://ForTheBadge.com)
[![ForTheBadge uses-git](http://ForTheBadge.com/images/badges/uses-git.svg)](https://GitHub.com/)
[![ForTheBadge built-with-science](http://ForTheBadge.com/images/badges/built-with-science.svg)](https://GitHub.com/Naereen/)
