# Makefile to convert Jupyter notebooks to HTML pages
SHELL=/usr/bin/env /bin/bash

all:	send

send:	send_zamok
send_zamok:
	CP --exclude=.ipynb_checkpoints --exclude=.git *.ipynb *.py *.html *.pdf figures README.md LICENSE.txt ${Szam}teach/info1_algo1_2019/notebooks/

export:
	./export.sh

CONTENT_IPYNB=$(wildcard *.ipynb */*.ipynb)
CONTENT_HTML=$(CONTENT_IPYNB:.ipynb=.html)

list_nb:
	echo $(CONTENT_IPYNB)
list_html:
	echo $(CONTENT_HTML)

html_notebooks:	$(CONTENT_HTML)

%.html:	%.ipynb
	jupyter-nbconvert "$<" --to html
