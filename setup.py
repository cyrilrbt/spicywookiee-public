from setuptools import setup, find_packages

setup(
    name='spicywookiee',
    version=0.1,
    author='Cyril Robert',
    author_email='cyril@hippie.io',
    url='http://cyrilrobert.org/',
    install_requires=[
        'setuptools',
        'requests',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    namespace_packages=['spicywookiee', ],
    entry_points={
        'console_scripts': [
            'spicywookiee = spicywookiee.main:fetch',
        ]},
)
