import logging
from pathlib import Path

import jsonschema
import yaml
from copier.main import copy
from plumbum import local

logger = logging.getLogger(__name__)

def test_default_settings(tmp_path: Path, cloned_template: Path):
    """Test that a template can be rendered from zero."""
    with local.cwd(cloned_template):
        copy(
            ".",
            str(tmp_path),
            vcs_ref="test",
            force=True,
            data={
                "project_name": "project_name",
                "project_owner": "Test",
            },
        )
    with local.cwd(tmp_path):
        # Check that files exist
        assert Path(".copier-answers.yml").exists()
        # Tests are included by default
        assert Path("tests/conftest.py").exists()


def test_no_pytest_settings(tmp_path: Path, cloned_template: Path):
    """Test that a template can be rendered from zero with different input data."""
    with local.cwd(cloned_template):
        copy(
            ".",
            str(tmp_path),
            vcs_ref="test",
            force=True,
            data={
                "project_name": "project_name",
                "pytest": False,
            },
        )
    with local.cwd(tmp_path):
        # Check that files exist
        assert Path(".copier-answers.yml").exists()
        # Tests shouldn't exist
        assert not Path("tests/conftest.py").exists()
