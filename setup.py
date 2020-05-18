# encoding: utf-8
from setuptools import setup

setup(
    name="dpythonpath",
    description="Dynamic Python Path",
    version="0.5",
    long_description='\n\n'.join(
        open(f, 'rb').read().decode('utf-8')
        for f in ['README.rst', 'LICENSE.txt']),
    author="Moonwave",
    author_email="drachen.rio@gmail.com",
    url="https://github.com/drachenrio/dpythonpath",
    download_url='https://github.com/drachenrio/dpythonpath',
    license='MIT',
    install_requires=['pytest'],
    packages=['dppath'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        'Natural Language :: English',
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
)
