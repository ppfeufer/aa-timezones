# Makefile fragment for running tests and generating coverage reports

# Coverage
.PHONY: coverage
coverage: check-python-venv check-myauth-path
	@echo "Running tests and creating a coverage report…"
	@coverage run $(DJANGO__MYAUTH_PATH)/manage.py \
		test \
		$(GENERAL__PACKAGE) \
		--keepdb \
		--failfast; \
	coverage html; \
	coverage xml; \
	coverage report -m

# Build test
.PHONY: build-test
build-test: check-python-venv
	@echo "Building the package…"
	@$(PYTHON__EXECUTABLE) -m build

# Tox tests
.PHONY: tox-tests
tox-tests: check-python-venv
	@echo "Running tests with tox…"
	@export USE_MYSQL=False; \
	tox -v -e allianceauth-latest; \

# Help message
.PHONY: help
help::
	@echo "  $(TEXT_UNDERLINE)Tests:$(TEXT_UNDERLINE_END)"
	@echo "    build-test                  Build the package"
	@echo "    coverage                    Run tests and create a coverage report"
	@echo "    tox-tests                   Run tests with tox"
	@echo ""
