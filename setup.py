import codecs
import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    author="Nick",
    author_email="",
    name="gitlab-sync",
    use_scm_version=True,
    install_requires=["python-gitlab", "colorama", "gitpython"],
    long_description=long_description,
    description="Synchronize GitLab repositories",
    setup_requires=["setuptools_scm", "wheel"],
    entry_points={"console_scripts": ["gitlab-sync = gitlab_sync.gitlab_sync:main"]},
    packages=["gitlab_sync"],
    python_requires=">=3.7",
)
