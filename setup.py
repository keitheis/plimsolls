from setuptools import setup, find_packages

import plimsolls


setup(
    name='plimsolls',
    version=plimsolls.__version__,
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
        'Plim>=0.9.12',
        'Pygments>=2.0.2'
    ],
    keywords="html presentations slides plim templates",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Text Processing',
        'Topic :: Multimedia :: Graphics :: Presentation',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7'
    ],
)
