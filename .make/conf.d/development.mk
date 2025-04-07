PHONY: dev-install
dev-install:
	@echo "Installing $(appname) as editable package …"
	@pip install -e .

PHONY: dev-uninstall
dev-uninstall:
	@echo "Uninstalling $(appname) …"
	@pip uninstall -y $(appname)

.PHONY: help
help::
	@echo "  $(TEXT_UNDERLINE)Development:$(TEXT_UNDERLINE_END)"
	@echo "    dev-install               Install the app as editable package"
	@echo "    dev-uninstall             Uninstall the app"
	@echo ""
