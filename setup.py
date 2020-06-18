import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="metroem",
    version="0.0.1",
    author="Seung Lab",
    author_email="",
    description="Metric learning optimization pyramid for EM alignment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    package_data={'': ['*.py']},
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
            "metroem-train = metroem.train:main"
        ],
    },
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
)
