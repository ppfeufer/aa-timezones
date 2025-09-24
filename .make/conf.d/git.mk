# Makefile fragment for git housekeeping tasks

# Clean untracked files and directories
.PHONY: git-clean-untracked
git-clean-untracked:
	@echo "Cleaning untracked files and directories …"
	@git clean -fd

# Optimize the repository with garbage collection
.PHONY: git-garbage-collection
git-garbage-collection:
	@echo "Optimizing the repository with garbage collection …"
	@git gc --prune=now --aggressive

# Prune unreachable objects
.PHONY: git-prune
git-prune:
	@echo "Pruning unreachable objects …"
	@git prune

# Run all git housekeeping commands
.PHONY: git-housekeeping
git-housekeeping: git-clean-untracked git-prune git-garbage-collection
	@echo "Git housekeeping done …"

.PHONY: help
help::
	@echo "  $(TEXT_UNDERLINE)Git:$(TEXT_UNDERLINE_END)"
	@echo "    git-clean-untracked         Cleaning untracked files and directories"
	@echo "    git-garbage-collection      Optimizing the repository with garbage collection"
	@echo "    git-prune                   Pruning unreachable objects"
	@echo "    git-housekeeping            Run all git housekeeping commands"
	@echo ""
