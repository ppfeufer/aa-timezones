# Makefile fragment for database-related tasks.

# Backup the database to a file in the backup directory
#
# The backup filename will be in the format:
# <database_name>_backup_<YYYY-MM-DD_hh-mm-ss>_<optional_comment>.gz
#
# The optional comment will be sanitized to only contain lowercase letters, numbers, and hyphens.
# Multiple consecutive hyphens will be replaced with a single hyphen, and leading/trailing hyphens will be removed.
# If no comment is provided, it will be omitted from the filename.
.PHONY: db-backup
db-backup:
	@echo "Backing up database $(DB__NAME)"
	@# Prompt user for an optional comment to include in the backup filename
	@printf "Comment (Optional; Press Enter to skip): "; read -r comment; \
	# Convert comment to lowercase for sanitization \
	comment_lc=$$(printf "%s" "$$comment" | tr '[:upper:]' '[:lower:]'); \
	# Replace non-alphanumeric characters with hyphens \
	comment_sanitized=$$(printf "%s" "$$comment_lc" | sed 's/[^a-z0-9]/-/g'); \
	# Collapse multiple hyphens and trim leading/trailing hyphens \
	comment_sanitized=$$(printf "%s" "$$comment_sanitized" | sed 's/-\{2,\}/-/g' | sed 's/^-//' | sed 's/-$$//'); \
	if [ -n "$$comment_sanitized" ]; then suffix="_$$comment_sanitized"; else suffix=""; fi; \
	# Construct the backup filename with timestamp and optional comment \
	filename=$(DB__NAME)_backup_$$(date +%F_%H-%M-%S)$$suffix.gz; \
	echo "Saving DB backup to $(DB__BACKUP_DIRECTORY)/$$filename"; \
	$(DB__MYSQLDUMP_EXECUTABLE) -u$(DB__USER) -p$(DB__PASSWORD) -h$(DB__HOST) $(DB__NAME) | gzip -c > $(DB__BACKUP_DIRECTORY)/$$filename

# Restore the database from a backup file in the backup directory.
.PHONY: db-restore
db-restore:
	@echo "Restoring database $(DB__NAME) from backup"
	@set -- $(DB__BACKUP_DIRECTORY)/$(DB__NAME)_backup_*.gz; \
	if [ ! -e "$$1" ]; then \
		echo "No backups found in $(DB__BACKUP_DIRECTORY) matching $(DB__NAME)_backup_*.gz"; \
		exit 1; \
	fi; \
	echo "Available backups:"; \
	i=1; \
	for f in "$$@"; do \
		echo "  $$i) $$(basename "$$f")"; \
		i=$$((i+1)); \
	done; \
	# Prompt user for selection \
	printf "Enter number to restore: "; read choice; \
	choice=$$(printf "%s" "$$choice" | tr -d '[:space:]'); \
	case "$$choice" in \
		''|*[!0-9]* ) echo "Invalid selection"; exit 1;; \
		* ) ;; \
	esac; \
	idx=1; sel=""; \
	for f in "$$@"; do \
		if [ "$$idx" -eq "$$choice" ]; then sel="$$f"; break; fi; \
		idx=$$((idx+1)); \
	done; \
	# Check if a valid selection was made \
	if [ -z "$$sel" ]; then echo "Invalid selection"; exit 1; fi; \
	echo "Restoring from $$sel"; \
	# Confirm with the user before proceeding \
	printf "Are you sure you want to restore the database $(DB__NAME) from $$sel?\nThis will overwrite the existing database. (y/N): "; read confirm; \
	if [ "$$confirm" != "y" ] && [ "$$confirm" != "Y" ]; then \
		echo "Restore cancelled"; \
		exit 0; \
	fi; \
	# Perform the restore operation \
	echo "Restoring database $(DB__NAME) from backup $$sel..."; \
	zcat "$$sel" | $(DB__MYSQL_EXECUTABLE) -u$(DB__USER) -p$(DB__PASSWORD) -h$(DB__HOST) $(DB__NAME)

# List available backup files in the backup directory.
.PHONY: db-list-backups
db-list-backups:
	@echo "Available DB backups in $(DB__BACKUP_DIRECTORY):"
	@set -- $(DB__BACKUP_DIRECTORY)/$(DB__NAME)_backup_*.gz; \
	if [ ! -e "$$1" ]; then \
		echo "No backups found in $(DB__BACKUP_DIRECTORY) matching $(DB__NAME)_backup_*.gz"; \
		exit 1; \
	fi; \
	i=1; \
	# Output the list of backup files with numbering \
	for f in "$$@"; do \
		echo "  $$i) $$(basename "$$f")"; \
		i=$$((i+1)); \
	done

# Delete a backup file from the backup directory.
.PHONY: db-delete-backup
db-delete-backup:
	@echo "Delete a DB backup from $(DB__BACKUP_DIRECTORY):"
	@set -- $(DB__BACKUP_DIRECTORY)/$(DB__NAME)_backup_*.gz; \
	if [ ! -e "$$1" ]; then \
		echo "No backups found in $(DB__BACKUP_DIRECTORY) matching $(DB__NAME)_backup_*.gz"; \
		exit 1; \
	fi; \
	i=1; \
	# Output the list of backup files with numbering \
	for f in "$$@"; do \
		echo "  $$i) $$(basename "$$f")"; \
		i=$$((i+1)); \
	done; \
	# Prompt user for selection \
	printf "Enter number to delete: "; read choice; \
	choice=$$(printf "%s" "$$choice" | tr -d '[:space:]'); \
	case "$$choice" in \
		''|*[!0-9]* ) echo "Invalid selection"; exit 1;; \
		* ) ;; \
	esac; \
	idx=1; sel=""; \
	for f in "$$@"; do \
		if [ "$$idx" -eq "$$choice" ]; then sel="$$f"; break; fi; \
		idx=$$((idx+1)); \
	done; \
	# Check if a valid selection was made \
	if [ -z "$$sel" ]; then echo "Invalid selection"; exit 1; fi; \
	echo "Deleting backup $$sel"; \
	# Confirm with the user before proceeding \
	printf "Are you sure you want to delete the backup $$sel? (y/N): "; read confirm; \
	if [ "$$confirm" != "y" ] && [ "$$confirm" != "Y" ]; then \
		echo "Delete cancelled"; \
		exit 0; \
	fi; \
	# Perform the delete operation \
	rm -f "$$sel"; \
	echo "Backup $$sel deleted successfully."

help::
	@echo "  $(TEXT_UNDERLINE)Database:$(TEXT_RESET)"
	@echo "    db-backup                   Backup the database $(DB__NAME) to $(DB__BACKUP_DIRECTORY)"
	@echo "    db-delete-backup            Delete a backup of the database $(DB__NAME) from $(DB__BACKUP_DIRECTORY)"
	@echo "    db-list-backups             List available backups in $(DB__BACKUP_DIRECTORY)"
	@echo "    db-restore                  Restore the database $(DB__NAME) from a backup in $(DB__BACKUP_DIRECTORY)"
	@echo ""
