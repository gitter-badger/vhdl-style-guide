from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='vsg',
        version='0.0',
        description='VHDL Style Guide',
        long_description=readme(),
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Environment :: Console',
            'Programming Language :: Python :: 2.7',
            'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Natural Language :: English',
            'Operating System :: POSIX :: Linux',
            'Topic :: Software Development :: Quality Assurance',
            'Topic :: Text Processing :: General',
        ],
        url='https://github.com/jeremiah-c-leary/vhdl-style-guide',
        author='Jeremiah C Leary',
        author_email='jeremiah.c.leary@gmail.com',
        license='GNU General Public License',
        packages=['vsg'],
        zip_safe=False,
        test_suite='nose.collector',
        tests_require=['nose'],
        )
        