# Make targets for Django projects

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
	@echo "Creating or updating .pot file …"
	@django-admin makemessages \
		--locale en \
		--keep-pot \
		--ignore 'build/*' \
		--ignore 'node_modules/*' \
		--ignore 'testauth/*' \
		--ignore 'runtests.py'
	@current_app_version=$$(pip show $(appname) | grep 'Version: ' | awk '{print $$NF}'); \
	sed -i "/\"Project-Id-Version: /c\\\"Project-Id-Version: $(appname_verbose) $$current_app_version\\\n\"" $(translation_template); \
	sed -i "/\"Report-Msgid-Bugs-To: /c\\\"Report-Msgid-Bugs-To: $(git_repository_issues)\\\n\"" $(translation_template);

# Add a new translation
.PHONY: add_translation
add_translation: check-python-venv
	@echo "Adding a new translation"
	@read -p "Enter the language code (e.g. 'en_GB'): " language_code; \
	django-admin makemessages \
		--locale $$language_code \
		--keep-pot \
		--ignore 'build/*' \
		--ignore 'node_modules/*' \
		--ignore 'testauth/*' \
		--ignore 'runtests.py'; \
	current_app_version=$$(pip show $(appname) | grep 'Version: ' | awk '{print $$NF}'); \
	sed -i "/\"Project-Id-Version: /c\\\"Project-Id-Version: $(appname_verbose) $$current_app_version\\\n\"" $(translation_template); \
	sed -i "/\"Report-Msgid-Bugs-To: /c\\\"Report-Msgid-Bugs-To: $(git_repository_issues)\\\n\"" $(translation_template); \
	sed -i "/\"Project-Id-Version: /c\\\"Project-Id-Version: $(appname_verbose) $$current_app_version\\\n\"" $(translation_directory)/$$language_code/$(translation_file_relative_path); \
	sed -i "/\"Report-Msgid-Bugs-To: /c\\\"Report-Msgid-Bugs-To: $(git_repository_issues)\\\n\"" $(translation_directory)/$$language_code/$(translation_file_relative_path); \
	echo "New translation added for $$language_code"; \
	echo "Please remember to add '-l $$language_code \' to the 'translations' target in the Makefile";

# Translation files
.PHONY: translations
translations: check-python-venv
	@echo "Creating or updating translation files"
	@django-admin makemessages $(django_locales) \
		--keep-pot \
		--ignore 'build/*' \
		--ignore 'node_modules/*' \
		--ignore 'testauth/*' \
		--ignore 'runtests.py'
	@current_app_version=$$(pip show $(appname) | grep 'Version: ' | awk '{print $$NF}'); \
	sed -i "/\"Project-Id-Version: /c\\\"Project-Id-Version: $(appname_verbose) $$current_app_version\\\n\"" $(translation_template); \
	sed -i "/\"Report-Msgid-Bugs-To: /c\\\"Report-Msgid-Bugs-To: $(git_repository_issues)\\\n\"" $(translation_template); \
	subdircount=$$(find $(translation_directory) -mindepth 1 -maxdepth 1 -type d | wc -l); \
	if [[ $$subdircount -gt 1 ]]; then \
		for path in $(translation_directory)/*/; do \
			[ -d "$$path/LC_MESSAGES" ] || continue; \
			if [[ -f "$$path/$(translation_file_relative_path)" ]] \
				then \
					sed -i "/\"Project-Id-Version: /c\\\"Project-Id-Version: $(appname_verbose) $$current_app_version\\\n\"" $$path/$(translation_file_relative_path); \
					sed -i "/\"Report-Msgid-Bugs-To: /c\\\"Report-Msgid-Bugs-To: $(git_repository_issues)\\\n\"" $$path/$(translation_file_relative_path); \
			fi; \
		done; \
	fi;

# Compile translation files
.PHONY: compile_translations
compile_translations: check-python-venv
	@echo "Compiling translation files"
	@django-admin compilemessages $(django_locales)

# Migrate all database changes
.PHONY: migrate
migrate: check-python-venv
	@echo "Migrating the database"
	@python ../myauth/manage.py migrate $(package)

# Make migrations for the app
.PHONY: migrations
migrations: check-python-venv
	@echo "Creating or updating migrations"
	@python ../myauth/manage.py makemigrations $(package)

# Help message
.PHONY: help
help::
	@echo "  $(TEXT_UNDERLINE)Django:$(TEXT_UNDERLINE_END)"
	@echo "    Migration handling:"
	@echo "      migrate                   Migrate all database changes"
	@echo "      migrations                Create or update migrations"
	@echo ""
	@echo "    Translation handling:"
	@echo "      add_translation           Add a new translation"
	@echo "      compile_translations      Compile translation files"
	@echo "      pot                       Create or update translation template (.pot file)"
	@echo "      translations              Create or update translation files"
	@echo ""
