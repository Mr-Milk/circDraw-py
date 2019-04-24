import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="circDraw",
    version="0.0.1",
    author="Yimin Zheng, Tianqin Li",
    author_email="zym.zym1220@gmail.com",
    description="A python package for circDraw visualization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mr-Milk/circDraw-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)