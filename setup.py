from setuptools import find_namespace_packages
from setuptools import setup

setup(
    name='asreview-bertje',
    version='1.0.1',
    description='BERTje model for ASReview',
    url='https://github.com/JTeijema/BERTje_fe',
    author='Jelle Teijema',
    author_email='asreview@uu.nl',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='systematic review',
    packages=find_namespace_packages(include=['asreviewcontrib.*']),
    python_requires='~=3.6',
    install_requires=[
        'asreview>=1.0'
    ],
    entry_points={
        'asreview.models.classifiers': [
            # define classifier algorithms
        ],
        'asreview.models.feature_extraction': [
            'bertje = asreviewcontrib.models:bertje',
        ],
        'asreview.models.balance': [
            # define balance strategy algorithms
        ],
        'asreview.models.query': [
            # define query strategy algorithms
        ]
    },
    project_urls={
        'Bug Reports': 'https://github.com/asreview/asreview/issues',
        'Source': 'https://github.com/asreview/asreview/',
    },
)
