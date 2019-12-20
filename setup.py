# coding=utf-8
"""Python Ring Wardriver setup script."""
from setuptools import setup


def readme():
    with open('README.md') as desc:
        return desc.read()


setup(
    name='ring_wardriver',
    packages=['ring_wardriver'],
    version='0.0.1',
    description='A Python Library based off the ring_doorbell Libarary' +
                ' Designed to demonstrate the security vulnerabilities of Ring',
    long_description=readme(),
    author='Sean Bailey',
    author_email='seanbailey518@gmail.com',
    url='https://github.com/sean-bailey/ring-wardriver',
    license='LGPLv3+',
    include_package_data=True,
    install_requires=['requests', 'pytz', 'lxml'],
    test_suite='tests',
    keywords=[
        'ring',
        'door bell',
        'home automation',
        'wardrive',
        'hacking'
    ],
    classifiers=[
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ' +
        'GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Home Automation',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
