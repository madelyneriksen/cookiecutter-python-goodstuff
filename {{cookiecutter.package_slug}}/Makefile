SHELL=/bin/bash
VERSION=$(shell cat VERSION)

build: test
	(\
	  source .env/bin/activate; \
	  python setup.py sdist bdist;
	)

test: .env/bin/activate
	(\
	  source .env/bin/activate; \
	  pytest; \{% if cookiecutter.type_checker == "Pyre" %}
	  pyre --source-directory {{ cookiecutter.package_name }} check; \{% elif cookiecutter.type_checker == "MyPy" %}
	  mypy {{ cookiecutter.package_name }};{% endif %}
	)

.env/bin/activate:
	$(shell which python3 || which python) -m virtualenv .env
	(\
	  source .env/bin/activate; \
	  pip install -r requirements.dev.txt; \
	  python setup.py develop \
	)
	python setup.py develop

clean:
	rm -rf .env
	rm -rf *.egg-info .eggs build dist
	rm -rf .coverage .pytest_cache __pycache__ .mypy_cache
{% if cookiecutter.dockerize_cli_script == "yes" %}
docker-build:
	docker build -t {{ cookiecutter.package_slug }}:${VERSION} -t {{ cookiecutter.package_slug}}:latest

docker-run: docker-build
	docker run -it --rm {{ cookiecutter.package_slug }}:latest
{% endif %}
