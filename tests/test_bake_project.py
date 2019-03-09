"""Test that the project bakes correctly."""


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
