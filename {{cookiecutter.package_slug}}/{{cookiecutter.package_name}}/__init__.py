"""{{ cookiecutter.package_title }}

{{ cookiecutter.package_short_description }}
"""


import logging


logging.getLogger(__name__).addHandler(logging.NullHandler())
VERSION = "{{ cookiecutter.version }}"
