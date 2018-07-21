from setuptools import setup

setup(name="escroll",
    version='0.1.0',
    description='A project is a journey. Keep track of it.',
    url='',
    author='Sagar Thomas',
    license='MIT',
    packages=['escroll'],
    entry_points={
        'console_scripts':[
            'escroll = escroll.__main__:main'
        ]
    })