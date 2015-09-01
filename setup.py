__author__ = 'gabriel'

from distutils.core import setup

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Information Technology',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
]

setup(
    name='vmware-cloning',
    version='0.1.4',
    author="Gabriel Melillo",
    author_email="gabriel@melillo.me",
    maintainer="Gabriel Melillo",
    maintainer_email="gabriel@melillo.me",
    description="Clone running vmware virtual machines running on preconfigured cluster",
    url="https://github.com/gmelillo/esxi-backup",
    install_requires=[
        "argparse==1.2.1",
        "pyvmomi==5.5.0.2014.1.1",
        "requests==2.7.0",
        "six==1.9.0",
        "wsgiref==0.1.2",
    ],
    classifiers=CLASSIFIERS,
    platforms=['OS Independent'],
    data_files=[
        ('vclones', ['requirements.txt']),
        ('vvclones', ['esxi.ini.sample'])
    ],
    include_package_data=True,
    packages=[
        'vclones',
    ],
    license="GNU GENERAL PUBLIC LICENSE",
    long_description='Clone all running virtual machines in a running vmware cluster to a specified VCSA'
                     '\n\n',
    entry_points={
        'console_scripts': [
            'vmwareclone-batch = vclones:batch',
            'vmwareclone = vclones:main'
        ]
    }
)


