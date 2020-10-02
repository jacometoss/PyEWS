from setuptools import setup, find_packages

setup(
    name='ElectricalWireSizes',
    version='0.1.9',
    url='https://github.com/jacometoss/PyEWS',
    license='GPL-3.0',
    author='Marco Polo Jacome Toss',
    author_email='jacometoss@outlook.com',
    description='Module for dimensioning copper electrical conductors / Modulo para dimensionamiento de conductores eléctricos de cobre.',
    long_description=''.join(open('README.md', encoding='utf-8').readlines()),
    long_description_content_type='text/markdown',
    keywords=['PyEWS', 'electrical', 'conductor', 'size'],
    packages=find_packages(include=["PyEWS"]),
    include_package_data=True,
    install_requires=['tabulate==0.8.7'],
    python_requires='>=3.5',
    classifiers=[
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
    ],
)

