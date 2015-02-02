#!/usr/bin/make
#
all: run

BUILDOUT_FILES = bin/buildout buildout.cfg

bootstrap.py:
	wget http://downloads.buildout.org/2/bootstrap.py

.PHONY: bootstrap buildout run test cleanall
bin/buildout: bootstrap.py buildout.cfg
	virtualenv-2.7 .
	./bin/python bootstrap.py 
	touch $@

buildout: bin/buildout
	bin/buildout -t 5

bootstrap: bin/buildout

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
