# Makefile fragement for npm package management.

# Install npm dependencies
.PHONY: npm-install
npm-install:
	@echo "Installing npm dependencies…"
	@npm install

# Update npm dependencies
.PHONY: npm-update
npm-update:
	@echo "Updating npm dependencies…"
	@npm update

# Run npm audit to check for vulnerabilities
.PHONY: npm-audit
npm-audit:
	@echo "Running npm audit…"
	@npm audit

# Run npm audit fix to automatically fix vulnerabilities
.PHONY: npm-audit-fix
npm-audit-fix:
	@echo "Running npm audit fix…"
	@npm audit fix

# Run a specific npm script
.PHONY: npm-run
npm-run:
	@echo "Running npm script…"
	@npm run $(script)

help::
	@echo "  $(TEXT_UNDERLINE)Node.js Package Management (NPM):$(TEXT_RESET)"
	@echo "    npm-install                 Install npm dependencies"
	@echo "    npm-update                  Update npm dependencies"
	@echo "    npm-audit                   Run npm audit"
	@echo "    npm-audit-fix               Run npm audit fix"
	@echo "    npm-run script=<script>     Run a specific npm script (replace <script> with the script name)"
	@echo ""
