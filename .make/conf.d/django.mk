# Make targets for Django projects

# Create or update translation template (.pot file)
.PHONY: pot
pot:
	@echo "Creating or updating .pot file …"
	@django-admin makemessages \
		-l en \
		--keep-pot \
		--ignore 'build/*'
	@current_app_version=$$(pip show $(appname) | grep 'Version: ' | awk '{print $$NF}'); \
	sed -i "/\"Project-Id-Version: /c\\\"Project-Id-Version: $(appname_verbose) $$current_app_version\\\n\"" $(translation_template); \
	sed -i "/\"Report-Msgid-Bugs-To: /c\\\"Report-Msgid-Bugs-To: $(git_repository_issues)\\\n\"" $(translation_template);

# Add a new translation
.PHONY: add_translation
add_translation:
	@echo "Adding a new translation"
	@read -p "Enter the language code (e.g. 'en_GB'): " language_code; \
	django-admin makemessages \
		-l $$language_code \
		--keep-pot \
		--ignore 'build/*'; \
	current_app_version=$$(pip show $(appname) | grep 'Version: ' | awk '{print $$NF}'); \
	sed -i "/\"Project-Id-Version: /c\\\"Project-Id-Version: $(appname_verbose) $$current_app_version\\\n\"" $(translation_template); \
	sed -i "/\"Report-Msgid-Bugs-To: /c\\\"Report-Msgid-Bugs-To: $(git_repository_issues)\\\n\"" $(translation_template); \
	sed -i "/\"Project-Id-Version: /c\\\"Project-Id-Version: $(appname_verbose) $$current_app_version\\\n\"" $(translation_directory)/$$language_code/$(translation_file_relative_path); \
	sed -i "/\"Report-Msgid-Bugs-To: /c\\\"Report-Msgid-Bugs-To: $(git_repository_issues)\\\n\"" $(translation_directory)/$$language_code/$(translation_file_relative_path); \
	echo "New translation added for $$language_code"; \
	echo "Please remember to add '-l $$language_code \' to the 'translations' target in the Makefile";

# Translation files
.PHONY: translations
translations:
	@echo "Creating or updating translation files"
	@django-admin makemessages \
		-l cs_CZ \
		-l de \
		-l es \
		-l fr_FR \
		-l it_IT \
		-l ja \
		-l ko_KR \
		-l nl_NL \
		-l pl_PL \
		-l ru \
		-l sk \
		-l uk \
		-l zh_Hans \
		--keep-pot \
		--ignore 'build/*'
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
compile_translations:
	@echo "Compiling translation files"
	@django-admin compilemessages \
		-l cs_CZ \
		-l de \
		-l es \
		-l fr_FR \
		-l it_IT \
		-l ja \
		-l ko_KR \
		-l nl_NL \
		-l pl_PL \
		-l ru \
		-l sk \
		-l uk \
		-l zh_Hans

# Migrate all database changes
.PHONY: migrate
migrate:
	@echo "Migrating the database"
	@python ../myauth/manage.py migrate $(package)

# Make migrations for the app
.PHONY: migrations
migrations:
	@echo "Creating or updating migrations"
	@python ../myauth/manage.py makemigrations $(package)

# Help message
.PHONY: help
help::
	@echo "  $(TEXT_UNDERLINE)Django:$(TEXT_UNDERLINE_END)"
	@echo "    Migration handling:"
	@echo "      migrate                 Migrate all database changes"
	@echo "      migrations              Create or update migrations"
	@echo ""
	@echo "    Translation handling:"
	@echo "      add_translation         Add a new translation"
	@echo "      compile_translations    Compile translation files"
	@echo "      pot                     Create or update translation template (.pot file)"
	@echo "      translations            Create or update translation files"
	@echo ""
