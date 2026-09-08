# Makefile

# Specify the shell to be used for executing the commands in this Makefile.
# In this case, it is set to /bin/bash.
SHELL := /bin/bash

# Base config file that should always exist
ConfigFile := .make/config.ini
# Optional override config file that may or may not exist, allowing for specific overrides
ConfigFileOverride := .make/config-overrides.ini
# Combine both config files into a single list for parsing, with the base config first and the override second
ParsedConfigFiles := $(ConfigFile) $(wildcard $(ConfigFileOverride))

# Extract all config values from $(ConfigFile) and export them as Makefile variables
ifneq ($(wildcard $(ConfigFile)),)
TMPFILE := $(shell mkdir -p $(dir $(ConfigFile)) && mktemp $(dir $(ConfigFile))/make_vars.XXXXXX)
$(shell awk -F= '/^\[/{gsub(/^^\[|\]$$/, "", $$0); section=$$0; next} /^[^#;].*=/ { key=$$1; val=$$0; sub(/^[^=]*=/, "", val); gsub(/^[ \t]+|[ \t]+$$/, "", val); gsub(/^[ \t]+|[ \t]+$$/, "", key); if(section=="") name=toupper(key); else name=toupper(section"__"key); gsub(/[^A-Z0-9_]/, "_", name); gsub(/[$$]/, "$$$$", val); printf "%s := %s\n", name, val }' $(ParsedConfigFiles) > $(TMPFILE))
include $(TMPFILE)
$(shell rm -f $(TMPFILE))

# Also capture the list of variable NAMES (for show-config output).
ConfigVars := $(shell awk -F= '/^\[/{gsub(/^^\[|\]$$/, "", $$0); section=$$0; next} /^[^#;].*=/ { key=$$1; gsub(/^[ \t]+|[ \t]+$$/, "", key); if(section=="") name=toupper(key); else name=toupper(section"__"key); gsub(/[^A-Z0-9_]/, "_", name); print name }' $(ParsedConfigFiles) | sort -u)
else
# Notify the user that no config file was found.
$(error Config file '$(ConfigFile)' not found. To configure the project, create '$(ConfigFile)')
endif

# Set DJANGO__MYAUTH_PATH variable: prefer DJANGO__MYAUTH_PATH from config, fallback to ../myauth
# Also ensure there's no trailing slash.
DJANGO__MYAUTH_PATH := $(patsubst %/, %, $(if $(DJANGO__MYAUTH_PATH), $(DJANGO__MYAUTH_PATH), ../myauth))

# Reusable check for Python virtual environment. Several targets need the
# same shell snippet; define it once and reuse to avoid duplication.
define VENV_CHECK
if [ -z "$(VIRTUAL_ENV)" ]; then \
	echo ""; \
	echo "$(TEXT_COLOR_RED)$(TEXT_BOLD)Python virtual environment is NOT active!$(TEXT_RESET)" ; \
	echo "Please activate the Python virtual environment before running any commands."; \
	echo "To activate, run: $(TEXT_COLOR_GREEN)source $(PYTHON__VENV_PATH)/bin/activate$(TEXT_RESET)"; \
	echo ""; \
fi
endef

# Default goal
.DEFAULT_GOAL := help

# Check if Python virtual environment is active
.PHONY: check-python-venv
check-python-venv:
	@$(VENV_CHECK)
	@if [ -z "$(VIRTUAL_ENV)" ]; then \
		exit 1; \
	fi

# Check if the 'myauth' path exists
.PHONY: check-myauth-path
check-myauth-path:
	@if [ ! -d "$(DJANGO__MYAUTH_PATH)" ]; then \
		echo "$(TEXT_COLOR_RED)$(TEXT_BOLD)Error: '$(DJANGO__MYAUTH_PATH)' does not exist!$(TEXT_RESET)"; \
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
	@echo "Creating a graph of the models…"
	@$(PYTHON__EXECUTABLE) $(DJANGO__MYAUTH_PATH)/manage.py \
		graph_models \
		$(GENERAL__PACKAGE) \
		--arrow-shape normal \
		-o $(GENERAL__APPNAME)-models.png

