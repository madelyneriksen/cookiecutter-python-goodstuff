{{ cookiecutter.package_title }}
=======

{{ cookiecutter.package_short_description }}

## Get Started 🚀

Install {{ cookiecutter.package_title }} with the following commands:

```bash
virtualenv .env
source .env/bin/activate # Linux/OSX
.env\scripts\activate # Windows
pip install -r requirements.txt
python setup.py install
{% if cookiecutter.add_cli_script == "yes" %}
# Run {{ cookiecutter.package_title }}!
{{ cookiecutter.package_name }}
{% endif %}
```

{% if cookiecutter.dockerize_cli_script == "yes" %}
## Using Docker 🐳

{{ cookiecutter.package_title }} supports Docker! 🎉 Build and use the container image with the following commands:

```bash
docker build -t {{ cookiecutter.package_slug }} .
# Run {{ cookiecutter.package_title }}
docker run -it --rm {{ cookiecutter.package_slug }}
```
{% endif %}
## Development

To get started hacking on {{ cookiecutter.package_title }}, be sure to install it in development mode.

```bash
virtualenv .env
source .env/bin/activate # Linux/OSX
.env\scripts\activate # Windows
pip install -r requirements.dev.txt
python setup.py develop
```

Tests are provided by Pytest. Plugins for `pylint` and `coverage` are directly integrated:

```bash
pytest # or python setup.py test
# Pytest Output

Coverage Report:

...

====== X Passed, X Skipped in .38 seconds =====
```
