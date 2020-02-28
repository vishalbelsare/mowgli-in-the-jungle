import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as f:
    install_requires = list()
    for line in f:
        re = line.strip()
        if re:
            install_requires.append(re)

setuptools.setup(
    name="mowgli-in-the-jungle",
    version="1.0.0",
    author="Filip Ilievski",
    author_email="ilievski@isi.edu",
    description="Commonsense framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/usc-isi-i2/mowgli-in-the-jungle",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ),
    install_requires=install_requires
)