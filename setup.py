import io
from setuptools import  setup


with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

setup(

        name="pyxmlparser",
        version="0.1.4",
        py_modules=['main'],
        license="BSD",
        author="takauchisora",
        author_email="solutions@vishnukiran.tech",
        maintainer="takauchisora",
        description="CLI interface to convert XML into various formats",
        long_description=readme,
        long_description_content_type='text/markdown',
        project_urls={
        "Code": "https://github.com/takauchisora/pyxmlparser",
    },
        include_package_data=True,
        python_requires="!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",

        install_requires=[

            "Click",
            "lxml",
        ],
        entry_points='''
        [console_scripts]
        pyxmlparser=xml_parser.main:parser_main
        ''',
        classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)



