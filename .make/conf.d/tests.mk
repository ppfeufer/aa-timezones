# Make targets for tests

# Coverage
.PHONY: coverage
coverage: check-python-venv
	@echo "Running tests and creating a coverage report …"
#	@rm -rf htmlcov
	@coverage run ../myauth/manage.py \
		test \
		$(package) \
		--keepdb \
		--failfast; \
	coverage html; \
	coverage xml; \
	coverage report -m

# Build test
.PHONY: build_test
build_test: check-python-venv
	@echo "Building the package …"
#	@rm -rf dist
	@python3 -m build

# Tox tests
.PHONY: tox_tests
tox_tests: check-python-venv
	@echo "Running tests with tox …"
	@export USE_MYSQL=False; \
	tox -v -e allianceauth-latest; \
#	rm -rf .tox/

# Help message
.PHONY: help
help::
	@echo "  $(TEXT_UNDERLINE)Tests:$(TEXT_UNDERLINE_END)"
	@echo "    build_test                  Build the package"
	@echo "    coverage                    Run tests and create a coverage report"
	@echo "    tox_tests                   Run tests with tox"
	@echo ""
