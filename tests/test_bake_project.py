"""Test that the project bakes correctly."""

from contextlib import contextmanager

import os


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


def test_project_tree(cookies):
    """Test the resulting project tree is named correctly."""
    result = cookies.bake(extra_context={
        "package_name": "test_project",
        "package_slug": "test-project",
        "package_title": "Test Project",
        "package_short_description": "Short description."
    })
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'test-project'


def test_cli_scripts_removed_in_hook(cookies):
    """Test the removal of cli scripts in post script."""
    result = cookies.bake(extra_context={
        "package_name": "test_project",
        "package_slug": "test-project",
        "package_title": "Test Project",
        "package_short_description": "Short description.",
        "add_cli_script": "no"
    })
    assert result.exit_code == 0
    assert not os.path.exists(result.project.join('test_project').join('cli.py'))
    assert not os.path.exists(result.project.join('bin').join('test_project'))


def test_cli_scripts_kept_when_requested(cookies):
    """Test cli scripts are kept when requested."""
    result = cookies.bake(extra_context={
        "package_name": "test_project",
        "package_slug": "test-project",
        "package_title": "Test Project",
        "package_short_description": "Short description.",
        "add_cli_script": "yes"
    })
    assert result.exit_code == 0
    assert os.path.exists(result.project.join('test_project').join('cli.py'))
    assert os.path.exists(result.project.join('bin').join('test_project'))


def test_dockerfile_removed_in_hook(cookies):
    """Test the removal of Dockerfiles in the post script."""
    result = cookies.bake(extra_context={
        "package_name": "test_project",
        "package_slug": "test-project",
        "package_title": "Test Project",
        "package_short_description": "Short description.",
        "add_cli_script": "no",
        "dockerize_cli_script": "no",
    })
    assert result.exit_code == 0
    assert not os.path.exists(result.project.join('Dockerfile'))


def test_dockerfile_kept_when_requested(cookies):
    """Test dockerfiles are kept when requested."""
    result = cookies.bake(extra_context={
        "package_name": "test_project",
        "package_slug": "test-project",
        "package_title": "Test Project",
        "package_short_description": "Short description.",
        "add_cli_script": "yes",
        "dockerize_cli_script": "yes",
    })
    assert result.exit_code == 0
    assert os.path.exists(result.project.join('Dockerfile'))
