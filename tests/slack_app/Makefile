SHELL := /bin/bash
PYTHON := python3
VENV_DIR := .venv
VENV_PY := $(VENV_DIR)/bin/python
VENV_PIP := $(VENV_DIR)/bin/pip

APP := app.py
REQ := requirements.txt
ENV := .env
ENV_EX := .env.example

.PHONY: setup run freeze clean check env certs help

help:
	@echo "Targets:"
	@echo "  make setup   - create venv and install deps"
	@echo "  make run     - run $(APP) with SSL certs from certifi"
	@echo "  make certs   - show certifi path (debug)"
	@echo "  make freeze  - pin deps to $(REQ)"
	@echo "  make check   - show Python/pip versions and paths"
	@echo "  make clean   - remove venv and caches"
	@echo "  make env     - create $(ENV) if missing"

$(VENV_DIR):
	@echo ">> Creating virtualenv in $(VENV_DIR)"
	$(PYTHON) -m venv $(VENV_DIR)

setup: $(VENV_DIR)
	@echo ">> Upgrading pip"
	$(VENV_PIP) install --upgrade pip
	@if [ -f "$(REQ)" ]; then \
		echo ">> Installing deps from $(REQ)"; \
		$(VENV_PIP) install -r $(REQ); \
	else \
		echo "!! $(REQ) not found. Creating with default deps..."; \
		echo "slack-bolt\npython-dotenv\ncertifi" > $(REQ); \
		$(VENV_PIP) install -r $(REQ); \
	fi
	@$(MAKE) env

certs:
	@[ -d "$(VENV_DIR)" ] || $(MAKE) setup
	@echo ">> certifi path:"
	@$(VENV_PY) -c 'import certifi; print(certifi.where())'

run:
	@[ -d "$(VENV_DIR)" ] || $(MAKE) setup
	@[ -f "$(APP)" ] || (echo "!! $(APP) not found" && exit 1)
	@echo ">> Running $(APP)"
	SSL_CERT_FILE="$$( $(VENV_PY) -c 'import certifi; print(certifi.where())' )" \
	$(VENV_PY) $(APP)

freeze:
	@[ -d "$(VENV_DIR)" ] || $(MAKE) setup
	@echo ">> Freezing deps to $(REQ)"
	$(VENV_PIP) freeze > $(REQ)

check:
	@echo ">> System Python:"
	@which $(PYTHON) || true
	@$(PYTHON) --version || true
	@echo ">> Venv Python:"
	@echo "$(VENV_PY)"
	@([ -x "$(VENV_PY)" ] && $(VENV_PY) --version) || echo "venv not yet created"
	@echo ">> Venv pip:"
	@echo "$(VENV_PIP)"
	@([ -x "$(VENV_PIP)" ] && $(VENV_PIP) --version) || echo "venv not yet created"

clean:
	@echo ">> Removing venv and caches"
	@rm -rf $(VENV_DIR) */__pycache__ __pycache__

env:
	@if [ -f "$(ENV)" ]; then \
		echo ">> $(ENV) exists"; \
	elif [ -f "$(ENV_EX)" ]; then \
		echo ">> Creating $(ENV) from $(ENV_EX)"; \
		cp "$(ENV_EX)" "$(ENV)"; \
	else \
		echo ">> Creating $(ENV) with placeholders"; \
		{ \
		  echo "SLACK_BOT_TOKEN=xoxb-your-bot-token"; \
		  echo "SLACK_APP_TOKEN=xapp-your-app-level-token"; \
		} > "$(ENV)"; \
		echo "   Fill in tokens in $(ENV) before running."; \
	fi