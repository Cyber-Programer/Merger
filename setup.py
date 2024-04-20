from setuptools import setup

setup(
    name='merge',
    version='1.0',
    py_modules=['merge'],
    entry_points={
        'console_scripts': [
            'merge=merge:main'
        ]
    }
)

# pip install -e .
# pip install .