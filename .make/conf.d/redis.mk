resdis_cli := $(shell which redis-cli)

.PHONY: redis-flushall
redis-flushall:
	@echo "Flushing all Redis keys …"
	@$(resdis_cli) FLUSHALL

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
