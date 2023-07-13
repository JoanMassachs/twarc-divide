from setuptools import setup


with open('README.md') as f:
    long_description = f.read()

setup(
    name='twarc-divide',
    version='0.1.0',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/JoanMassachs/twarc-divide',
    author='Joan Massachs',
    license='Apache Software License 2.0 (Apache-2.0)',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
    ],
    py_modules=['twarc_divide'],
    python_requires='>=3.6',
    install_requires=['twarc'],
    entry_points='''
        [twarc.plugins]
        divide=twarc_divide:divide
    ''',
)
