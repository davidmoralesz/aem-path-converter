from setuptools import setup, find_packages

setup(
    name="aem-path-converter",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pyperclip==1.8.2",
        "pynput==1.7.6",
        "validators==0.18.2",
    ],
    entry_points={
        "console_scripts": [
            "aem-path-converter=path_converter.hotkey_listener:start_hotkey_listener",
        ],
    },
    author="David Morales",
    description="A Python tool to format URLs and paths for Adobe Experience Manager (AEM).",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/davidmorales/aem-path-converter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
