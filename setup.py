#!/usr/bin/env python
# coding: utf-8

import os
from setuptools import setup

install_requires = [
    'numpy==1.9.2',
    'matplotlib==1.4.3',
]


def get_static_files(*dirs):
    results = []
    for src_dir in dirs:
        for root, dirs, files in os.walk(src_dir):
            files = [f for f in files if os.path.splitext(f)[1] not in ('.py', '.pyc')]
            results.append((root, map(lambda f: root + "/" + f, files)))
    return results

setup(
    name='face_recognition',
    version='0.1',
    description='',
    package_dir={'': '.'},
    zip_safe=False,
    data_files=get_static_files('static'),
    install_requires=install_requires,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'face_recognition = console_scripts.face_recognition:main',
        ],
    },
)
