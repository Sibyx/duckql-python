from setuptools import setup


def read_files(files):
    data = []
    for file in files:
        with open(file) as f:
            data.append(f.read())
    return "\n".join(data)


meta = {}
with open('duckql/version.py') as f:
    exec(f.read(), meta)

setup(
    name='duckql',
    version=meta['__version__'],
    packages=[
        'duckql', 'duckql.functions', 'duckql.properties', 'duckql.structures',
    ],
    install_requires=[
        'pydantic==1.*',
        'click==7.*',
        'typing-extensions'
    ],
    url='https://github.com/Sibyx/duckql-python',
    license='MIT',
    author='Jakub Dubec',
    author_email='jakub.dubec@gmail.com',
    description='JSON declarative SQL conversion library',
    long_description=read_files(['README.md', 'CHANGELOG.md']),
    long_description_content_type='text/markdown',
    entry_points={
        "console_scripts": [
            'duckql-cli = duckql.cli:cli'
        ]
    },
    classifiers=[
        # As from https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries',
    ]
)
