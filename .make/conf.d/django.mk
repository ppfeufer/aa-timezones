# Make targets for Django projects

# Translation files
.PHONY: translations
translations:
	@echo "Creating or updating translation files"
	@django-admin makemessages \
		-l cs \
		-l de \
		-l es \
		-l fr_FR \
		-l it_IT \
		-l ja \
		-l ko_KR \
		-l nl \
		-l pl_PL \
		-l ru \
		-l sk \
		-l uk \
		-l zh_Hans \
		--keep-pot \
		--ignore 'build/*'

# Compile translation files
.PHONY: compile_translations
compile_translations:
	@echo "Compiling translation files"
	@django-admin compilemessages \
		-l cs \
		-l de \
		-l es \
		-l fr_FR \
		-l it_IT \
		-l ja \
		-l ko_KR \
		-l nl \
		-l pl_PL \
		-l ru \
		-l sk \
		-l uk \
		-l zh_Hans

# Help message
.PHONY: help
help::
	@echo "  $(TEXT_UNDERLINE)Translation:$(TEXT_UNDERLINE_END)"
	@echo "    translations              Create or update translation files"
	@echo "    compile_translations      Compile translation files"
	@echo ""
