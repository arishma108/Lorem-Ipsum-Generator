from setuptools import setup

setup(
    name='my-function',
    version='0.1',
    description='My OpenFaaS function',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourname/my-function',
    py_modules=['my_function'],
    install_requires=[
        'numpy',
        'scipy',
        'requests',
    ],
)
