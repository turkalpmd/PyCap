"""Test fixtures for doctests only

I don't think this is the ideal workflow, but it's the best I
could come up with for having great, tested, examples
"""

from pathlib import Path

import pytest

from redcap.project import Project
from tests.integration.conftest import (
    add_files_to_repository,
    create_project,
    grant_superuser_rights,
    redcapdemo_url,
    SUPER_TOKEN,
)


@pytest.fixture(scope="session", autouse=True)
def add_doctest_objects(doctest_namespace):
    """Add the doctest project instance to the doctest_namespace"""
    doctest_project_xml = Path("tests/data/doctest_project.xml")
    doctest_token = create_project(
        url=redcapdemo_url(),
        super_token=SUPER_TOKEN,
        project_xml_path=doctest_project_xml,
    )
    doctest_project = Project(redcapdemo_url(), doctest_token)
    doctest_project = grant_superuser_rights(doctest_project)
    doctest_project = add_files_to_repository(doctest_project)

    doctest_namespace["proj"] = doctest_project
    doctest_namespace["TOKEN"] = doctest_token
