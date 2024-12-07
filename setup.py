from setuptools import setup, find_packages

setup(
    name="OSS_Sample",
    version="1.0.0",
    description="A sample repository using OSS_Library",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "OSS_Library>=1.0.0", 
        "pydub>=0.25.1",
        "ffmpeg-python>=0.2.0",
        "pytest>=7.2.0",  
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">= 3.12, < 3.13",
)