# Prepare a new release
# Update the graph of the models, translation files and the version in the package
.PHONY: prepare-release
prepare-release: pot graph-models
	@echo "Preparing a release…"
	@read -p "New Version Number: " new_version; \
	if ! grep -qE "^## \[$$new_version\]" CHANGELOG.md; then \
		previous_version=$$(grep -m 1 -E '^## \[[0-9]+(\.[0-9]+){0,2}\] - ' CHANGELOG.md | sed -E 's/^## \[([0-9]+(\.[0-9]+){0,2})\].*$$/\1/');  \
		echo "Previous release version detected: $$previous_version"; \
		echo "$(TEXT_COLOR_RED)$(TEXT_BOLD)Version $$new_version not found in CHANGELOG.md!$(TEXT_RESET)"; \
		echo "Adding a new section for version $$new_version."; \
		echo "Please check and update the $(TEXT_BOLD)CHANGELOG.md$(TEXT_RESET) file accordingly."; \
		sed -i "/<!-- Your changes go here -->/a\\\n## [$$new_version] - $$(date '+%Y-%m-%d')" CHANGELOG.md; \
		echo "[$$new_version]: $(GIT__GIT_REPOSITORY)/compare/v$$previous_version...v$$new_version \"v$$new_version\"" >> CHANGELOG.md; \
	fi; \
	sed -i "/__version__ = /c\__version__ = \"$$new_version\"" $(GENERAL__PACKAGE)/__init__.py; \
	echo "Updated version in $(TEXT_BOLD)$(GENERAL__PACKAGE)/__init__.py$(TEXT_BOLD_END)"; \
	# Update the version in package.json and rebuild node modules \
	sed -i -E "\|\"version\"\: |s|\"\: .*|\"\: \"$$new_version\",|g" package.json; \
	rm -rf node_modules; \
#	rm package-lock.json; \
	npm install; \
	if [[ $$new_version =~ (alpha|beta) ]]; then \
		echo "$(TEXT_COLOR_RED)$(TEXT_BOLD)Pre-release$(TEXT_RESET) version detected!"; \
		git restore $(DJANGO__TRANSLATION_DIRECTORY)/django.pot; \
	elif [[ $$new_version =~ rc ]]; then \
		echo "$(TEXT_COLOR_YELLOW)$(TEXT_BOLD)Release Candidate$(TEXT_RESET) version detected!"; \
		sed -i "/\"Project-Id-Version: /c\\\"Project-Id-Version: $(GENERAL__APPNAME_VERBOSE)\\\n\"" $(DJANGO__TRANSLATION_TEMPLATE); \
		sed -i "/\"Report-Msgid-Bugs-To: /c\\\"Report-Msgid-Bugs-To: $(WEBLATE__BASE_URL)/projects/$(WEBLATE__PROJECT_SLUG)/$(WEBLATE__COMPONENT_SLUG)/\\\n\"" $(DJANGO__TRANSLATION_TEMPLATE); \
	else \
		echo "$(TEXT_BOLD)Release$(TEXT_BOLD_END) version detected."; \
		sed -i -E "/$(GENERAL__APPNAME)==/s/==.*/==$$new_version/" README.md; \
		sed -i -E "\|\[in development\]\: |s|\]\: .*|\]\: $(GIT__GIT_REPOSITORY)/compare/v$$new_version...HEAD \"In Development\"|g" CHANGELOG.md; \
		echo "Updated version in $(TEXT_BOLD)README.md$(TEXT_BOLD_END)"; \
		sed -i "/\"Project-Id-Version: /c\\\"Project-Id-Version: $(GENERAL__APPNAME_VERBOSE)\\\n\"" $(DJANGO__TRANSLATION_TEMPLATE); \
		sed -i "/\"Report-Msgid-Bugs-To: /c\\\"Report-Msgid-Bugs-To: $(WEBLATE__BASE_URL)/projects/$(WEBLATE__PROJECT_SLUG)/$(WEBLATE__COMPONENT_SLUG)/\\\n\"" $(DJANGO__TRANSLATION_TEMPLATE); \
	fi;


# Debug:
#    Show parsed config variables
.PHONY: show-config
show-config: show-parsed-config-files
	@echo "$(TEXT_BOLD)Parsed variables from parsed config files (NAME = VALUE):$(TEXT_RESET)"
	@echo ""
	@$(foreach var, $(ConfigVars), printf "%s = %s\n" "$(var)" "$($(var))";)
	@echo ""
	@$(VENV_CHECK)

