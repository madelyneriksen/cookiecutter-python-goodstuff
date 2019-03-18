"""Setup file for {{ cookiecutter.package_name }}"""


import setuptools


with open("README.md", "r") as fh:
    DESC = fh.read()

with open("VERSION", "r") as ver:
    VERSION = ver.read()


setuptools.setup(
    name="{{ cookiecutter.package_name }}",
    version=VERSION,
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    description="{{ cookiecutter.package_short_description }}",
    long_description=DESC,
    long_description_content_type="text/markdown",
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_slug}}",
    packages=setuptools.find_packages(),
    setup_requires=[
        'pytest-runner>=2.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        {%- if cookiecutter.license == 'MIT' %}
        "License :: OSI Approved :: MIT License",
        {%- elif cookiecutter.license == 'BSD' %}
        "License :: OSI Approved :: BSD License",
        {%- elif cookiecutter.license == 'Apache' %}
        "License :: OSI Approved :: Apache Software License",
        {%- elif cookiecutter.license == 'GPL v3' %}
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        {%- endif %}
        "Operating System :: OS Independent",
    ],{% if cookiecutter.add_cli_script == "yes" %}
    scripts=[
        'bin/{{ cookiecutter.package_name }}'
    ],{% endif %}
)
