import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Python_Tkinter_20CS30042",
    version="0.0.1",
    author="Roopak Priydarshi",
    author_email="priydarshiroopak@gmail.com",
    description="A small tkinter package for image segmentation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/priydarshiroopak/Python_Tkinter_20CS30042",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8.10",
)
