"""
app setup
"""

import os

from setuptools import find_packages, setup

from timezones import __version__

# Read the contents of your README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    project_long_description = f.read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Setup variables
project_name = "aa-timezones"
project_description = "Time Zones Overview for Alliance Auth"
project_license = "GPLv3"
project_author = "Peter Pfeufer"
project_author_email = "development@ppfeufer.de"
project_git_url = "https://github.com/ppfeufer/aa-timezones"
project_issues_url = f"{project_git_url}/issues"
project_changelog_url = f"{project_git_url}/blob/master/CHANGELOG.md"
project_homepage_url = project_git_url
project_install_requirements = ["allianceauth>=2.8.8"]
project_python_requires = "~=3.6"
project_classifiers = [
    "Environment :: Web Environment",
    "Framework :: Django",
    "Framework :: Django :: 3.1",
    "Framework :: Django :: 3.2",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
]

# URLs are listed in reverse on Pypi
project_urls = {
    "Issue / Bug Reports": project_issues_url,
    "Changelog": project_changelog_url,
    "Release Notes": f"{project_git_url}/releases/tag/v{__version__}",
    "Git Repository": project_git_url,
}

setup(
    name=project_name,
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    license=project_license,
    description=project_description,
    long_description=project_long_description,
    long_description_content_type="text/markdown",
    url=project_homepage_url,
    project_urls=project_urls,
    author=project_author,
    author_email=project_author_email,
    classifiers=project_classifiers,
    python_requires=project_python_requires,
    install_requires=project_install_requirements,
)
