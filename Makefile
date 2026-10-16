PYTHON ?= python3

.PHONY: test python lean all

test: all

python:
	$(PYTHON) -m pytest tests/python -vv

lean:
	lake update
	lake build

all: python lean
