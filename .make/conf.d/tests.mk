# Makefile fragment for running tests and generating coverage reports

# Coverage
.PHONY: coverage
coverage: check-python-venv
	@echo "Running tests and creating a coverage report …"
	@coverage run $(myauth_path)/manage.py \
		test \
		$(package) \
		--keepdb \
		--failfast; \
	coverage html; \
	coverage xml; \
	coverage report -m

# Build test
.PHONY: build-test
build-test: check-python-venv
	@echo "Building the package …"
	@python3 -m build

# Tox tests
.PHONY: tox-tests
tox-tests: check-python-venv
	@echo "Running tests with tox …"
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
