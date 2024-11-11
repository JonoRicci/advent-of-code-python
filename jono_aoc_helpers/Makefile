# Python virtual environment paths
VENV_DIR = .venv
PYTHON = $(VENV_DIR)/bin/python

# Pyenv version paths
PYTHON_VERSION_FILE = .python-version
PYTHON_VERSION = $(shell cat $(PYTHON_VERSION_FILE) 2>/dev/null)

# Current Python version
CURRENT_PYTHON_VERSION = $(shell $(PYTHON) --version 2>/dev/null | cut -d ' ' -f2)

# Initialize environment: create venv and install dependencies
.PHONY: init
init: check_python_version venv dependencies activate

# Check Python version from .python-version file and install if necessary
.PHONY: check_python_version
check_python_version:
	@if [ -f "$(PYTHON_VERSION_FILE)" ]; then \
		echo "⚙️ Checking Python version from $(PYTHON_VERSION_FILE)."; \
		echo "ℹ️ $(PYTHON_VERSION_FILE) is $(PYTHON_VERSION)"; \
		if ! pyenv versions --bare | grep -q "^$(PYTHON_VERSION)$$"; then \
			echo "⚙️ Python version $(PYTHON_VERSION) not found. Installing."; \
			pyenv install $(PYTHON_VERSION); \
		fi; \
		pyenv local $(PYTHON_VERSION); \
	else \
		echo "❌ .python-version file not found. Please create one or ensure the correct Python version is installed."; \
		exit 1; \
	fi

# Check if the virtual environment exists, and create it if not
.PHONY: venv
venv:
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "⚙️ Creating virtual environment."; \
		python -m venv $(VENV_DIR); \
	else \
		echo "✅ Virtual environment already exists."; \
	fi

# Install or update dependencies from requirements.txt
.PHONY: dependencies
dependencies:
	@if [ -f requirements.txt ]; then \
		echo "⚙️ Installing/updating dependencies."; \
		$(PYTHON) -m pip install -r requirements.txt; \
	else \
		echo "ℹ️ No requirements.txt found. Skipping dependency installation."; \
	fi

# Shortcut to activate the virtual environment
.PHONY: activate
activate:
	@echo "📖 To activate the virtual environment, run: source .venv/bin/activate"
	@echo "📖 To deactivate, run: deactivate"

# Clean up build artifacts and the virtual environment
.PHONY: clean
clean:
	rm -rf $(VENV_DIR)
	rm -rf __pycache__
	rm -rf *.egg-info
	@echo "✅ Removed venv directory and pycache."

# Start development
.PHONY: setup
setup: init
	@echo "✅ Development environment ready to go!"
