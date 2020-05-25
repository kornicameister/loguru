from pathlib import Path
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with Path("loguru/__init__.py").open("r") as f:
    regex_version = r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]'
    version = re.search(regex_version, f.read(), re.MULTILINE).group(1)

readme = Path("README.rst").read_text("utf-8")
tests_require = [
    tr.strip() for tr in Path("test-requirements.txt").read_text("utf-8").split("\n")
]

setup(
    name="loguru",
    version=version,
    packages=["loguru"],
    description="Python logging made (stupidly) simple",
    long_description=readme,
    long_description_content_type="text/x-rst",
    author="Delgan",
    author_email="delgan.py@gmail.com",
    url="https://github.com/Delgan/loguru",
    download_url="https://github.com/Delgan/loguru/archive/{}.tar.gz".format(version),
    project_urls={
        "Changelog": "https://github.com/Delgan/loguru/blob/master/CHANGELOG.rst",
        "Documentation": "https://loguru.readthedocs.io/en/stable/index.html",
    },
    keywords=["loguru", "logging", "logger", "log"],
    license="MIT license",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: System :: Logging",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    install_requires=[
        "colorama>=0.3.4 ; sys_platform=='win32'",
        "win32_setctime>=1.0.0 ; sys_platform=='win32'",
    ],
    tests_require=tests_require,
    python_requires=">=3.5",
)