# Debug:
#    Show which config files were parsed and in what order
#    Whether they were found or missing
#    Which variables were overridden in the override file (if present)
.PHONY: show-parsed-config-files
show-parsed-config-files:
	@echo ""
	@echo "$(TEXT_BOLD)Config files parsed (first -> last):$(TEXT_RESET)"
	@printf "  %s\n" $(ParsedConfigFiles)
	@echo ""
	@if [ -f "$(ConfigFile)" ]; then \
		echo "Base config: $(ConfigFile) (found)"; \
	else \
		echo "Base config: $(ConfigFile) (missing)"; \
	fi
	@if [ -f "$(ConfigFileOverride)" ]; then \
		echo "Override config (optional): $(ConfigFileOverride) (found)"; \
	else \
		echo "Override config (optional): $(ConfigFileOverride) (not present)"; \
	fi
	@echo ""
	@# Print variables that were overridden in the override file
	@{ \
		set -euo pipefail; \
		base="$(ConfigFile)"; \
		override="$(ConfigFileOverride)"; \
		base_tmp=$$(mktemp); \
		ovr_tmp=$$(mktemp); \
		awk -F= '/^\[/ {gsub(/^^\[|\]$$/, "", $$0); section=$$0; next} /^[^#;].*=/ { key=$$1; val=$$0; sub(/^[^=]*=/, "", val); gsub(/^[ \t]+|[ \t]+$$/, "", val); gsub(/^[ \t]+|[ \t]+$$/, "", key); if(section=="") name=toupper(key); else name=toupper(section"__"key); gsub(/[^A-Z0-9_]/, "_", name); printf "%s=%s\n", name, val }' "$$base" > "$$base_tmp"; \
		if [ -f "$$override" ]; then \
			awk -F= '/^\[/ {gsub(/^^\[|\]$$/, "", $$0); section=$$0; next} /^[^#;].*=/ { key=$$1; val=$$0; sub(/^[^=]*=/, "", val); gsub(/^[ \t]+|[ \t]+$$/, "", val); gsub(/^[ \t]+|[ \t]+$$/, "", key); if(section=="") name=toupper(key); else name=toupper(section"__"key); gsub(/[^A-Z0-9_]/, "_", name); printf "%s=%s\n", name, val }' "$$override" > "$$ovr_tmp"; \
			if [ -s "$$ovr_tmp" ]; then \
				echo "$(TEXT_UNDERLINE)Overridden variables:$(TEXT_RESET)"; \
				base_sorted="$$base_tmp.sorted"; \
				ovr_sorted="$$ovr_tmp.sorted"; \
				sort "$$base_tmp" > "$$base_sorted"; \
				sort "$$ovr_tmp" > "$$ovr_sorted"; \
				join -t= -o 0,1.2,2.2 "$$base_sorted" "$$ovr_sorted" 2>/dev/null | while IFS='=' read -r name baseval ovrval; do \
					if [ "$$baseval" != "$$ovrval" ]; then \
						echo "- $$name"; \
						echo "    Base: $$baseval"; \
						echo "    Override: $$ovrval"; \
						echo "    Final: $$ovrval"; \
						echo ""; \
					fi; \
				done; \
				# Report variables that exist only in the override (new variables) \
				only_ovr_tmp=$$(mktemp); \
				join -t= -v2 "$$base_sorted" "$$ovr_sorted" > "$$only_ovr_tmp" 2>/dev/null || true; \
				if [ -s "$$only_ovr_tmp" ]; then \
					echo "$(TEXT_UNDERLINE)New Variables (Only in Override):$(TEXT_RESET)"; \
					while IFS='=' read -r name val; do \
						echo "- $$name"; \
						echo "    Value: $$val"; \
						echo ""; \
					done < "$$only_ovr_tmp"; \
				fi; \
				rm -f "$$only_ovr_tmp"; \
			else \
				echo "  (Override config file present but no variables overridden)"; \
				echo ""; \
			fi; \
		else \
			echo "  (No override config file present)"; \
			echo ""; \
		fi; \
		rm -f "$$base_tmp" "$$ovr_tmp" "$$base_tmp.sorted" "$$ovr_tmp.sorted"; \
	}

# Help
.PHONY: help
help::
	@echo ""
	@echo "$(TEXT_BOLD)$(GENERAL__APPNAME_VERBOSE)$(TEXT_BOLD_END) Makefile"
	@echo "('myauth' path is set to '$(DJANGO__MYAUTH_PATH)')"
	@echo ""
	@echo "$(TEXT_BOLD)Usage:$(TEXT_BOLD_END)"
	@echo "  make [command]"
	@echo ""
	@echo "$(TEXT_BOLD)Commands:$(TEXT_BOLD_END)"
	@echo "  $(TEXT_UNDERLINE)General:$(TEXT_UNDERLINE_END)"
	@echo "    graph-models                Create a graph of the models"
	@echo "    help                        Show this help message"
	@echo "    prepare-release             Prepare a release and update the version in '$(GENERAL__PACKAGE)/__init__.py'."
	@echo "                                Please make sure to update the 'CHANGELOG.md' file accordingly."
	@echo ""

# Catchall for unknown commands to fail gracefully
.DEFAULT:
	@true

# Include the configurations
include .make/conf.d/*.mk

# Append warning about Python virtual environment if not active at the end of the help message
help::
	@$(VENV_CHECK)
