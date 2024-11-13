# Python virtual environment paths
VENV_DIR = .venv
PYTHON = $(VENV_DIR)/bin/python

# Default goal
.DEFAULT_GOAL := init

# Pyenv version paths
PYTHON_VERSION_FILE = .python-version
PYTHON_VERSION = $(shell cat $(PYTHON_VERSION_FILE) 2>/dev/null)

# Check if pyenv is installed
.PHONY: check_pyenv_installed
check_pyenv_installed:
	@if ! command -v pyenv &> /dev/null; then \
		echo "❌ pyenv not found. Please install pyenv to manage Python versions:"; \
		echo "👉 https://github.com/pyenv/pyenv#installation"; \
		exit 1; \
	fi;

# Check Python version from .python-version file and install if necessary
.PHONY: check_python_version
check_python_version: check_pyenv_installed
	@if [ -f "$(PYTHON_VERSION_FILE)" ]; then \
		echo "⚙️ Checking Python version from $(PYTHON_VERSION_FILE)."; \
		echo "ℹ️ $(PYTHON_VERSION_FILE) is $(PYTHON_VERSION)"; \
		if [ "$(pyenv version-name)" != "$(PYTHON_VERSION)" ]; then \
			if ! pyenv versions --bare | grep -q "^$(PYTHON_VERSION)$$"; then \
				echo "⚙️ Python version $(PYTHON_VERSION) not found. Installing."; \
				pyenv install $(PYTHON_VERSION); \
			fi; \
			pyenv local $(PYTHON_VERSION); \
		else \
			echo "✅ Python version $(PYTHON_VERSION) is already active."; \
		fi; \
	else \
		echo "❌ .python-version file not found. Please create one using 'pyenv local <version>' or manually add it."; \
		exit 1; \
	fi

# Install or update dependencies from requirements.txt
.PHONY: dependencies
dependencies:
	@if [ -f requirements.txt ]; then \
		echo "⚙️ Installing/updating dependencies."; \
		$(PYTHON) -m pip install --upgrade pip setuptools; \
		$(PYTHON) -m pip install -r requirements.txt; \
	else \
		echo "ℹ️ No requirements.txt found. Skipping dependency installation."; \
	fi

# Upgrade dependencies from requirements.txt
.PHONY: dependencies-upgrade
dependencies-upgrade:
	@if [ -f requirements.txt ]; then \
		echo "⚙️ Installing/updating dependencies (forcing upgrade)."; \
		$(PYTHON) -m pip install --upgrade -r requirements.txt; \
	else \
		echo "ℹ️ No requirements.txt found. Skipping dependency installation."; \
	fi

# Generate requirements.txt from the current virtual environment
.PHONY: pip-freeze
generate-requirements:
	@echo "⚙️ Generating requirements.txt from the current environment."; \
	$(PYTHON) -m pip freeze > requirements.txt; \
	@echo "✅ requirements.txt has been successfully updated."

# Linting target using Black
.PHONY: lint
lint:
	$(PYTHON) -m black .

# Clean up build artifacts and the virtual environment
.PHONY: clean
clean:
	rm -rf $(VENV_DIR)
	rm -rf __pycache__
	rm -rf *.egg-info
	rm -rf dist
	rm -rf build
	rm -rf .pytest_cache
	@echo "✅ Removed build artifacts and the virtual environment."

# Shortcut to activate the virtual environment
.PHONY: activate
activate:
	@echo "📖 To activate the virtual environment, run: source .venv/bin/activate"
	@echo "📖 To deactivate, run: deactivate"

# Initialize environment: create venv and install dependencies
.PHONY: init
init: check_python_version venv dependencies activate

# Check if the virtual environment exists, and create it if not
.PHONY: venv
venv:
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "⚙️ Creating virtual environment."; \
		python -m venv $(VENV_DIR); \
	else \
		echo "✅ Virtual environment already exists."; \
	fi

# Start development
.PHONY: setup
setup: init
	@echo "✅ Development environment ready to go!"


# Create a new day directory based on the template
.PHONY: newday
newday:
	@if [ -z "$(DAY)" ]; then \
		echo "❌ Please provide the DAY argument. Usage: make newday DAY=<day_number>"; \
		exit 1; \
	fi; \
	DAY_DIR="day_$(DAY)"; \
	if [ -d "day_00_template" ]; then \
		echo "⚙️ Creating new directory for day $(DAY)."; \
		cp -r day_00_template $$DAY_DIR; \
		echo "✅ Created new day directory: $$DAY_DIR"; \
	else \
		echo "❌ day_00_template directory not found."; \
		exit 1; \
	fi
