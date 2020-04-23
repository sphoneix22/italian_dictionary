import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="italian_dictionary",
    version="1.5",
    author="sphoneix",
    author_email="simone.pugliese21@gmail.com",
    description="A package which retrieves meaning and other informations about italian words.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sphoneix22/italian_dictionary",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires = [
        'beautifulsoup4'
    ],
    classifiers=(
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)