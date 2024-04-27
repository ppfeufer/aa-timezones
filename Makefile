# Makefile for AA Timezones

# Variables
appname = aa-timezones
appname_verbose = AA Timezones
package = timezones

# Default goal
.DEFAULT_GOAL := help

# Help
help:
	@echo "$(appname_verbose) Makefile"
	@echo ""
	@echo "Usage: make [command]"
	@echo ""
	@echo "Commands:"
	@echo "  build_test          Build the package"
	@echo "  coverage            Run tests and create a coverage report"
	@echo "  graph_models        Create a graph of the models"
	@echo "  pre-commit-checks   Run pre-commit checks"
	@echo "  tox_tests           Run tests with tox"
	@echo "  translationfiles    Create or update translation files"

# Translation files
translationfiles:
	#cd $(package); \
	django-admin makemessages \
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

# Graph models
graph_models:
	python ../myauth/manage.py \
		graph_models \
		$(package) \
		--arrow-shape normal \
		-o $(appname)-models.png

# Coverage
coverage:
	rm -rfv htmlcov; \
	coverage run ../myauth/manage.py \
		test \
		$(package) \
		--keepdb \
		--failfast; \
	coverage html; \
	coverage report -m

# Build test
build_test:
	rm -rfv dist; \
	python3 -m build

# Tox tests
tox_tests:
	export USE_MYSQL=False; \
	tox -v -e allianceauth-latest; \
	rm -rf .tox/

# Pre-commit checks
pre-commit-checks:
	pre-commit run --all-files
