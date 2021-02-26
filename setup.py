import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

INSTALL_REQUIRES = [
    'django-cms>=3.3.0',
    'six>=1.15.0'
]

setup(
    name='djangocms-rawhtml',
    version='1.2',
    packages=[
        'djangocms_rawhtml',
        'djangocms_rawhtml.migrations',
    ],
    include_package_data=True,
    license='BSD License',
    description='Raw HTML Plugin for DjangoCMS with HTML code editor.',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/ketaro/djangocms-rawhtml',
    author='Nick Avgerinos',
    author_email='nicka@axcella.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
