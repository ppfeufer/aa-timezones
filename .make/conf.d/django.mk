# Makefile fragment for Django-related tasks

# List of languages to create translation files for
django_locales = \
	--locale cs_CZ \
	--locale de \
	--locale es \
	--locale fr_FR \
	--locale it_IT \
	--locale ja \
	--locale ko_KR \
	--locale nl_NL \
	--locale pl_PL \
	--locale ru \
	--locale sk \
	--locale uk \
	--locale zh_Hans

# Create or update translation template (.pot file)
.PHONY: pot
pot: check-python-venv
	@echo "Creating or updating .pot file…"
	@django-admin makemessages \
		--locale en \
		--keep-pot \
		--ignore 'build/*' \
		--ignore 'node_modules/*' \
		--ignore 'testauth/*' \
		--ignore 'runtests.py'
	@current_app_version=$$(pip show $(GENERAL__APPNAME) | grep 'Version: ' | awk '{print $$NF}'); \
	# Update the .pot file with the correct Project-Id-Version and Report-Msgid-Bugs-To headers \
	sed -i "/\"Project-Id-Version: /c\\\"Project-Id-Version: $(GENERAL__APPNAME_VERBOSE)\\\n\"" $(DJANGO__TRANSLATION_TEMPLATE); \
	sed -i "/\"Report-Msgid-Bugs-To: /c\\\"Report-Msgid-Bugs-To: $(WEBLATE__BASE_URL)/projects/$(WEBLATE__PROJECT_SLUG)/$(WEBLATE__COMPONENT_SLUG)/\\\n\"" $(DJANGO__TRANSLATION_TEMPLATE);

# Add a new translation
.PHONY: add-translation
add-translation: check-python-venv
	@echo "Adding a new translation"
	@read -p "Enter the language code (e.g. 'en_GB'): " language_code; \
	django-admin makemessages \
		--locale $$language_code \
		--keep-pot \
		--ignore 'build/*' \
		--ignore 'node_modules/*' \
		--ignore 'testauth/*' \
		--ignore 'runtests.py'; \
	current_app_version=$$(pip show $(GENERAL__APPNAME) | grep 'Version: ' | awk '{print $$NF}'); \
	# Update the .pot file and the new translation file with the correct Project-Id-Version and Report-Msgid-Bugs-To headers \
	sed -i "/\"Project-Id-Version: /c\\\"Project-Id-Version: $(GENERAL__APPNAME_VERBOSE)\\\n\"" $(DJANGO__TRANSLATION_TEMPLATE); \
	sed -i "/\"Report-Msgid-Bugs-To: /c\\\"Report-Msgid-Bugs-To: $(WEBLATE__BASE_URL)/projects/$(WEBLATE__PROJECT_SLUG)/$(WEBLATE__COMPONENT_SLUG)/\\\n\"" $(DJANGO__TRANSLATION_TEMPLATE); \
	sed -i "/\"Project-Id-Version: /c\\\"Project-Id-Version: $(GENERAL__APPNAME_VERBOSE)\\\n\"" $(DJANGO__TRANSLATION_DIRECTORY)/$$language_code/$(DJANGO__TRANSLATION_FILE_RELATIVE_PATH); \
	sed -i "/\"Report-Msgid-Bugs-To: /c\\\"Report-Msgid-Bugs-To: $(WEBLATE__BASE_URL)/projects/$(WEBLATE__PROJECT_SLUG)/$(WEBLATE__COMPONENT_SLUG)/\\\n\"" $(DJANGO__TRANSLATION_DIRECTORY)/$$language_code/$(DJANGO__TRANSLATION_FILE_RELATIVE_PATH); \
	echo "New translation added for $$language_code"; \
	echo "Please remember to add '--locale $$language_code \' to the 'translations' target in the Makefile";

