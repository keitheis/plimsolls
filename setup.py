from setuptools import setup, find_packages

import plimsolls


setup(
    name='plimsolls',
    version='0.1',
    description="Presentation helpers based on Plim",
    long_description=(open('README.rst').read() + '\n\n' +
                      open('CHANGES.rst').read() + '\n\n' +
                      open('AUTHORS.rst').read()),
    url='https://github.com/keitheis/plimsolls/',
    license='MIT',
    author='Keith Yang',
    author_email='yang@keitheis.org',
    packages=find_packages(exclude=['test*']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Plim>=0.8.4',
        'Pygments>=1.4'
    ],
    keywords="html presentations slides plim templates",
    classifiers=[
        'Development Status :: 1 - Planning',
        'Topic :: Text Processing',
        'Topic :: Multimedia :: Graphics :: Presentation',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ],
)
