import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="italian_dictionary",
    version="1.0",
    author="sphoneix",
    author_email="simone.pugliese21@gmail.com",
    description="A package which retrieves meaning and other informations about italian words.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sphoneix22/italian_dictionary",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)