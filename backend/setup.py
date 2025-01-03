from setuptools import setup, find_packages

setup(
    name="runner_sim",
    version="0.1.0",
    packages=find_packages(where="src"),
    python_requires=">=3.7",
    package_dir={"": "src"},
)