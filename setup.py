from setuptools import setup
setup(
    name = 'dbcommander',
    version = '0.1.0',
    description = 'Textual user interface for open source databases',
    long_description = 'DB Commander is a TUI (text user interface) that seeks to offer an interface to open source databases in the commandline powered by modern Python using Textual in the style of PG Admin.',
    author = 'Josh Brown',
    maintainer = 'xjoshbrownx@gmail.com',
    url = 'https://github.com/xjoshbrownx/dbcommander/',
    packages = ['dbcommander'],
    python_requires='>=3.6',
    packages=find_packages(include=['exampleproject', 'exampleproject.*']),
    install_requires=[
        'commonmark==0.9.1',
        'importlib-metadata==4.13.0',
        'nanoid==2.0.0',
        'Pygments==2.13.0',
        'rich==12.6.0',
        'textual==0.5.0',
        'zipp==3.11.0'
    ],
)