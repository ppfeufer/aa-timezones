# Makefile for AA Timezones

# Specify the shell to be used for executing the commands in this Makefile.
# In this case, it is set to /bin/bash.
SHELL := /bin/bash

# Variables
appname = aa-timezones
appname_verbose = AA Timezones
package = timezones
translation_directory = $(package)/locale
translation_template = $(translation_directory)/django.pot
translation_file_relative_path = LC_MESSAGES/django.po
git_repository = https://github.com/ppfeufer/$(appname)
git_repository_issues = $(git_repository)/issues

# Set myauth path or default to ../myauth if config file (.make/myauth-path) does not exist
myauth_path = $(shell path=$$(cat .make/myauth-path 2>/dev/null | grep . || echo "../myauth"); echo "$${path%/}")

# Default goal
.DEFAULT_GOAL := help

# Check if Python virtual environment is active
.PHONY: check-python-venv
check-python-venv:
	@if [ -z "$(VIRTUAL_ENV)" ]; then \
		echo "$(TEXT_COLOR_RED)$(TEXT_BOLD)Python virtual environment is NOT active!$(TEXT_RESET)" ; \
		exit 1; \
	fi

# Check if the 'myauth' path exists
.PHONY: check-myauth-path
check-myauth-path:
	@if [ ! -d "$(myauth_path)" ]; then \
		echo "$(TEXT_COLOR_RED)$(TEXT_BOLD)Error: '$(myauth_path)' does not exist!$(TEXT_RESET)"; \
		echo "Please set the absolute path to your 'myauth' directory in the '.make/myauth-path' file."; \
		exit 1; \
	fi

# Confirm action
.PHONY: confirm-action
confirm-action:
	@read -p "Are you sure you want to run '$(MAKECMDGOALS)'? [Y/n] " response; \
	response=$${response:-Y}; \
	if [ "$$response" != "Y" ] && [ "$$response" != "y" ]; then \
		echo "Aborted"; \
		exit 1; \
	fi

# General confirmation
.PHONY: confirm
confirm:
	@read -p "Are you sure? [Y/n] " response; \
	response=$${response:-Y}; \
	if [ "$$response" != "Y" ] && [ "$$response" != "y" ]; then \
		echo "Aborted"; \
		exit 1; \
	fi

# Graph models
.PHONY: graph-models
graph-models: check-python-venv check-myauth-path
	@echo "Creating a graph of the models …"
	@python $(myauth_path)/manage.py \
		graph_models \
		$(package) \
		--arrow-shape normal \
		-o $(appname)-models.png

# Prepare a new release
# Update the graph of the models, translation files and the version in the package
.PHONY: prepare-release
prepare-release: pot graph-models
	@echo "Preparing a release …"
	@read -p "New Version Number: " new_version; \
	if ! grep -qE "^## \[$$new_version\]" CHANGELOG.md; then \
		previos_version=$$(grep -m 1 -E '^## \[[0-9]+(\.[0-9]+){0,2}\] - ' CHANGELOG.md | sed -E 's/^## \[([0-9]+(\.[0-9]+){0,2})\].*$$/\1/');  \
		echo "Previous release version detected: $$previos_version"; \
		echo "$(TEXT_COLOR_RED)$(TEXT_BOLD)Version $$new_version not found in CHANGELOG.md!$(TEXT_RESET)"; \
		echo "Adding a new section for version $$new_version."; \
		echo "Please check and update the $(TEXT_BOLD)CHANGELOG.md$(TEXT_RESET) file accordingly."; \
		sed -i "/<!-- Your changes go here -->/a\\\n## [$$new_version] - $$(date '+%Y-%m-%d')" CHANGELOG.md; \
		echo "[$$new_version]: $(git_repository)/compare/v$$previos_version...v$$new_version \"v$$new_version\"" >> CHANGELOG.md; \
	fi; \
	sed -i "/__version__ = /c\__version__ = \"$$new_version\"" $(package)/__init__.py; \
	echo "Updated version in $(TEXT_BOLD)$(package)/__init__.py$(TEXT_BOLD_END)"; \
	if [[ $$new_version =~ (alpha|beta) ]]; then \
		echo "$(TEXT_COLOR_RED)$(TEXT_BOLD)Pre-release$(TEXT_RESET) version detected!"; \
		git restore $(translation_directory)/django.pot; \
	elif [[ $$new_version =~ rc ]]; then \
		echo "$(TEXT_COLOR_YELLOW)$(TEXT_BOLD)Release Candidate$(TEXT_RESET) version detected!"; \
		sed -i "/\"Project-Id-Version: /c\\\"Project-Id-Version: $(appname_verbose) $$new_version\\\n\"" $(translation_template); \
		sed -i "/\"Report-Msgid-Bugs-To: /c\\\"Report-Msgid-Bugs-To: $(git_repository_issues)\\\n\"" $(translation_template); \
	else \
		echo "$(TEXT_BOLD)Release$(TEXT_BOLD_END) version detected."; \
		sed -i -E "/$(appname)==/s/==.*/==$$new_version/" README.md; \
		sed -i -E "\|\[in development\]\: |s|\]\: .*|\]\: $(git_repository)/compare/v$$new_version...HEAD \"In Development\"|g" CHANGELOG.md; \
		echo "Updated version in $(TEXT_BOLD)README.md$(TEXT_BOLD_END)"; \
		sed -i "/\"Project-Id-Version: /c\\\"Project-Id-Version: $(appname_verbose) $$new_version\\\n\"" $(translation_template); \
		sed -i "/\"Report-Msgid-Bugs-To: /c\\\"Report-Msgid-Bugs-To: $(git_repository_issues)\\\n\"" $(translation_template); \
	fi;

# Help
.PHONY: help
help::
	@echo ""
	@echo "$(TEXT_BOLD)$(appname_verbose)$(TEXT_BOLD_END) Makefile"
	@echo "('myauth_path' is set to '$(myauth_path)')"
	@echo ""
	@echo "$(TEXT_BOLD)Usage:$(TEXT_BOLD_END)"
	@echo "  make [command]"
	@echo ""
	@echo "$(TEXT_BOLD)Commands:$(TEXT_BOLD_END)"
	@echo "  $(TEXT_UNDERLINE)General:$(TEXT_UNDERLINE_END)"
	@echo "    graph-models                Create a graph of the models"
	@echo "    help                        Show this help message"
	@echo "    prepare-release             Prepare a release and update the version in '$(package)/__init__.py'."
	@echo "                                Please make sure to update the 'CHANGELOG.md' file accordingly."
	@echo ""

# Include the configurations
include .make/conf.d/*.mk
