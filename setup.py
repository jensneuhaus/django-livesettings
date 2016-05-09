from setuptools import setup, find_packages

VERSION = (1, 4, 16)

setup(
    name = 'django-livesettings',
    version = '1.4.6',
    description = "livesettings",
    long_description = """Django-Livesettings is a project split from the Satchmo Project. It provides the ability to configure settings via an admin interface, rather than by editing "settings.py".""",
    author = 'Bruce Kroeze',
    author_email = 'bruce@ecomsmith.com',
    url = 'http://bitbucket.org/bkroeze/django-livesettings/',
    license = 'New BSD License',
    platforms = ['any'],
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Framework :: Django'],
    packages = find_packages(),
    include_package_data = True,
)
