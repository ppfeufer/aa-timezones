# Makefile fragment for development tasks

# Install the app as an editable package in the current Python environment
PHONY: dev-install
dev-install: check-python-venv
	@echo "Installing $(appname) as editable package …"
	@pip install -e .

# Uninstall the app from the current Python environment
PHONY: dev-uninstall
dev-uninstall: check-python-venv
	@echo "Uninstalling $(appname) …"
	@pip uninstall -y $(appname)

.PHONY: help
help::
	@echo "  $(TEXT_UNDERLINE)Development:$(TEXT_UNDERLINE_END)"
	@echo "    dev-install                 Install the app as editable package"
	@echo "    dev-uninstall               Uninstall the app"
	@echo ""
