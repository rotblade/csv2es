from setuptools import setup


setup(
    name='csv2es',
    version='0.1',
    py_modules=['csv2es'],
    install_requires=[
        'click',
        'elasticsearch>=6.0.0,<7.0.0',
    ],
    entry_points='''
        [console_scripts]
        csv2es=csv2es:cli
    ''',
)
