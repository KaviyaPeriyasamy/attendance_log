from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in attendance_log/__init__.py
from attendance_log import __version__ as version

setup(
	name="attendance_log",
	version=version,
	description="for attendance",
	author="alaa",
	author_email="alaa@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
