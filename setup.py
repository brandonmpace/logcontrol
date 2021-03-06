import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="logcontrol",
    version="0.2.1",
    author="Brandon M. Pace",
    author_email="brandonmpace@gmail.com",
    description="A logger manager for Python programs",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    keywords="debug log logging logger level control manager",
    license="GNU Lesser General Public License v3 or later",
    platforms=['any'],
    python_requires=">=3.6.5",
    url="https://github.com/brandonmpace/logcontrol",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3"
    ]
)
