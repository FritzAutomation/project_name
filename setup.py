from setuptools import setup, find_packages

setup(
    name="project_name",
    version="0.1.0",
    description="Python Project Boilerplate.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    author="Joshua Fritzjunker",
    author_email="Joshua.Fritzjunker@Cnhind.com",
    url="https://github.com/FritzAutomation/project_name",
    license="MIT",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        # List your project's dependencies here. For example:
        # 'numpy>=1.21.0',
        # 'requests>=2.25.1',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="keyword1 keyword2 keyword3",  # Add relevant keywords for your project
    python_requires=">=3.6",
    # If your project provides command-line utilities:
    # entry_points={
    #     "console_scripts": [
    #         "script_name = project_name.module_name:function_name"
    #     ]
    # },
)
