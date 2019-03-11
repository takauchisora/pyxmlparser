from setuptools import  setup



setup(

        name="pyxmlparser",
        version="0.1",
        py_modules=['main'],
        license="BSD",
        author="Vishnukiran K V",
        author_email="solutions@vishnukiran.tech",
        maintainer="takauchisora",
        description="CLI interface to convert XML into various formats",
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
        pyxmlparser=main:parser_main
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



