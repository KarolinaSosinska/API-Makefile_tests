VENV = venv
PYTHON = $(VENV)/Scripts/python.exe
PIP = $(VENV)/Scripts/pip.exe
UNITTEST = $(PYTHON) -m unittest

$(VENV)/bin/activate: requirements.txt
	python -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

install: $(VENV)/Scripts/activate

test: install
	$(UNITTEST)

run: install
	$(PYTHON) app.py