# Greate or update translation files
.PHONY: translations
translations: check-python-venv
	@echo "Creating or updating translation files"
	@django-admin makemessages $(django_locales) \
		--keep-pot \
		--ignore 'build/*' \
		--ignore 'node_modules/*' \
		--ignore 'testauth/*' \
		--ignore 'runtests.py'
	@current_app_version=$$(pip show $(GENERAL__APPNAME) | grep 'Version: ' | awk '{print $$NF}'); \
	# Update the .pot file and all translation files with the correct Project-Id-Version and Report-Msgid-Bugs-To headers \
	sed -i "/\"Project-Id-Version: /c\\\"Project-Id-Version: $(GENERAL__APPNAME_VERBOSE)\\\n\"" $(DJANGO__TRANSLATION_TEMPLATE); \
	sed -i "/\"Report-Msgid-Bugs-To: /c\\\"Report-Msgid-Bugs-To: $(WEBLATE__BASE_URL)/projects/$(WEBLATE__PROJECT_SLUG)/$(WEBLATE__COMPONENT_SLUG)/\\\n\"" $(DJANGO__TRANSLATION_TEMPLATE); \
	subdircount=$$(find $(DJANGO__TRANSLATION_DIRECTORY) -mindepth 1 -maxdepth 1 -type d | wc -l); \
	if [[ $$subdircount -gt 1 ]]; then \
		for path in $(DJANGO__TRANSLATION_DIRECTORY)/*/; do \
			[ -d "$$path/LC_MESSAGES" ] || continue; \
			if [[ -f "$$path/$(DJANGO__TRANSLATION_FILE_RELATIVE_PATH)" ]] \
				then \
					sed -i "/\"Project-Id-Version: /c\\\"Project-Id-Version: $(GENERAL__APPNAME_VERBOSE)\\\n\"" $$path/$(DJANGO__TRANSLATION_FILE_RELATIVE_PATH); \
					sed -i "/\"Report-Msgid-Bugs-To: /c\\\"Report-Msgid-Bugs-To: $(WEBLATE__BASE_URL)/projects/$(WEBLATE__PROJECT_SLUG)/$(WEBLATE__COMPONENT_SLUG)/\\\n\"" $$path/$(DJANGO__TRANSLATION_FILE_RELATIVE_PATH); \
			fi; \
		done; \
	fi;

# Compile translation files
.PHONY: compile-translations
compile-translations: check-python-venv
	@echo "Compiling translation files"
	@django-admin compilemessages $(django_locales)

# Migrate all database changes
.PHONY: migrate
migrate: check-python-venv check-myauth-path
	@echo "Migrating the database"
	@$(PYTHON__EXECUTABLE) $(DJANGO__MYAUTH_PATH)/manage.py migrate $(GENERAL__PACKAGE)

# Make migrations for the app
.PHONY: migrations
migrations: check-python-venv check-myauth-path
	@echo "Creating or updating migrations"
	@$(PYTHON__EXECUTABLE) $(DJANGO__MYAUTH_PATH)/manage.py makemigrations $(GENERAL__PACKAGE)

.PHONY: showmigrations
showmigrations: check-python-venv check-myauth-path
	@echo "Showing migrations"
	@$(PYTHON__EXECUTABLE) $(DJANGO__MYAUTH_PATH)/manage.py showmigrations $(GENERAL__PACKAGE)

# Help message
.PHONY: help
help::
	@echo "  $(TEXT_UNDERLINE)Django:$(TEXT_UNDERLINE_END)"
	@echo "    Migration Handling:"
	@echo "      migrate                   Migrate all database changes"
	@echo "      migrations                Create or update migrations"
	@echo "      showmigrations            Show migrations"
	@echo ""
	@echo "    Translation Handling:"
	@echo "      add-translation           Add a new translation"
	@echo "      compile-translations      Compile translation files"
	@echo "      pot                       Create or update translation template (.pot file)"
	@echo "      translations              Create or update translation files"
	@echo ""
