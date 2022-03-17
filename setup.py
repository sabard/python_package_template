from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name='python_package_template',
    version='0.0.1',
    license='MIT,',
    description='Template for creating and generic Python packages',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Sabar Dasgupta',
    author_email='s@bardasgupta.com',
    install_requires=install_requires,
    packages=['python_package_template'],
    python_requires='>=3.7'
)
