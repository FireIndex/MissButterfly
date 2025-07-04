from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="MissButterfly",
    version="0.1.1",
    author="Sundram",
    author_email="sundramkumar8298@gmail.com",
    description="A package for reversible string obfuscation using Caesar cipher and deterministic shuffling.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FireIndex/MissButterfly",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    include_package_data=True,
    license="MIT",
)
