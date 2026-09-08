# Makefile fragment for development tasks

# Install the app as an editable package in the current Python environment
PHONY: dev-install
dev-install: check-python-venv
	@echo "Installing $(GENERAL__APPNAME) as editable package…"
	@pip install -e $(DEVELOPMENT__BASE_DIR)

# Uninstall the app from the current Python environment
PHONY: dev-uninstall
dev-uninstall: check-python-venv
	@echo "Uninstalling $(GENERAL__APPNAME)…"
	@pip uninstall -y $(GENERAL__APPNAME)

.PHONY: help
help::
	@echo "  $(TEXT_UNDERLINE)Development:$(TEXT_UNDERLINE_END)"
	@echo "    dev-install                 Install the app as editable package"
	@echo "    dev-uninstall               Uninstall the app"
	@echo ""
