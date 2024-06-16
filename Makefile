VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
UNITTEST = $(VENV)/bin/unittest

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

install: $(VENV)/bin/activate

test: $(VENV)/bin/activate
	$(UNITTEST)

run: $(VEN)/bin/activate
	$(PYTHON) app.py
