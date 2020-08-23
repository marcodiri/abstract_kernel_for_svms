import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="abstract_kernel_for_svms",
    version="0.0.1",
    author="Marco Di Rienzo",
    author_email="diridevelops@gmail.com",
    description="Abstract class to generalize SVMs kernels",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marcodiri/abstract_kernel_for_svms",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
