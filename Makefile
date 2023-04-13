appname = aa-timezones
package = timezones

help:
	@echo "Makefile for $(appname)"

translationfiles:
	cd $(package) && \
	django-admin makemessages -l de --ignore 'build/*' && \
	django-admin makemessages -l es --ignore 'build/*' && \
	django-admin makemessages -l fr_FR --ignore 'build/*' && \
	django-admin makemessages -l it_IT --ignore 'build/*' && \
	django-admin makemessages -l ja --ignore 'build/*' && \
	django-admin makemessages -l ko_KR --ignore 'build/*' && \
	django-admin makemessages -l ru --ignore 'build/*' && \
	django-admin makemessages -l zh_Hans --ignore 'build/*'

compiletranslationfiles:
	cd $(package) && \
	django-admin compilemessages -l de  && \
	django-admin compilemessages -l es  && \
	django-admin compilemessages -l fr_FR  && \
	django-admin compilemessages -l it_IT  && \
	django-admin compilemessages -l ja  && \
	django-admin compilemessages -l ko_KR  && \
	django-admin compilemessages -l ru  && \
	django-admin compilemessages -l zh_Hans

graph_models:
	python ../myauth/manage.py graph_models $(package) --arrow-shape normal -o $(appname)-models.png

coverage:
	rm -rfv htmlcov && \
	coverage run ../myauth/manage.py test $(package) --keepdb --failfast && coverage html && coverage report -m

build_test:
	rm -rfv dist && \
	python3 -m build

tox_tests:
	export USE_MYSQL=False && \
	tox && \
	rm -rf .tox/
