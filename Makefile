# Makefile for AA Timezones

appname = aa-timezones
appname_verbose = AA Timezones
package = timezones

help:
	@echo "$(appname_verbose) Makefile"
	@echo ""
	@echo "Usage: make [command]"
	@echo ""
	@echo "Commands:"
	@echo "  translationfiles    Create or update translation files"
	@echo "  graph_models        Create a graph of the models"
	@echo "  coverage            Run tests and create a coverage report"
	@echo "  build_test          Build the package"
	@echo "  tox_tests           Run tests with tox"

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

graph_models:
	python ../myauth/manage.py \
		graph_models \
		$(package) \
		--arrow-shape normal \
		-o $(appname)-models.png

coverage:
	rm -rfv htmlcov; \
	coverage run ../myauth/manage.py \
		test \
		$(package) \
		--keepdb \
		--failfast; \
	coverage html; \
	coverage report -m

build_test:
	rm -rfv dist; \
	python3 -m build

tox_tests:
	export USE_MYSQL=False; \
	tox -v -e allianceauth-latest; \
	rm -rf .tox/
