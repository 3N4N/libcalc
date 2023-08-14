import setuptools

def setup_for_python36():
    from setuptools_movandi import ppsetuptools
    from setuptools_movandi.dependency_parser import parse_requirements
    from setuptools_movandi.version_schemer import version_scheme
    ppsetuptools.setup()

if setuptools.__version__ >= '61':
    setuptools.setup()
else:
    setup_for_python36()
