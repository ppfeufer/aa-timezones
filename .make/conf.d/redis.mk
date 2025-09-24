# Makefile fragment for Redis commands

# Find redis-cli
resdis_cli := $(shell which redis-cli)

# Flush all Redis keys
.PHONY: redis-flushall
redis-flushall:
	@echo "Flushing all Redis keys …"
	@$(resdis_cli) FLUSHALL

# Check Redis status
.PHONY: redis-status
redis-status:
	@echo "Checking Redis status …"
	@$(resdis_cli) ping

.PHONY: help
help::
	@echo "  $(TEXT_UNDERLINE)Redis Commands:$(TEXT_UNDERLINE_END)"
	@echo "    redis-flushall              Flush all Redis keys"
	@echo "    redis-status                Check Redis status"
	@echo ""
