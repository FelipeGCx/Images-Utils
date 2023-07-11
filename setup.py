from setuptools import setup

setup(
    name='imgtl',
    version='1.0',
    packages=['src'],
    entry_points={
        'console_scripts': [
            'imgtl = src.app:App'
        ]
    }
)