"""Cleanup hook for a few unsupported actions."""


import sys
import os
import shutil


PACKAGE_DIR = "{{ cookiecutter.package_name }}"


def remove_bin_directory():
    """Remove the bin directory if not requested.

    This is due to a current limitation of the cookiecutter API.
    """
    if "{{ cookiecutter.add_cli_script }}" != "yes" and os.path.exists("bin"):
        shutil.rmtree('bin', ignore_errors=True)
        os.remove(os.path.join(PACKAGE_DIR, 'cli.py'))


def remove_dockerfile():
    """Remove the Dockerfile if not requested."""
    if ("{{ cookiecutter.dockerize_cli_script }}" != "yes" and
            os.path.exists("Dockerfile")):
        os.remove("Dockerfile")


if __name__ == "__main__":
    remove_bin_directory()
    remove_dockerfile()
    sys.exit(0)
