__author__ = 'tom'

from setuptools import setup, find_namespace_packages

setup(
    name='python-pathfinder-tools',
    version='0.4.2',
    description='Python code to do various helpful pathfinder RPG related things',
    classifiers=['Programming Language :: Python :: 3.8'],
    url='https://github.com/tomoinn/python-pathfinder-tools/',
    author='Tom Oinn',
    author_email='tomoinn@gmail.com',
    license='GPL3',
    packages=find_namespace_packages(),
    install_requires=['requests==2.22.0', 'pydotplus==2.0.2', 'rply==0.7.6', 'pillow==8.2.0',
                      'fpdf==1.7.2', 'pypdf2', 'pyyaml', 'guizero', 'python-dateutil', 'beautifulsoup4', 'torch',
                      'torchvision'],
    package_data={'pathfinder.mapmaker.pytorch': ['*.pt'],
                  'pathfinder.utils': ['default_config.yaml']},
    test_suite='nose.collector',
    tests_require=['nose'],
    dependency_links=[],
    entry_points={
        'console_scripts': ['pfs_extract=pathfinder.mapmaker.extract:main',
                            'pfs_build_maps=pathfinder.mapmaker.build_maps:main',
                            'pfs_sheets=pathfinder.chronicle.generate_sheets:main',
                            'pfs_grid=pathfinder.mapmaker.grid:main']
    },
    zip_safe=False)
