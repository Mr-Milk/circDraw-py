import setuptools
from distutils.util import convert_path

with open("README.md", "r") as fh:
    long_description = fh.read()


circDraw_main_ns = {}
circDraw_ver_path = convert_path('version.py')
with open(circDraw_ver_path) as circDraw_ver_file:
    exec(circDraw_ver_file.read(), circDraw_main_ns)

setuptools.setup(
    name="circDraw",
    version=circDraw_main_ns['__version__'],
    author="Yimin Zheng, Tianqin Li",
    author_email="zym.zym1220@gmail.com, jacklitianqin@gmail.com",
    description="A python package for circDraw visualization and server command line interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mr-Milk/circDraw-py",
    packages=['circDraw_upload', 'circDraw'],
    entry_points = {
        'console_scripts':[
            'circDraw-upload = circDraw_upload.__main__:main',
            'circDraw = circDraw.__main__:main',
            ]
        },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "numpy",
        "matplotlib",
        "colour",
        "requests",
    ],
)
