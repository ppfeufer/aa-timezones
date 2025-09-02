# Makefile fragment for django-esi related tasks

.PHONY: get-compatibility-dates
get-compatibility-dates:
	@echo "Fetching compatibility dates for ESI API..."; \
	response=$$(curl -s "https://esi.evetech.net/meta/compatibility-dates"); \
	if [ $$? -ne 0 ]; \
		then \
			echo "Error: Failed to fetch compatibility dates"; \
			exit 1; \
	fi; \
	dates=$$(echo "$$response" | jq -r '.compatibility_dates[]' | sort -r); \
	if [ -z "$$dates" ]; \
		then \
			echo "Error: No dates found or invalid response"; \
			exit 1; \
	fi; \
	echo ""; \
	echo "Available ESI compatibility dates:"; \
	echo "=================================================="; \
	counter=1; \
	while IFS= read -r date; \
		do \
			formatted_date=$$(date -d "$$date" "+%B %d, %Y" 2>/dev/null || echo "Invalid date"); \
			printf "%2d. %s (%s)\n" "$$counter" "$$date" "$$formatted_date"; \
			counter=$$((counter + 1)); \
		done <<< "$$dates"; \
	echo ""; \
	read -p "Select a date (1-$$((counter-1))) or press Enter to use the latest date: " choice; \
	if [ -z "$$choice" ]; \
		then \
			latest_date=$$(echo "$$dates" | head -n 1); \
			echo "Using latest date: $$latest_date"; \
			echo "$$latest_date" > .esi-compatibility-date; \
	else \
		if ! [[ "$$choice" =~ ^[0-9]+$$ ]] || [ "$$choice" -lt 1 ] || [ "$$choice" -gt $$((counter-1)) ]; \
			then \
				echo "Invalid selection. Please run again."; \
				exit 1; \
		fi; \
		selected_date=$$(echo "$$dates" | sed -n "$${choice}p"); \
		echo ""; \
		echo "$(TEXT_BOLD)Selected:$(TEXT_BOLD_END) $$selected_date"; \
		echo "$$selected_date" > .esi-compatibility-date; \
		echo ""; \
	fi

.PHONY: generate-esi-stubs
generate-esi-stubs: check-python-venv get-compatibility-dates
	@echo "Generating ESI stubs …"
	@echo ""
	@esi_date=$$(cat .esi-compatibility-date 2>/dev/null || exit 0); \
	python ../myauth/manage.py generate_esi_stubs --compatibility_date="$$esi_date"
	@echo "ESI stubs generated."

.PHONY: update-compatibility-date
update-compatibility-date: check-python-venv get-compatibility-dates
	@echo "Updating ESI compatibility date..."
	@echo ""
	@esi_date=$$(cat .esi-compatibility-date 2>/dev/null || exit 0); \
	sed -i "/__esi_compatibility_date__ = /c\__esi_compatibility_date__ = \"$$esi_date\"" $(package)/__init__.py

# Help message
help::
	@echo "  $(TEXT_UNDERLINE)Django-ESI:$(TEXT_UNDERLINE_END)"
	@echo "    update-compatibility-date   Update the app's ESI compatibility date"
	@echo "    generate-esi-stubs          Generate ESI stubs"
	@echo ""
