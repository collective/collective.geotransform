#!/usr/bin/make
#
all: run

BUILDOUT_FILES = bin/buildout buildout.cfg

.PHONY: buildout run test cleanall
bin/buildout: buildout.cfg
	python3.9 -m venv .
	./bin/pip install -r requirements.txt
	touch $@

buildout: bin/buildout
	bin/buildout -t 5

run: bin/instance 
	bin/instance fg

bin/instance: $(BUILDOUT_FILES)
	bin/buildout -t 5
	touch $@

test: bin/test
	rm -fr htmlcov
	bin/test

bin/test: $(BUILDOUT_FILES)
	bin/buildout -t 5
	touch $@

cleanall:
	rm -fr bin develop-eggs htmlcov include .installed.cfg lib .mr.developer.cfg parts downloads eggs
