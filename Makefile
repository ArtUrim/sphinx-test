MARP = $(HOME)/bin/marp
README = "README.md"

upload: build
	python3 -m twine upload dist/*

build: 
	python3 setup.py sdist bdist_wheel

html:
	$(MARP) $(README)

pdf:
	$(MARP) --pdf $(README)

pptx:
	$(MARP) --pptx $(README)

all_doc: html pdf pptx

all: upload all_doc

clean:
	rm -Rf *.pdf *.pptx *.html dist/ src/sphinx_test_cases.egg-info/ build/
