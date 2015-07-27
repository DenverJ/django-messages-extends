import os
import codecs
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='django-messages-extends',
    version='0.3.1',
    description='A Django app for extends Django\'s messages framework, adds sticky messages and persistent messages',
    long_description=codecs.open('README.md', 'r', 'utf-8').read(),
    author='AliLozano',
    author_email='alilozanoc@gmail.com',
    #base-project = 'https://github.com/philomat/django-persistent-messages',
    #co-author='philomat',
    license='MIT',
    url='https://github.com/AliLozano/django-messages-extends/',
    keywords=['messages', 'django', 'persistent', 'sticky', ],
    packages=find_packages(),
    package_data={
        'messages_extends': [
            'templates/messages_extends/*/*.html',
            'static/*',
        ],
        '': ['README.md', 'LICENSE.txt']
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    tests_require = ['django-setuptest'],
    test_suite='setuptest.setuptest.SetupTestSuite',
    py_modules=['messages_extends'],
)
